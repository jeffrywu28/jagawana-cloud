# App Engine with Flask

## How to Create & Configure the API
This is API for Android Apps. We use python version 3.8 and python framework Flask
We Refers you follow this tutorial for the command and how to config it :

https://www.qwiklabs.com/focuses/1014?parent=catalog

Or use this simple tutorial :
1. Open [GCP Console](https://console.cloud.google.com/) then at the left > APIs & Services > Library. <br><img src="https://user-images.githubusercontent.com/47622164/121245959-ce98c700-c8ca-11eb-8805-f129e5191e25.png" width="350">
2. Try enable Python Virtual Environtment and install the requirement
```
virtualenv -p python3 env
```
3. Then activate with this command
```
source env/bin/activate
```
4. Copy and paste my requirement to your requirement.txt
```
pip install -r requirements.txt
```
5. I try to download the Hello World example (use it in GCP Console)
```
gsutil -m cp -r gs://spls/gsp067/python-docs-samples .
```
6. Then go to the folder
```
cd python-docs-samples/appengine/standard_python3/hello_world
```
7. Edit your code at
```
nano main.py
```
8. Test your flask with this command
```
python main.py
```
9. Then click like example below for checking <br>
![image](https://user-images.githubusercontent.com/47622164/121248557-c3936600-c8cd-11eb-9d0b-cd18d2b88800.png)

10. After all checked, Deploy your App
```
gcloud app deploy
```
11. Yes and choose your favorite region. Then show your deployed link. Click and test it.
```
gcloud app browse
```
<br>

## How to Use The API
```
/getallresult 
```
Request using method GET. This API used to return all information about predict result.<br>
Example : https://url.appspot.com/getallresult
```
/getresultid?id={parameter} 
```
Request using method GET. This API used to get 1 point data which is indicated as dangerous at the jungle. Input an idClip to use.<br>
Example : https://url.appspot.com/getresultid?id=00696dc3-03ac-4c79-9c91-de1bd40819dd
```
/getaudio?audioname={parameter} 
```
Request using the GET method. This API generates a sound download link that is detected as dangerous based on idAudioFile. Input an idAudioFile to use.<br>
Example : https://url.appspot.com/getaudio?audioname=59ba3dde-d4a3-4f64-a7cc-8f223a1f40a8

```
/getalldevices
```
Request using the GET method. This API generates all connected device to Jagawana Cloud.<br>
Example: https://url.appspot.com/getalldevices
