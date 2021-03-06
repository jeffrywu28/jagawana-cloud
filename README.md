# Jagawana - Cloud Computing Configurations
[![Country](https://img.shields.io/badge/country-Indonesia-blue.svg)](#)
[![Version](https://img.shields.io/badge/Jagawana-Alpha-brightgreen.svg?maxAge=259200)]()

## What is Jagawana?
<img src="https://user-images.githubusercontent.com/47622164/119649272-a5008a00-be4c-11eb-9524-a7c4bd7e89b7.png" width="500">
Jagawana is an integrated system that is able to identify the sounds produced by logging engines (chainsaw, axes, trucks, etc). The system is integrated with sound sensors installed in the forest by applying the concept of the Internet of Things. The sensor is integrated with the cloud system to identify sounds through the Machine Learning model in order to understand the sounds it receives. These voices will be processed in the cloud for further identification, if the sound is the sound of a lumberjack machine, the cloud will transmit the information to the Jagawana Android application in the form of an alarm and the location where logging occurs. The Jagawana application is targeted by its users as forest rangers, namely Polisi Kehutanan or local residents to make it easier for them to monitor and protect the forest and directly to the location of logging in case of illegal logging happening.

## Table Of Contents
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#jagawana---cloud-computing-configurations">What Is Jagawana ?</a>
    </li>
    <li>
      <a href="https://github.com/jeffrywu28/jagawana-cloud/blob/main/services/GETTINGSTARTED.md">Getting Started</a>
    </li>
    <li><a href="https://github.com/jeffrywu28/jagawana-cloud/blob/main/CONTRIBUTING.md">Contributing</a></li>
    <li><a href="https://github.com/jeffrywu28">Contact</a></li>
  </ol>
</details>

## Collabolator
### Google Bangkit 2021 Capstone Project from Jagawana Team member [ B21-CAP0218 ]
- Bobby Anggunawan (A1721801) - Mobile Programming (Android) - STMIK Mikroskil
- Marsya Yeece Jenniffer (A3092763) - Mobile Programming (Android) - Universitas Sam Ratulangi
- Jeffry Haryanto Gunawan (C2442279) - Cloud Computing - Universitas Kristen Petra
- Rini Aprilianty Riadi (C2142092) - Cloud Computing - Universitas Islam Indonesia
- Harisno (M0080883) - Machine Learning - Universitas Gadjah Mada
- Nico Renaldo (M0080886) - Machine Learning - Universitas Gadjah Mada

### Another Jagawana Github Path
* [Internet of Things](https://github.com/nicorenaldo/jagawana-iot)
* [Machine Learning](https://github.com/nicorenaldo/jagawana-ml)
* [Mobile Apps Android](https://github.com/Bobby-Anggunawan/Jagawana-AndroidApp)

## Prototype Architecture of Jagawana Cloud Computing
Cloud Provider using Google Cloud Platform and the Subscription is $200 for 2 month.

<img src="https://user-images.githubusercontent.com/47622164/119015884-8a995d00-b9c3-11eb-8222-de83b5105a73.jpeg" width="250">

#### GCP Service :
1. Google Cloud IoT Core
2. Google Cloud Pub/Sub
3. Google Cloud Functions
4. Google AI Platform
5. Google Cloud Storage
6. Google BigQuery
7. Google App Engine

## Getting Started
All of Documentations to getting started is in [here](https://github.com/jeffrywu28/jagawana-cloud/blob/main/services/GETTINGSTARTED.md).

## Progress Report Cloud Computing Path:
1. Successfully set permissions for each team member.
2. Sucessfully set budget alerting when it reaches 90 dollars.
3. Successfully connected the IoT device to the cloud.
4. Successfully deploy ML Model that is already running in the cloud.
5. Successfully creating a Pub / Sub where when the data audio is entered, the Pub/ Sub will receive a message,then with Cloud Function the incoming data will be recorded in the BigQuery and Cloud Storage.
6. Successfully connect to android platform using the API from AppEngine.


## Contributing
See our contributing guides at [here](https://github.com/jeffrywu28/jagawana-cloud/contributing.md).
