# Jagawana-cloud
[![Country](https://img.shields.io/badge/country-Indonesia-blue.svg)](#)
[![Version](https://img.shields.io/badge/Jagawana-Alpha-brightgreen.svg?maxAge=259200)]()


<img src="https://user-images.githubusercontent.com/47622164/119649272-a5008a00-be4c-11eb-9524-a7c4bd7e89b7.png" width="500">
Jagawana is an integrated system that is able to identify the sounds produced by logging engines (chainsaw, axes, trucks, etc). The system is integrated with sound sensors installed in the forest by applying the concept of the Internet of Things. The sensor is integrated with the cloud system to identify sounds through the Machine Learning model in order to understand the sounds it receives. These voices will be processed in the cloud for further identification, if the sound is the sound of a lumberjack machine, the cloud will transmit the information to the Jagawana Android application in the form of an alarm and the location where logging occurs. The Jagawana application is targeted by its users as forest rangers, namely Polisi Kehutanan or local residents to make it easier for them to monitor and protect the forest and directly to the location of logging in case of illegal logging happening.

## Table Of Contents
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#jagawana-cloud">What Is Jagawana ?</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## Collabolator
### Google Capstone Project from Jagawana Team member
- Bobby Anggunawan (A1721801) - Mobile Programming (Android) - STMIK Mikroskil
- Marsya Yeece Jenniffer (A3092763) - Mobile Programming (Android) - Universitas Sam Ratulangi
- Jeffry Haryanto Gunawan (C2442279) - Cloud Computing - Universitas Kristen Petra
- Rini Aprilianty Riadi (C2142092) - Cloud Computing - Universitas Islam Indonesia
- Harisno (M0080883) - Machine Learning - Universitas Gadjah Mada
 Nico Renaldo (M0080886) - Machine Learning - Universitas Gadjah Mada
### Another Github Path
* [Machine Learning](https://github.com/nicorenaldo/jagawana-ml)
* [Android](https://github.com/Bobby-Anggunawan/Jagawana-AndroidApp)

## Prototype Architecture of Jagawana Cloud Computing
- Cloud Provider using Google Cloud Platform and the Subscription is $200.
<img src="https://user-images.githubusercontent.com/47622164/119015884-8a995d00-b9c3-11eb-8222-de83b5105a73.jpeg" width="250">

## Documentation
All of Documentation is in [here](https://github.com/jeffrywu28/jagawana-cloud/wiki)

## Progress Report Cloud Computing Path:
1. Successfully set permissions for each team member.
2. Sucessfully set budget alerting when it reaches 90 dollars.
3. Successfully connected the IoT device to the cloud.
4. Successfully deploy ML Model that is already running in the cloud.
5. Successfully creating a Pub / Sub where when the data audio is entered, the Pub/ Sub will receive a message, 
   then with Cloud Function the incoming data will be recorded in the BigQuery and Cloud Storage.
6. Successfully in making the output of the model on BigQuery accessible via android using the API from AppEngine

## Contributing
See our contributing guides at ...
