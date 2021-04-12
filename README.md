# FYP LPR GCP Function

## Cloud Function

Can be deployed directly from this repository, will just work :)

## Compute Engine

```
gcloud init # login to a applicable account
sudo apt install build-essential python3 python3-pip python3-pip python3-dev
# clone the repository
gcloud source repos clone fyp-lpr-gcp-functions --project=fyp-lpr
cd fyp-lpr-gc-functions
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt # if py37
```

