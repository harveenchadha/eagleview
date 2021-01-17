import pandas as pd
from tqdm import tqdm
import os

X_test = pd.read_csv('data/test.csv')

X_test_paths = X_test.file_path.unique()


for image in tqdm(X_test_paths):
    cmd= 'python eagleview/scripts/efficientdet/model_inspect.py \
--runmode=saved_model_infer \
--model_name=efficientdet-d2 \
--saved_model_dir=eagleview/checkpoints/exported_model \
--hparams=eagleview/config/config.yaml \
--input_image='+image+' \
--output_image_dir=eagleview/results'
    filename = image.split('/')[-1]
    cmd_2 = 'mv eagleview/results/0.jpg eagleview/results/'+filename
    

    os.system(cmd)
    os.system(cmd_2)
