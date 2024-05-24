import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay
import tensorflow as tf
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, SimpleRNN
import preprocessing.main
    
def SimpleRNN_model():
    df_sp500 = preprocessing.main()

    # Aplicar one-hot encoding a la variable objetivo SENT
    label_encoder = LabelEncoder()
    y = df_sp500["Último"]

    # Seleccionar las características y la variable objetivo
    X_columns = ["Último", "Apertura", "Máximo", "Mínimo"]
    X = df_sp500[X_columns].values

    # Normalizar las características
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    y_scaled = scaler.fit_transform(y.values.reshape(-1, 1))  # Corrección aquí

    # Crear los rezagos de las características
    lags = 30
    X_lagged = []
    y_lagged = []
    for i in range(lags, len(X_scaled)):
        X_lagged.append(X_scaled[i-lags:i])
        y_lagged.append(y_scaled[i])  # No hace falta cambiar aquí

    X_lagged = np.array(X_lagged)
    y_lagged = np.array(y_lagged)

    # Dividir los datos en conjuntos de entrenamiento, validación y prueba
    train_size = int(0.7 * len(X_lagged))
    val_size = int(0.2 * len(X_lagged))
    test_size = len(X_lagged) - train_size - val_size

    X_train, X_val, X_test = X_lagged[:train_size], X_lagged[train_size:train_size+val_size], X_lagged[-test_size:]
    y_train, y_val, y_test = y_lagged[:train_size], y_lagged[train_size:train_size+val_size], y_lagged[-test_size:]


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

    # Construir el modelo SimpleRNN
    model = Sequential([
        SimpleRNN(250, return_sequences=True, activation='sigmoid', input_shape=(30, 4)),
        SimpleRNN(units=50, activation='sigmoid'),
        Dropout(0.2),
        Dense(units=1, activation='relu')  # 3 neuronas en la capa de salida para clasificación
    ])

    # Compilar el modelo
    model.compile(loss='mse',
                optimizer=tf.optimizers.Adam(learning_rate=1e-3), metrics=['mae'])

    # Ajustar el modelo
    history = model.fit(X_train, y_train,
                        epochs=50, batch_size=32, validation_data=(X_val, y_val),
                        callbacks=[checkpoint, stopping])

    # Evaluar el modelo en el conjunto de prueba
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Accuracy: {accuracy}')

    # Predicciones en el conjunto de prueba
    y_pred = model.predict(X_test)

    # Desnormalizar las predicciones y los valores reales
    y_pred_unscaled = scaler.inverse_transform(y_pred)
    y_test_unscaled = scaler.inverse_transform(y_test)


    # Desnormalizar los datos para calcular las métricas
    y_train_unscaled = scaler.inverse_transform(y_train)
    y_val_unscaled = scaler.inverse_transform(y_val)

    # Predecir sobre los conjuntos de entrenamiento y validación para calcular las métricas
    y_train_pred = model.predict(X_train)
    y_val_pred = model.predict(X_val)

    # Desnormalizar las predicciones
    y_train_pred_unscaled = scaler.inverse_transform(y_train_pred)
    y_val_pred_unscaled = scaler.inverse_transform(y_val_pred)

    # Calcular las métricas
    train_mse = mean_squared_error(y_train_unscaled, y_train_pred_unscaled)
    train_mae = mean_absolute_error(y_train_unscaled, y_train_pred_unscaled)
    val_mse = mean_squared_error(y_val_unscaled, y_val_pred_unscaled)
    val_mae = mean_absolute_error(y_val_unscaled, y_val_pred_unscaled)

    print("Métricas del modelo:")
    print(f"Loss en entrenamiento (MSE): {train_mse}")
    print(f"MAE en entrenamiento: {train_mae}")
    print(f"Loss en validación (MSE): {val_mse}")
    print(f"MAE en validación: {val_mae}")

    # Evaluar el modelo en el conjunto de prueba
    loss, mae = model.evaluate(X_test, y_test)
    print(f'Loss en prueba (MSE): {loss}')
    print(f'MAE en prueba: {mae}')

    return model, loss, mae

# SimpleRNN_model()