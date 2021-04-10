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


# Global initialization might be cached
init()  # Initialize LPR


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
    source_blob = source_bucket.get_blob(file["name"])

    # Decode
    image = np.asarray(bytearray(source_blob.download_as_string()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
    # Letterbox
    img = letterbox(image, new_shape=imgsz_detect)[0]
    # Stack
    img = np.stack(img, 0)
    print(img.shape, img.dtype)
    # Convert
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to bsx3x416x416
    img = np.ascontiguousarray(img)
    im0s = image  # source size image

    res = proc(img, im0s, view_img=False)

    with NamedTemporaryFile() as temp:
        temp.write(b"hello")
        temp.write(json.dumps(res))

        temp.flush()

        dest_filename = filename + ".txt"
        dest_bucket_name = "yolov5-output"
        dest_bucket = client.get_bucket(dest_bucket_name)
        dest_blob = dest_bucket.blob(dest_filename)
        dest_blob.upload_from_filename(temp.name)


if __name__ == "__main__":
    run_lpr({"name": "ALE03072.JPG", "bucket": "yolov5-input"}, None)
