#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

def data_Adquisition():
    # Descargar el archivo CSV
    url = 'https://drive.google.com/uc?export=view&id=1QvQewt31IAGzqxgutnzyVjcr9E7p5UPC'
    response = requests.get(url)
    if response.status_code == 200:

        content = StringIO(response.text)
        df_sp500 = pd.read_csv(content, on_bad_lines='skip')
        # Convertir la columna 'Fecha' a tipo datetime
        df_sp500['Fecha'] = pd.to_datetime(df_sp500['Fecha'], format='%d.%m.%Y')
        # Limpiar y convertir las columnas 'Último' y 'Apertura' a tipo float
        df_sp500['Último'] = df_sp500['Último'].str.replace('.', '').str.replace(',', '.').astype(float)
        df_sp500['Apertura'] = df_sp500['Apertura'].str.replace('.', '').str.replace(',', '.').astype(float)

        # Guardar el encabezado en un archivo CSV
        df_sp500.head().to_csv('encabezado_datos.csv', index=False)
        
        # Graficar datos
        df_sp500.set_index('Fecha', inplace=True)
        serie_tiempo = df_sp500['Último']
        plt.figure(figsize=(10, 6))
        serie_tiempo.plot(color='blue', linewidth=1)
        plt.title('Serie de Tiempo del Último Precio del S&P 500')
        plt.xlabel('Fecha')
        plt.ylabel('Precio de Cierre')
        plt.grid(True)
        plt.savefig('serie_tiempo_sp500.png')
        plt.close()  # Cerrar la figura después de guardar el gráfico
        return df_sp500
    else:
        print("Error al descargar el archivo.")

# Llamar a la función para ejecutarla
data_Adquisition()
