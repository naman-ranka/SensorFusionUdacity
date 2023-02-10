import argparse
import time
import cv2

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from matplotlib import animation

from object_detection.builders.dataset_builder import build as build_dataset
from object_detection.utils.config_util import get_configs_from_pipeline_file
from object_detection.utils.label_map_util import create_category_index_from_labelmap
from object_detection.utils import visualization_utils as viz_utils

#from utils import get_module_logger


## *IMPORTANT*
## CHANGE THE PAREMETERS BELOW
## labelmap_path = "PATH TO LABEL_MAP.PBTXT"
## model_path = "PATH TO TRAINED AND EXPOTED OBJECT DETECTION MODEL"
## config_path = "PATH TO PIPELINE FILE"

labelmap_path = "label_map.pbtxt"
model_path = "home/experiments/try4/exported/saved_model"
config_path = "home/experiments/try4/pipeline_new.config"

category_index = create_category_index_from_labelmap(labelmap_path,use_display_name=True)

detect_fn = tf.saved_model.load(model_path)


def create_model():
    configs = get_configs_from_pipeline_file(config_path)
    # eval_config = configs['eval_config']
    # eval_input_config = configs['eval_input_config']
    model_config = configs['model']
    detect_fn = tf.saved_model.load(model_path)
    return detect_fn

def detect(detect_fn,image):
    
    image_np = np.array(image)
    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.uint8)
        
    detections = detect_fn(input_tensor)

    # tensor -> numpy arr, remove one dimensions
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, ...].numpy()
                    for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(
        np.int64)

    image_np_with_detections = image_np.copy()
    viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np_with_detections,
        detections['detection_boxes'],
        detections['detection_classes'],
        detections['detection_scores'],
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=.80,
        agnostic_mode=False)
    
    # cv2.imshow("result", image_np_with_detections)
    # cv2.waitKey(100)

    return detections

