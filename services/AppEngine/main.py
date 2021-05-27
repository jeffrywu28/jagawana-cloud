#created by Jeffry, feel free my telegram @jeffanzos
#This API purpose to connect data from the cloud so that it can be accessed by Android platform.
#You can change this App Engine to another service like VM instance,docker. This is 1 of the example, you can create your own API maybe with NodeJs, Django, etc.
#We use python 3.8 to run this Flask

from flask import Flask,request
from google.cloud import bigquery
import json

app = Flask(__name__)

#var
gcp_project = {YOUR GCP PROJECT ID} #please change with your gcp project id
public_url = {YOUR PUBLIC URL BUCKET STORAGE} #please change with your gcp storage bucket
bq_client = bigquery.Client(project=gcp_project)

#default home page, you can change anything at here.
@app.route('/')
def hello_world():
    return 'Hello, World!'

# getresult API endpoint with GET http request.
# how to use : https://project.appspot.com/getallresult 
# this API returns all of the result prediction data with a link to play predictable sound.
@app.route('/getallresult',methods=['GET'])
def hello():
    """Return a friendly HTTP greeting."""
    QUERY = ('SELECT idClip, r.idAudioFile, startInterval, endInterval, idDevice,region,longitude,latitude,timestamp,classifyResult,CONCAT("https://storage.googleapis.com/input-audio-pipeline/",r.idAudioFile) AS linkaudio FROM `gcp-project-id.jagawana_data.Result` r inner join `gcp-project-id.jagawana_data.IotInputdata` i on r.idAudioFile = i.idAudioFile inner join `gcp-project-id.jagawana_data.Class` c on r.idClass=c.idClass inner join `gcp-project-id.jagawana_data.Region` reg on i.idRegion= reg.idRegion')
    query_job = bq_client.query(QUERY)  # API request to bigquery
    df = query_job.to_dataframe() #parse query result to dataframe
    df['timestamp'] = df['timestamp'].astype(str) #convert timestamp format
    json_obj = json.dumps(df.to_dict('records')) #parse the dataframe to JSON
    return json_obj

# getresultid API endpoint with GET http request.
# how to use : https://project.appspot.com/getresultid?id=00696dc3-03ac-4c79-9c91-de3b040819dd
# this API returns 1 of the result prediction data.Enter idClip to use.
@app.route('/getresultid',methods=['GET'])
def resultbyid():
    idcl = request.args['id']
    QUERY2 = ('SELECT idClip,region,longitude,latitude,timestamp,classifyResult FROM `gcp-project-id.jagawana_data.Class` c inner join `gcp-project-id.jagawana_data.Result`r on c.idClass = r.idClass inner join `gcp-project-id.jagawana_data.IotInputdata` ii on ii.idAudioFile=r.idAudioFile inner join `gcp-project-id.jagawana_data.Region` reg on reg.idRegion= ii.idRegion WHERE idClip = "' + idcl +'"')
    query_job = bq_client.query(QUERY2) 
    df = query_job.to_dataframe()
    df['timestamp'] = df['timestamp'].astype(str)
    json_obj = json.dumps(df.to_dict('records'))
    return json_obj

#get link request by audioname with GET http request. input 1 of idClip to use.
#how to use : https://project.appspot.com/getaudio?audioname=59ba3dde-d4a3-4f64-aacc-8f693a1f40a8
#it will be generated audio link to play predicted sound.
@app.route('/getaudio',methods=['GET'])
def getAudio():
    audioname = request.args['audioname']
    return (public_url+audioname)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
