import pandas as pd
from tqdm import tqdm
import os
import argparse
import matplotlib.pyplot as plt
import cv2


def start_infer(image_path):

    cmd= 'python efficientdet/model_inspect.py \
    --runmode=saved_model_infer \
    --model_name=efficientdet-d2 \
    --saved_model_dir=../checkpoints/exported_model \
    --hparams=../config/config.yaml \
    --input_image='+image_path+' \
    --output_image_dir=/tmp'
    
    os.system(cmd)
    det_image = cv2.cvtColor(cv2.imread('/tmp/0.jpg'), cv2.COLOR_BGR2RGB) 

    plt.imshow(det_image)
    plt.show()




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Infer on single image')
    parser.add_argument('-i', '--image', required=True, help='Image Path')

    args_local = parser.parse_args()

    start_infer(args_local.image)