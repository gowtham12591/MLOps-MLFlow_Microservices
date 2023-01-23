### MLFlow model serving

# Run this from command line
# -  use `set MLFLOW_TRACKING_URI=http://localhost:5004` for windows
# - use `export MLFLOW_TRACKING_URI=http://localhost:5004` if in linux/mac

## **Now run this command from command line**

# make sure we use to write the different port - other than the one you used while starting mlflow server

# `mlflow models serve --model-uri models:/Iris-dvc/Production -p 6004 --env-manager=local`

# Predicting the results using endpiont created by serving the model

import requests
import pandas as pd

X_test = pd.read_csv('data/Test_data.csv')
lst = X_test.values.tolist()
inference_request = {
        "data": lst
}
endpoint = "http://localhost:6004/invocations"
response = requests.post(endpoint, json=inference_request)
print(response)
print(response.text)