# eagleview

# Intution

Since the problem was just to detect person and car, I wanted to use a method that is SOTA at the moment. I could have done it with YOLOv3 but wanted to do something new. So the intution is that I would freeze the entire network and just retrain the last two layers by changing the classes as person & car are already present in imagenet. I did had the intention of clustering annotation boxes to find anchor boxes for accurate object detection (check EDA notebook) but finally decided not to use it. I ended up using EfficientDet-D2 as the final arch.

# Code Base

All code is picked from google's automl repository for [efficientdet](https://github.com/google/automl/tree/master/efficientdet)

# Folder structure explanation

config: contains the config

| Folder | Purpoe              |
|------------------|-------------------|
| config | contains the config for finetuning efficient det model for two classes                |
| data  | contains the train, valid, test splits. TF records were also generated but can't be pushed to git due to size limitation               |
| logs  | contains the training logs for efficient det model |
| notebooks  | contains the notebook for EDA, TF record generation and clustering of anchor boxes |
| results  | contains the output of efficientdet finetuned model on the test set |
| scripts | contains the efficient det scripts plus custom scripts for inference |
| checkpoints | contains the checkpoints used for finetuning and frozen model |
| checkpoints/exported_model | frozen graph of final finetuned model |
| checkpoints/pretrained | contains the pretrained checkpoint from google |
| checkpoints/finetuning | all the finetuned checkpoints are stored here |
| data/processed | contains tf records for train, test and valid |
| data/raw | contains original data |




# Training Information: Loss Function and Metrics

Epochs completed : 10 [Due to limited GPU availability]

Hardware: Single GPU, Google Colab

Loss Function: Focal Loss

Metrics: AP

# Misc

Use setup.ipynb file in the colab to replicate results.

To check the result of detection, check the results folder. These images were not used for training and were part of the test set.

In case you need to infer on a custom image. Scripts > infer_single_image.py

# Download entire code

Including TF-records, checkpoints, exported model

[Here](!www.kaggle.com/harveenchadha/efficientdet-custom)


