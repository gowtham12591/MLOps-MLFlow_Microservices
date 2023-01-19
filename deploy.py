# Create a virtual environment
# python -m venv mlflow
# Activate the virtual environment using
# source mlflow/bin/activate

# Requirements - 
# pip install fastapi, requests, uvicorn, joblib

from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
import pickle
import joblib
import numpy as np
import pandas as pd
from io import StringIO
import requests

app = FastAPI()

# Main page url
@app.get('/')
async def root():
    return{'message':'MLFlow Model Deployment'}

# Use /docs# to navigate to this page
@app.post('/files_churn/')
#async def create_file(file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...))
async def batch_prediction(file: bytes = File(...)):
    s = str(file, 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)
    lst = df.values.tolist()
    inference_request = {"data": lst}
    endpoint = "http://localhost:6000/invocations"
    response = requests.post(endpoint, json=inference_request)
    print(response.text)

    return response.text

# Use /docs# to navigate to this page
@app.post('/files_iris/')
#async def create_file(file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...))
async def iris_batch_prediction(file: bytes = File(...)):
    s = str(file, 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)
    lst = df.values.tolist()
    inference_request = {"data": lst}
    endpoint = "http://localhost:6001/invocations"
    response = requests.post(endpoint, json=inference_request)
    print(response.text)

    return response.text


# Use /docs# to navigate to this page
@app.post('/files_flight/')
#async def create_file(file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...))
async def batch_prediction(file: bytes = File(...)):
    s = str(file, 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)
    lst = df.values.tolist()
    inference_request = {"data": lst}
    endpoint = "http://localhost:6002/invocations"
    response = requests.post(endpoint, json=inference_request)
    print(response.text)

    return response.text

# Use /docs# to navigate to this page
@app.post('/files_iris_dvc/')
#async def create_file(file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...))
async def iris_batch_prediction(file: bytes = File(...)):
    s = str(file, 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)
    lst = df.values.tolist()
    inference_request = {"data": lst}
    endpoint = "http://localhost:6004/invocations"
    response = requests.post(endpoint, json=inference_request)
    print(response.text)

    return response.text

# To run this file use the command
# python -m uvicorn deploy:app --reload
# To check the FaskAPI page go the url and then type /docs#



