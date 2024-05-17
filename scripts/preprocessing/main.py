#!/usr/bin/env python3
import sys
import pandas as pd
sys.path.append('/workspaces/Proyecto_MLDS6/scripts')

# Importar la función desde data_acquisition/main.py
import data_acquisition.main as dta

def data_prepocessing():
    df_sp500=dta.data_Adquisition()
    # Convertir la columna 'Fecha' a tipo datetime
    df_sp500['Fecha'] = pd.to_datetime(df_sp500['Fecha'], format='%d.%m.%Y')
    # Limpiar y convertir las columnas 'Último' eliminando puntos y comas y convirtiendola a tipo float
    df_sp500['Último']=df_sp500['Último'].str.replace('.', '').str.replace(',', '.').astype(float)
    # Limpiar y convertir las columnas 'Apertura' eliminando puntos y comas y convirtiendola a tipo float
    df_sp500['Apertura']=df_sp500['Apertura'].str.replace('.', '').str.replace(',', '.').astype(float)
    # Limpiar y convertir las columnas 'Máximo' eliminando puntos y comas y convirtiendola a tipo float
    df_sp500['Máximo']=df_sp500['Máximo'].str.replace('.', '').str.replace(',', '.').astype(float)
    # Limpiar y convertir las columnas 'Mínimo' eliminando puntos y comas y convirtiendola a tipo float
    df_sp500['Mínimo']=df_sp500['Mínimo'].str.replace('.', '').str.replace(',', '.').astype(float)
    # Limpiar y convertir las columnas '% var.' eliminando puntos, comas, porcentajes y convirtiendola a tipo float
    df_sp500['% var.']=df_sp500['% var.'].str.replace('%', '').str.replace(',', '.').astype(float)
    # Eliminar la columna "Vol." ya que todos sus valores son vacios
    df_sp500=df_sp500.drop(columns=["Vol."])
    #Se agrega la columna de SEN  como etiquetas de varabiable categorica para ver describir comportamientos positivos negativos o neutros del mercado
    df_sp500['SENT']=['Positivo' if var>=0.17 else 'Negativo' if var<=-0.17 else 'Neutro' for var in df_sp500['% var.'] ]
    print(df_sp500)
    return df_sp500

data_prepocessing()