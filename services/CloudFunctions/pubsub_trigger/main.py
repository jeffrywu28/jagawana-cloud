'''
    Created on May 2021
    Nico Renaldo <nicorenald@gmail.com>
'''

# Deploy Command with Google Cloud SDK
#gcloud functions deploy prediction --region asia-southeast2 --runtime python37 --trigger-topic do_predict

import base64
import json
import uuid
from google.cloud import bigquery
from google.cloud import storage
from google.cloud import pubsub_v1

# Basic data about your project
project_id = "your-project-id"
bucket_name = "your-bucket-name"
bucket_folder = 'your-bucket-folder-name'
topic_target = 'do_predict'

# BigQuery
bq_client = bigquery.Client(project=project_id)
table_id = "project-id.dataset-name.table-name"

# Cloud Storage
storage_client = storage.Client()

# Checking for duplicates filename
def check_query(filename):
    QUERY = ('SELECT * FROM ' + table_id + ' WHERE idAudioFile="' + filename + '"')
    query_job = bq_client.query(QUERY)  # API request
    rows = len(list(query_job.result()))  # Waits for query to finish
    return rows

# Creating a Query on BigQuery Table
def insert_query(payload):
    exists = check_query(payload["idAudioFile"])
    if(exists >= 1):
        print("UUID Exists, creating a new UUID")
        payload["idAudioFile"] = str(uuid.uuid4())
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

# Creating a .wav file to temporary location from payload
def make_wavefile(data, idAudioFile):
    wave_bytes = bytes(eval(data))
    destination = "/tmp/" + idAudioFile + ".wav"
    with open(destination, mode='bw') as f:
        f.write(wave_bytes)
    print("Soundwave created at {}".format(destination))

# Making a Payload for Querying
def make_payload(payload, context):
    filename = str(uuid.uuid4())
    duration = len(payload["data"])/16000
    message = {
        "idAudioFile" : filename,
        "timestamp" : context.timestamp,
        "idDevice" : payload["idDevice"],
        "predictStatus" : "false",
        "duration" : int(duration),
        "Longitude" : payload["Longitude"],
        "Latitude" : payload["Latitude"],
        "idRegion" : 1
    }
    return message

# Creating a file on Cloud Storage
def write_storage(destination):
    source = "/tmp/temp.wav"
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination)
    blob.upload_from_filename(source)
    print("File uploaded to {}.".format(destination))

# Publishing a message to `do_predict` topic to trigger prediction functions
def publish_trigger(idAudioFile):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_target)
    payload = {
    "idAudioFile" : idAudioFile,
    }
    data = json.dumps(payload).encode("utf-8")
    future = publisher.publish(topic_path, data)
    print(future.result())
    print(f"Published messages to {topic_path}.")

# Main Functions, triggered by a message from device
def pubsub_trigger(event, context):
    print("""This Function was triggered by messageId {} published at {}""".format(context.event_id, context.timestamp))

    if 'data' in event:
        message = base64.b64decode(event['data']).decode('utf-8')
        payload = json.loads(message)
    
    new_payload = make_payload(payload, context)
    print('Payload {}!'.format(new_payload))

    sended_payload = insert_query(new_payload)
    make_wavefile(payload["data"], "temp")
    write_storage(bucket_folder + sended_payload["idAudioFile"])

    publish_trigger(sended_payload["idAudioFile"])

