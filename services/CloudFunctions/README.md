# GCP Cloud Functions

We are using Cloud Functions to automate data saving from Pub/Sub to Storage and BigQuery, as well as making predictions from our model deployed at AI Platform.

## Deploying Cloud Functions

Make sure you have [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed to deploy from your machine, or you could upload it manually from GCP Console.

Go into the download folder through your terminal, from inside the functions folder type the following code to deploy the whole folder.

```
gcloud functions deploy pubsub_trigger --region asia-southeast2 --runtime python37 --trigger-topic audio
```
The code above will create a new cloud functions with the name pubsub_trigger, you can change the region to your liking and the topic existed in your system.

You can change the cloud functions name to your liking, make sure to include the functions name inside the `main.py` file as it would be called as the trigger.