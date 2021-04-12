#!/usr/bin/env bash
import sys
sys.path.append("yolov5")

from flask import Flask, request, Response
import json
import cv2
from cv2 import IMREAD_UNCHANGED
import numpy as np
from yolov5.helpers import *
from yolov5.utils.datasets import letterbox

init()  # Initialize LPR
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/lpr', methods=['POST'])
def lpr():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        nparr = np.fromstring(uploaded_file.read(), np.uint8)
        image = cv2.imdecode(nparr, IMREAD_UNCHANGED)
        # Letterbox
        img = letterbox(image, new_shape=imgsz_detect)[0]
        # Stack
        img = np.stack(img, 0)
        # Convert
        img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to bsx3x416x416
        img = np.ascontiguousarray(img)
        im0s = [image]  # source size image

        res = proc(img, im0s, view_img=False)

        response = {"results": res}
        return Response(response = json.dumps(response), status=200, mimetype="application/json")
    else:
        return Response(response = "no image uploaded", status=403)

app.run(host="0.0.0.0", port=8000)