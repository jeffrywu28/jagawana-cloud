'''
    Created on May 2021
    Nico Renaldo <nicorenald@gmail.com>
'''

# Deploy Command with Google Cloud SDK
#gcloud functions deploy prediction --region asia-southeast2 --runtime python37 --trigger-topic do_predict

import json
import librosa
import base64
import numpy as np
import uuid
from google.api_core.client_options import ClientOptions
from googleapiclient import discovery
from google.cloud import bigquery
from google.cloud import storage

# Basic data about your project
project_id = "your-project-id"
bucket_name = "your-bucket-name"
bucket_folder = 'your-bucket-folder-name'
client_options = ClientOptions(api_endpoint=endpoint)

# Endpoint of the ML Model deployed on AI Platform
endpoint = 'your-ml-endpoint'
ml = discovery.build('ml-name', 'ml-version', client_options=client_options)
model_name = 'projects/{}/models/{}/versions/{}'.format(project, model, version)

# BigQuery
bq_client = bigquery.Client(project=project_id)
table_id = "project-id.dataset-name.table-name"

# Cloud Storage
storage_client = storage.Client()

# Configuration for Audio Data
class conf:
    sr = 16000
    duration = 3
    hop_length = 340*duration
    fmin = 20
    fmax = sr // 2
    n_mels = 128
    n_fft = n_mels * 20
    samples = sr * duration
    epochs = 30

# Functions to denoise and split audio into clips, returning interval of each clip
def split_audio(audio_data, w, h, threshold_level, tolerence=10):
    split_map = []
    start = 0
    data = np.abs(audio_data)
    threshold = threshold_level*np.mean(data[:25000])
    inside_sound = False
    near = 0
    for i in range(0,len(data)-w, h):
        win_mean = np.mean(data[i:i+w])
        if(win_mean>threshold and not(inside_sound)):
            inside_sound = True
            start = i
        if(win_mean<=threshold and inside_sound and near>tolerence):
            inside_sound = False
            near = 0
            split_map.append([start, i])
        if(inside_sound and win_mean<=threshold):
            near += 1
    return split_map

# Download file from bucket to a temporary location
def download_file(filename):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(bucket_folder + filename)
    blob = blob.download_to_filename('/tmp/read_temp.wav')

# Extracting feature of waveform to Mel Spectogram
def feature(signal):
    spectrogram = librosa.feature.melspectrogram(signal, sr=conf.sr, n_mels=conf.n_mels, hop_length=conf.hop_length, n_fft=conf.n_fft, fmin=conf.fmin, fmax=conf.fmax)

    spectrogram = librosa.power_to_db(spectrogram)
    prediction_data = np.array(spectrogram)
    prediction_data = prediction_data.reshape(1, prediction_data.shape[0], prediction_data.shape[1], 1)
    return prediction_data

# Requesting an Online Prediction to AI Platform
def start_predict(feature):
    payload = {"instances" : feature.tolist()}
    request = ml.projects().predict(name=model_name,body=payload)
    response = request.execute()
    print(response["predictions"][0])
    if(max(response["predictions"][0]) > 0.7):
        idclass = np.argmax(response["predictions"][0])
        return  idclass
    else:
        return(99)

# Checking for duplicates filename
def check_query(clipname):
    QUERY = ('SELECT * FROM ' + table_id + ' WHERE idClip="' + clipname + '"')
    query_job = bq_client.query(QUERY)
    rows = len(list(query_job.result()))
    return rows

# Creating a Query on BigQuery Table
def insert_query(payload):
    exists = check_query(payload["idClip"])
    if(exists >= 1):
        print("UUID Exists, creating a new UUID")
        payload["idClip"] = str(uuid.uuid4())
        return insert_query(payload)
    else:
        print("No UUID found, writing query")
        rows_to_insert = [payload]
        errors = bq_client.insert_rows_json(table_id, rows_to_insert)
        if errors == []:
            print("New rows have been added.")
            return payload
        else:
            print("Encountered errors while inserting rows: {}".format(errors))

# Making a Payload for Querying
def make_payload(idAudioFile, idclass, intvl):
    clip_name = str(uuid.uuid4())
    message = {
        "idClip" : clip_name,
        "idAudioFile" : idAudioFile,
        "idClass" : int(idclass),
        "startInterval" : int(intvl[0]),
        "endInterval" : int(intvl[1]),
    }
    return message

# Main Functions, triggered by topic `do_predict` on Pub/Sub
def prediction(event, context):
    print("""This Function was triggered by messageId {} published at {}""".format(context.event_id, context.timestamp))
    if 'data' in event:
        message = base64.b64decode(event['data']).decode('utf-8')
        payload = json.loads(message)
        idAudioFile = payload["idAudioFile"]
    
    print("Downloading file")
    # Download File
    download_file(idAudioFile)

    # Load File
    print("Loading File")
    signal , rate = librosa.load('/tmp/read_temp.wav', sr=conf.sr)

    # Create Clips
    print("Cutting into Clips")
    sound_clips = split_audio(signal, 10000, 2500, 15, 10)
    
    if(sound_clips==[]):
        intvl = [0,len(signal)]
        prediction_data = feature(signal)
        result = start_predict(prediction_data)

        # Create Payload
        clip_payload = make_payload(idAudioFile, result, intvl)

        # Make Query
        insert_query(clip_payload)

    else:
        for intvl in sound_clips:
            # Predict Clips
            print("Start Querying")
            clip, index = librosa.effects.trim(signal[intvl[0]:intvl[1]], top_db=20, frame_length=512, hop_length=64)
            prediction_data = feature(clip)
            result = start_predict(prediction_data)

            # Create Payload
            clip_payload = make_payload(idAudioFile, result, intvl)

            # Make Query
            insert_query(clip_payload)