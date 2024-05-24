#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
sys.path.append('/workspaces/Proyecto_MLDS6/scripts')

# Importar la función desde preprocessing/main.py
import preprocessing.main as dtp 

def feature_extraction():
    # Cargar el DataFrame
    # df_sp500 ya contiene los datos necesarios
    df_sp500=dtp.data_prepocessing()

    y = df_sp500["Último"]
    # Seleccionar las características y la variable objetivo
    X_columns = ["Último", "Apertura", "Máximo", "Mínimo"]
    X = df_sp500[X_columns].values

    # Normalizar las características
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    y_scaled = scaler.fit_transform(y.values.reshape(-1, 1))  

    # Crear los rezagos de las características
    lags = 30
    X_lagged = []
    y_lagged = []
    for i in range(lags, len(X_scaled)):
        X_lagged.append(X_scaled[i-lags:i])
        y_lagged.append(y_scaled[i]) 

    X_lagged = np.array(X_lagged)
    y_lagged = np.array(y_lagged)

    # Dividir los datos en conjuntos de entrenamiento, validación y prueba
    train_size = int(0.7 * len(X_lagged))
    val_size = int(0.2 * len(X_lagged))
    test_size = len(X_lagged) - train_size - val_size

    X_train, X_val, X_test = X_lagged[:train_size], X_lagged[train_size:train_size+val_size], X_lagged[-test_size:]
    y_train, y_val, y_test = y_lagged[:train_size], y_lagged[train_size:train_size+val_size], y_lagged[-test_size:]

    return X_train, X_val, X_test, y_train, y_val, y_test, scaler

X_train, X_val, X_test, y_train, y_val, y_test, scaler= feature_extraction()

print("X_train shape: "+str(X_train.shape))
print("X_train shape: "+str(X_val.shape))
print("X_test shape: "+str(X_test.shape))
print("y_train shape: "+str(y_train.shape))
print("y_train shape: "+str(y_val.shape))
print("y_test shape: "+str(y_test.shape))

# Obtener los datos de la columna "Último"
df_sp500=dtp.data_prepocessing()
ultimo_column = df_sp500['Último']

# Crear un arreglo de índices para la serie de tiempo
indices = range(len(ultimo_column))

# Graficar la serie de tiempo
plt.figure(figsize=(10, 6))
plt.plot(indices, ultimo_column, label='Último', color='blue')

# Resaltar los datos de entrenamiento, validación y prueba
train_indices = range(len(y_train))
val_indices = range(len(y_train), len(y_train) + len(y_val))
test_indices = range(len(y_train) + len(y_val), len(y_train) + len(y_val) + len(y_test))

plt.scatter(train_indices, ultimo_column[:len(y_train)], color='green', label='Entrenamiento')
plt.scatter(val_indices, ultimo_column[len(y_train):len(y_train) + len(y_val)], color='orange', label='Validación')
plt.scatter(test_indices, ultimo_column[len(y_train) + len(y_val):len(y_train) + len(y_val) + len(y_test)], color='red', label='Prueba')

# Etiquetas y leyenda
plt.xlabel('Índice')
plt.ylabel('Valor Último')
plt.title('Serie de Tiempo de la Columna "Último" con Conjuntos de Entrenamiento, Validación y Prueba')
plt.legend()

# Guardar la gráfica como imagen PNG
plt.savefig('/workspaces/Proyecto_MLDS6/docs/modeling/serie_de_tiempo.png')

# Mostrar la gráfica (opcional, puedes comentar esto si no quieres que se muestre)
# plt.show()