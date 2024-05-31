import os

import joblib
import ngrok
import mlflow
import subprocess

from SimpleRNN_model import SimpleRNN_model

def deployment():
    # MLflow
    command = """
    mlflow server \
            --backend-store-uri sqlite:///tracking.db \
            --default-artifact-root file:mlruns \
            -p 5000 &
    """
    subprocess.run(command, shell=True, check=True)


    # Supongamos que NGROK_TOKEN está almacenado en una variable de entorno
    ngrok_token = os.getenv('NGROK_TOKEN')

    # Construir el comando
    command = f"ngrok authtoken {ngrok_token}"

    # Ejecutar el comando
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    ngrok.connect(5000, "http")

    mlflow.set_tracking_uri("http://localhost:5000")
    exp_id = mlflow.create_experiment(name="sp_500_modeling", artifact_location="mlruns/")

    # RNN model
    with mlflow.start_run(
        run_name="rnn",
        experiment_id=exp_id
        ):
        model, MSE_RNN, MAE_RNN = SimpleRNN_model()

        mlflow.sklearn.log_model(model, "model_lstm")
        mlflow.log_metric("MSE", MSE_RNN)
        mlflow.log_metric("MAE", MAE_RNN)
        mlflow.end_run()

    # Save model and verified model can be loaded
    joblib.dump(model,'./mlruns')
    model_test = joblib.load('model.joblib')

    