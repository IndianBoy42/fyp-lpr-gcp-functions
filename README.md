# FYP LPR GCP Function

## Compute Engine

Access to a configurable Virtual Machine

More powerful if you can pay for it.

Easier to deploy a single instance as you have SSH access

Setup
```
# install dependencies
sudo apt install build-essential python3 python3-pip python3-pip python3-dev
cd fyp-lpr-gc-functions
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt # if py37
```

If you have python 3.8 installed use:
```
pip install -r requirements38.txt # if py37
```

## Cloud Function

Serverless, weak CPU but automatically scalable, 

under continuous load the setup stage should be cached

Can be deployed directly from this repository, will just work :)

Sending images into Google Cloud Functions is overcomplicated, not designed for this...

### How to get this repository from GCloud
```
gcloud init # login to a applicable account
# clone this repository
gcloud source repos clone fyp-lpr-gcp-functions --project=fyp-lpr
```
