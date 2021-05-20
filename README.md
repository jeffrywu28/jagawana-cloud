# Jagawana-cloud
[![Country](https://img.shields.io/badge/country-Indonesia-blue.svg)](#)
[![Version](https://img.shields.io/badge/Jagawana-Alpha-brightgreen.svg?maxAge=259200)]()

## Member :
This is part of our Google Capstone Project from Jagawana Team Cloud Computing Path.
- Jeffry Gunawan (C2442279)
- Rini Aprilianty (C2142092)

## What Is Jagawana?
An integrated system that is able to identify the sounds produced by logging engines (chainsaw, axes, trucks, etc). The system is integrated with sound sensors installed in the forest by applying the concept of the Internet of Things. The sensor is integrated with the cloud system to identify sounds through the Machine Learning model in order to understand the sounds it receives. These voices will be processed in the cloud for further identification, if the sound is the sound of a lumberjack machine, the cloud will transmit the information to the Jagawana Android application in the form of an alarm and the location where logging occurs. The Jagawana application is targeted by its users as forest rangers, namely Polisi Kehutanan or local residents to make it easier for them to monitor and protect the forest and directly to the location of logging in case of illegal logging happening.

## Prototype Architecture of Jagawana Cloud Computing
- Cloud Provider using Google Cloud Platform and the Subscription is $200.
<img src="https://user-images.githubusercontent.com/47622164/119015884-8a995d00-b9c3-11eb-8222-de83b5105a73.jpeg" width="250">

### Receive Data from IoT
We receive audio data from IoT device (NodeMCU) using GCP IoT Core using MQTT Protocol. 
Pub/Sub is triggered when the audio files ready to store and then Google Cloud Functions will manage file to store audio to GCP Storage Bucket.
#### Pub/Sub
The Topic Name : projects/xenon-anthem-312407/topics/audio

Subscriptions :
  - audio = receive from IoT Core
  - gcf-pubsub_trigger = trigger the cloud functions to manage the GCP Storage Bucket & Google BigQuery.
  
![image](https://user-images.githubusercontent.com/47622164/119029551-f33c0600-b9d2-11eb-97d2-9bd327a075fd.png)

#### Cloud Functions
The main function of Cloud Function is Ingest data like write data name to bigquery, read table from bigquery, write storage to bucket, make wave file, and format filename.

### To be continued
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

## Progress Report Cloud Computing Path:
1. Successfully set permissions for each team member.
2. Sucessfully set budget alerting when it reaches 90 dollars.
3. Successfully connected the IoT device to the cloud.
4. Successfully deploy ML Model that is already running in the cloud.
5. Successfully creating a Pub / Sub where when the data audio is entered, the Pub/ Sub will receive a message, 
   then with Cloud Function the incoming data will be recorded in the BigQuery and Cloud Storage.
6. Successfully in making the output of the model on BigQuery accessible via android using the API from AppEngine
