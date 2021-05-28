# App Engine with Flask

## How to Create & Configure the API
This is API for Android Apps.
We Refers you follow this tutorial for the command and how to config it :

https://www.qwiklabs.com/focuses/1014?parent=catalog

## How to Use The API
```
/getallresult 
```
Request using method GET. This API used to return all information about predict result.
Contoh : https://url.appspot.com/getallresult
```
/getresultid?id={parameter} 
```
Request using method GET. This API used to get 1 point data which is indicated as dangerous at the jungle. Input an idClip to use.
Contoh : https://url.appspot.com/getresultid?id=00696dc3-03ac-4c79-9c91-de1bd40819dd
```
/getaudio?audioname={parameter} 
```
Request using the GET method. This API generates a sound download link that is detected as dangerous based on idAudioFile. Input an idAudioFile to use.
Contoh : https://url.appspot.com/getaudio?audioname=59ba3dde-d4a3-4f64-a7cc-8f223a1f40a8
