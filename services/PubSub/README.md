# Pub/Sub
We create 2 Pubsub Topic. Pub/sub is a GCP service can ingest data and asyncronous-messaging with even-driven system.

<img src="https://user-images.githubusercontent.com/47622164/119776432-20b31300-beef-11eb-99cf-0ed07ab430f4.png">

### Purpose of each topic
#### audio topic 
Topic for communicate device to IoT Core, have 2 subscriptions.

<img src="https://user-images.githubusercontent.com/47622164/119776790-91f2c600-beef-11eb-8f77-42c6e57a272c.png">

* audio-sub : subscribe message from IoT Core.
* gcf-pubsub_trigger : trigger to save audio file at GCS with available formats.

#### do_predic topic
Topic for trigger ML online predictions and return the result to bigquery and GCS. The topic have 2 subscriptions.

<img src="https://user-images.githubusercontent.com/47622164/119777336-3543db00-bef0-11eb-8b00-982005756a39.png">

* do_predict-sub : receive trigger command from do_predic topic.
* gcf-prediction : trigger ML prediction and return the result to bigquery and GCS.

## Next Step
[Next Step is We Configuring Bigquery]().


## References
[Google Cloud Pub/Sub](https://cloud.google.com/pubsub)

[Learn Pub/Sub at Qwiklabs](https://www.qwiklabs.com/focuses/3719?locale=id&parent=catalog)