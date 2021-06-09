# Welcome to the Jagawana Cloud land!
The quickest way to getting started with the Jagawana-Cloud path. You can get [free-trial](https://cloud.google.com/free/docs/gcp-free-tier) 90-day with $300 GCP product credits or  buy some credit at [GCP](https://cloud.google.com/gcp) (**this amount just for SIMULATION ONLY** and only lasted 1 month).

## The role of cloud computing in this capstone project

- Cloud Computing act as station from IoT device, manage data using Machine Learning and data distributor which mean send API to Android.
- First is Cloud IoT core, used to monitoring iot device.
- Pub/sub, used to trigger the cloud function as a messenger between services.
- Cloud functions, used to trigger Cloud Storage (GCS) to receive sound and predict the ML using Ai platform.
- Then Ai platform, used to training model and predict result.
- Big query to save all information data and GCS to save model, record, container files and many more.
- We use app engine built with python Flask, used to deliver API to mobile apps.
- All code we use python programming languages.

## Getting Started

### Requirements
* Google Account.
* Credit or Debit card to buy GCP credits.
* IoT device (Rasp,etc.).

You can claim your free-trial $300 tutorial [here](https://k21academy.com/google-cloud/create-google-cloud-free-tier-account/). <br>
If you have an GCP coupon, you can redeem at [here](https://console.cloud.google.com/trygcp)

### Quickstart
1. Add your teammates to join your GCP at this [tutorial](https://www.youtube.com/watch?v=PqMGmRhKsnM) 
2. Set the payment billing alert (if you want) at [here](https://www.youtube.com/watch?v=F4omjjMZ54k) and you can learn how to optimize your billing [here](https://www.youtube.com/playlist?list=PLIivdWyY5sqKJx6FwJMRcsnFIkkNFtsX9).
3. Set your connection within Google IoT Core with Raspi. You can learn the guide [here](https://www.youtube.com/watch?v=3Zwlj9x96Jg) and the official documentation is [here](https://cloud.google.com/iot/docs/quickstart).
4. Prepare The Google Cloud Storage folder,permission, you can watch our tutorial at [here](https://www.youtube.com/watch?v=PoVbGE0HrRA)
5. Create Bigquery dataset and table schema. the tutorial [here](https://github.com/jeffrywu28/jagawana-cloud/tree/main/services/BigQuery)
6. Create Pub/Sub connection between IoT Core and Cloud Function, Storage Group and Cloud Function, AI Platform and Cloud Function. at [here](https://github.com/jeffrywu28/jagawana-cloud/tree/main/services/PubSub)
7. For tutorial how to deploy ML to GCP, view [here](https://github.com/nicorenaldo/jagawana-ml#deploying-model-to-gcp)
8. Create cloud Function for trigger the Google Cloud Storage and AI Platform [here](https://github.com/jeffrywu28/jagawana-cloud/tree/main/services/CloudFunctions)
