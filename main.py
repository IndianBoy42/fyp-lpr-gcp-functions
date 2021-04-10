import sys

sys.path.append("yolov5")

import numpy as np
from PIL import Image
import cv2
import requests
from yolov5.azure import proc, init
from yolov5.utils.datasets import letterbox
from google.cloud import storage
from tempfile import NamedTemporaryFile
import json

imgsz_detect = 640
imgsz_recog = 224
device = "cpu"

augment = False
conf_thres_detect = 0.5
iou_thres_detect = 0.3
classes_detect = None
conf_thres_recog = 0.5
iou_thres_recog = 0.5
classes_recog = None
agnostic_nms = False


def run_lpr(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    filename = file["name"]

    client = storage.Client()
    source_bucket = client.get_bucket(file["bucket"])
    source_blob = source_bucket.get_blob(filename)

    with NamedTemporaryFile() as temp:
        print("Hello World", file=temp)

        dest_filename = filename
        dest_bucket_name = "yolov5-output"
        dest_bucket = client.get_bucket(dest_bucket_name)
        dest_blob = dest_bucket.blob(dest_filename)
        dest_blob.upload_from_filename(temp)
