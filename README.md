# Case Study on MLOps

Let us understand MLOps with the below questions and then we can slowly move to the implementation.

What is MLOps?
- MLOps stands for Machine Learning Operations. MLOps is a core function of Machine Learning engineering, focused on streamlining the process of taking machine learning models to production, and then maintaining and monitoring them.

Why MLOps is required?
- MLOps accounts for the unique aspects of AI/ML projects in project management, CI/CD, and quality assurance, helping us improve delivery time, reduce defects, and make data science more productive. MLOps refers to a methodology that is built on applying DevOps practices to machine learning workloads.

How to implement it?
- It can be implemented using some common tools like
    - MLflow
    - Kubeflow
    - Sklearn
    - GCP
    - AWS
    - Azure

In this case study MLflow tool is utilized to showcase MLOps with three datasets.

What is MLflow and its Components?
MLflow is an open source platform to manage the ML lifecycle, including experimentation, reproducibility, deployment, and a central model registry. MLFlow currently offers four components:
- MLflow Tracking
- MLflow Projects
- MLflow Models
- Model Registry

For all the three datasets, separate implementation using MLflow is done and finally deployed as a microservice using their respective endpoints. The implementation follows the below structure:
-	Data Source
-	Ingestion API
-	Transformers
-	Temporary storage
-	Data pre-processing / Enrichment
-	Feature splitting, Model Training and Validation
-	Experiments (Hyperparameter Tuning)
-	Data Version Control
-	Model Registration and Serving using MLflow
-	Deployment using Fast API as a Microservice
-	Dockerisation
-	Pushing to Git-Hub

Data Source:
Place where the data is stored/generated. It can be on DBs(SQL and No-SQL), Sensors and IOTs, Live data, Kafka Topics, Messaging Queue etc.

Ingestion API:
Data is ingested from data source. In local systems we can use Pandas read command, also using Kafka producer and consumer.

Transformers:
Data merging or data transformation obtained from data source.

Temporary Storage:
Storing it temporarily for later use. 

Data pre-processing / Enrichment:
Pre-process the obtained the data received from the transformers and making it suitable for model building. (Missing value treatment, duplicates, outlier treatment, checking for data imbalance are some pre-processing methods)

Feature splitting, Model Training and Validation:
Splitting the independent and target features, scaling and model building. Finally validating with the trained model.
 
Experiments (Hyperparameter Tuning):
Tuning the base classifier using Grid-search or Randomized search cv and pickling the model for future use.

Data Version Control:
Creating tags for data received. The real time data received will be varying may be on weekly or monthly basis, so it is a good practice to keep tags on the data received, so retraining of model can be easily done. Here DVC is used for data versioning.
Model Registration and Serving using MLflow:
Using MLflow, model, data and parameters can be registered and served. By serving the models and endpoint can be generated which can be used for final prediction.

Deployment using Fast API as a Microservice:
Using Fast API all the endpoints are deployed as microservice. 


Datasets Used:
1. Churn classifier dataset - https://www.kaggle.com/datasets/blastchar/telco-customer-churn
2. Iris classifier dataset - https://www.kaggle.com/datasets/uciml/iris
3. Airline customer satisfaction - https://www.kaggle.com/code/firuzjuraev/airlines-customer-satisfaction-classification/data?select=Invistico_Airline.csv

