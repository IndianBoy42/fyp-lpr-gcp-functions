from PIL import Image
import json
import requests
import cv2

testfilename = "./yolov5/inference/input/ALE03072.JPG"
server = "http://localhost:8000"
with open(testfilename, "rb") as f:
    r = requests.post(
        server + "/lpr",
        files={"file": f},
    )
    print("Response:", r)
    print("Res JSON:", r.json()['results'])