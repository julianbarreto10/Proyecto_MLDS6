#!/usr/bin/env python3
import sys
import os
import pandas as pd
import numpy as np
import mlflow
from pyngrok import ngrok
import subprocess
from IPython.display import display
from pyngrok import ngrok
import tensorflow as tf
from scikeras.wrappers import KerasRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import  Dense, Dropout, SimpleRNN
sys.path.append('/workspaces/Proyecto_MLDS6/scripts')

# Importar la función desde data_acquisition/main.py
import eda.main as edc 

X_train, X_val, X_test, y_train, y_val, y_test, scaler= edc.feature_extraction()


checkpoint = tf.keras.callbacks.ModelCheckpoint(
                  filepath='best_weights_SRNN.weights.h5',
                  monitor="val_mae",
                  verbose=1,
                  save_best_only=True,
                  save_weights_only=True,
                  mode="min",
            )
stopping = tf.keras.callbacks.EarlyStopping(
                monitor="val_mae",
                patience=10,
                verbose=1,
                mode="min",
                restore_best_weights=True,
            )


# Función para crear el modelo


def create_model(activation='relu', lstm_units=250, dropout_rate=0.2, optimizer='adam'):
    model = Sequential([
        SimpleRNN(units=lstm_units, return_sequences=True, activation=activation, input_shape=(30, 4)),
        SimpleRNN(units=int(lstm_units/5), activation=activation),
        Dropout(dropout_rate),
        Dense(units=1, activation='relu')
    ])
    model.compile(loss='mse', optimizer=optimizer, metrics=['mae'])
    return model

# Crear un modelo KerasRegressor para usar en GridSearchCV
model = KerasRegressor(build_fn=create_model, verbose=0,activation='relu',lstm_units=100)

# Definir los hiperparámetros a ajustar
param_grid = {
    'lstm_units': [100, 150, 200]
}

# Realizar la búsqueda de cuadrícula
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, scoring='neg_mean_squared_error', verbose=2)
grid_result = grid_search.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_val, y_val), callbacks=[stopping])

# Mostrar los mejores resultados
print("Mejor MSE: %f usando %s" % (grid_result.best_score_, grid_result.best_params_))

# Evaluar el mejor modelo en el conjunto de prueba
best_model = grid_result.best_estimator_
y_pred = best_model.predict(X_test)
y_pred_unscaled = scaler.inverse_transform(y_pred)
y_test_unscaled = scaler.inverse_transform(y_test)
mse = mean_squared_error(y_test_unscaled, y_pred_unscaled)
mae = mean_absolute_error(y_test_unscaled, y_pred_unscaled)
print(f'MSE en prueba del mejor modelo: {mse}')
print(f'MAE en prueba del mejor modelo: {mae}')

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
exp_id = mlflow.create_experiment(name="sp_500_modeing", artifact_location="mlruns/")

with mlflow.start_run(
        run_name="grid_search_model",
        experiment_id=exp_id
        ):
    model = best_model
    mlflow.log_metric("MSE", mse)
    mlflow.log_metric("MSE", mae)
    mlflow.grid_search_model.log_model(model, "model")