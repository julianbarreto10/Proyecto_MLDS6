import mlflow
import os
import pandas as pd
from pyngrok import ngrok
from GRU_model import GRU_model
from LSTM_model import LSTM_model
from SimpleRNN_model import SimpleRNN_model



def main():
    ngrok.connect(5000, "http")
    mlflow.set_tracking_uri("http://localhost:5000")
    exp_id = mlflow.create_experiment(name="project_models1", artifact_location="mlruns/")
    # LSTM model
    with mlflow.start_run(
        run_name="lstm",
        experiment_id=exp_id
        ):
        model, MSE_LSTM, MAE_LSTM = LSTM_model()

        mlflow.sklearn.log_model(model, "model_lstm")
        mlflow.log_metric("MSE", MSE_LSTM)
        mlflow.log_metric("MAE", MAE_LSTM)
        mlflow.end_run()


    # GRU model
    with mlflow.start_run(
        run_name="gru",
        experiment_id=exp_id
        ):
        model, MSE_GRU, MAE_GRU = GRU_model()

        mlflow.sklearn.log_model(model, "model_lstm")
        mlflow.log_metric("MSE", MSE_GRU)
        mlflow.log_metric("MAE", MAE_GRU)
        mlflow.end_run()

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



main()