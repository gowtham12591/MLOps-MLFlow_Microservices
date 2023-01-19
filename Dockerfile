# Base image
FROM python:3.7.11

# Set working directory
WORKDIR /app

# Copy files
COPY Churn_classifier /app/
COPY Iris_classifier /app/
COPY Iris_dvc /app/
COPY Flight_satisfaction /app/
COPY requirements.txt /app/ 
COPY test /app/
COPY deploy.py /app/

# Install dependencies
RUN pip install -r requirements.txt
#RUN python3 deploy.py

# Run the application
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "--timeout", "120"]
CMD ["app:app"]