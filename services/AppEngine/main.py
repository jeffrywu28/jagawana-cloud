from flask import Flask,request
from google.cloud import bigquery
import json

app = Flask(__name__)

#var
gcp_project = {YOUR GCP PROJECT ID} #please change with your gcp project id
public_url = {YOUR PUBLIC URL BUCKET STORAGE} #please change with your gcp storage bucket
bq_client = bigquery.Client(project=gcp_project)

#default home page
@app.route('/')
def hello_world():
    return 'Hello, World!'

#getresult
@app.route('/getallresult',methods=['GET'])
def hello():
    """Return a friendly HTTP greeting."""
    QUERY = ('SELECT idClip, r.idAudioFile, startInterval, endInterval, idDevice,region,longitude,latitude,timestamp,classifyResult,CONCAT("https://storage.googleapis.com/input-audio-pipeline/Wave%20Storage/",r.idAudioFile) AS newfield FROM `gcp-project-id.jagawana_data.Result` r inner join `gcp-project-id.jagawana_data.IotInputdata` i on r.idAudioFile = i.idAudioFile inner join `gcp-project-id.jagawana_data.Class` c on r.idClass=c.idClass inner join `gcp-project-id.jagawana_data.Region` reg on i.idRegion= reg.idRegion')
    query_job = bq_client.query(QUERY)  # API request
    df = query_job.to_dataframe() #parse query result to JSON
    df['timestamp'] = df['timestamp'].astype(str)
    json_obj = json.dumps(df.to_dict('records'))
    return json_obj

#getresult by id
@app.route('/getresultid',methods=['GET'])
def resultbyid():
    idcl = request.args['id']
    QUERY2 = ('SELECT idClip,region,longitude,latitude,timestamp,classifyResult FROM `gcp-project-id.jagawana_data.Class` c inner join `gcp-project-id.jagawana_data.Result`r on c.idClass = r.idClass inner join `gcp-project-id.jagawana_data.IotInputdata` ii on ii.idAudioFile=r.idAudioFile inner join `gcp-project-id.jagawana_data.Region` reg on reg.idRegion= ii.idRegion WHERE idClip = "' + idcl +'"')
    query_job = bq_client.query(QUERY2)  # API request
    df = query_job.to_dataframe()
    df['timestamp'] = df['timestamp'].astype(str)
    json_obj = json.dumps(df.to_dict('records'))
    return json_obj

#get link request by audioname
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
