# For model reg
# mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 0.0.0.0 --port 5004 
import numpy as np
import pandas as pd
import warnings 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
from sklearn.metrics import average_precision_score, confusion_matrix, accuracy_score, classification_report, plot_confusion_matrix
import mlflow
import mlflow.sklearn
from mlflow import log_metric, log_param, log_artifacts
import pickle

# Get url from DVC
import dvc.api

path = 'data/Iris.csv'
repo = '/Volumes/GL/TECH/IIITH/TA_Session_Material/DVC_Handson'
version = 'v2' 

data_url = dvc.api.get_url(path=path,
                           repo=repo,
                           rev=version)
mlflow.set_experiment(experiment_name='Iris-DVC')

def get_metrics(y_true, y_pred, y_pred_prob):
    from sklearn.metrics import accuracy_score,precision_score,recall_score,log_loss
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred,average='micro')
    recall = recall_score(y_true, y_pred,average='micro')
    entropy = log_loss(y_true, y_pred_prob)
    return {'accuracy': round(acc, 2), 'precision': round(prec, 2), 'recall': round(recall, 2), 'entropy': round(entropy, 2)}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    print('Starting the experiment')
    mlflow.set_tracking_uri("http://127.0.0.1:5004")
    mlflow.set_experiment(experiment_name='Iris-DVC')

    mlflow.autolog()  ##record automatically

    df = pd.read_csv(data_url)

    # log data params
    mlflow.log_param('data_version',version)
    mlflow.log_param('data_url',data_url)
    mlflow.log_param('input_rows', df.shape[0])
    mlflow.log_param('input_cols', df.shape[1])

    # Data Preparation for model building
    y = df.iloc[:,5] 
    X = df.iloc[:,0:5] 

    # Splitting the data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y , test_size = 0.2, random_state =42, stratify=y)

    # Scaling the data
    sc = StandardScaler()
    X_train_sc = sc.fit_transform(X_train)
    X_test_sc = sc.transform(X_test)


    # Basic classifer 
    classifier = LogisticRegression()
    classifier.fit(X_train,y_train)
    Tr_acc = classifier.score(X_train_sc, y_train)

    # Saving test and target data for future use
    test_data = pd.DataFrame(X_test_sc)
    test_data.to_csv('data/Test_data.csv', index='False')
    target_data = pd.DataFrame(y)
    target_data.to_csv('data/Target_data.csv', index='False')

    mlflow.log_artifact('Test_data.csv')
    mlflow.log_artifact('Target_data.csv') 
     
    # save the model to disk
    pickle.dump(classifier, open('models/LRClassifier.pkl', 'wb'))

    y_pred = classifier.predict(X_test_sc)
    y_pred_prob = classifier.predict_proba(X_test_sc)

    run_metrics = get_metrics(y_test, y_pred, y_pred_prob)
    
    # Log the metrics for training and testing

    mlflow.log_metric("Accuracy for Training", Tr_acc)
    for metric in run_metrics:
        mlflow.log_metric(metric, run_metrics[metric])

    mlflow.set_tag("tag1", "Basic_Classifier")
    mlflow.set_tags({"tag2":"Iris_dvc", "tag3":"Production"})
    mlflow.sklearn.log_model(classifier, "model",registered_model_name="Iris-dvc")
    