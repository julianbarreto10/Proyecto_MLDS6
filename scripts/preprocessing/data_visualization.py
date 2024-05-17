#!/usr/bin/env python3
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import matplotlib.pyplot as plt
import wget

import main

def data_visualization():
    df_sp500 = main.data_preprocessing()

    df_sp500.groupby('SENT').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
    plt.gca().spines[['top', 'right',]].set_visible(False)

    # Codigo para grafico 2
    figsize = (12, 1.2 * len(df_sp500['SENT'].unique()))
    plt.figure(figsize=figsize)
    sns.violinplot(df_sp500, x='% var.', y='SENT', inner='box', palette='Dark2')
    sns.despine(top=True, right=True, bottom=True, left=True)

    # Codigo para grafico 3
    # Asegúrate de tener 'df_sp500' correctamente cargado y procesado
    df_sp500['Fecha'] = pd.to_datetime(df_sp500['Fecha'], format='%d.%m.%Y')
    df_sp500['Último']=df_sp500['Último'].str.replace('.', '').str.replace(',', '.').astype(float)
    df_sp500['Apertura']=df_sp500['Apertura'].str.replace('.', '').str.replace(',', '.').astype(float)

    # Crear el gráfico interactivo 1
    fig = make_subplots(rows=1, cols=1, shared_xaxes=True, shared_yaxes=True,
                        subplot_titles=("Comportamiento a lo largo del tiempo"))

    # Agregar las líneas correspondientes a cada variable
    fig.add_trace(go.Scatter(x=df_sp500['Fecha'], y=df_sp500['Último'], mode='lines', name='Último'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_sp500['Fecha'], y=df_sp500['Apertura'], mode='lines', name='Apertura'), row=1, col=1)

    # Actualizar el diseño del gráfico
    fig.update_layout(title_text="Comportamiento a lo largo del tiempo",
                    xaxis_title="Fecha",
                    yaxis_title="Valor",
                    showlegend=True)

    # Agregar botones de selección de variable
    buttons = []
    for var in ['Último', 'Apertura']:
        buttons.append(dict(method='update',
                            label=var,
                            args=[{'visible': [col == var for col in ['Último', 'Apertura']]}]))

    fig.update_layout(updatemenus=[dict(active=0, buttons=buttons)])

    # Mostrar el gráfico interactivo 2
    fig.show()

    # Asegúrate de tener 'df_sp500' correctamente cargado y procesado
    df_sp500['Máximo']=df_sp500['Máximo'].str.replace('.', '').str.replace(',', '.').astype(float)
    df_sp500['Mínimo']=df_sp500['Mínimo'].str.replace('.', '').str.replace(',', '.').astype(float)
    # Crear el gráfico interactivo
    fig = make_subplots(rows=1, cols=1, shared_xaxes=True, shared_yaxes=True,
                        subplot_titles=("Comportamiento a lo largo del tiempo"))

    # Agregar las líneas correspondientes a cada variable
    fig.add_trace(go.Scatter(x=df_sp500['Fecha'], y=df_sp500['Máximo'], mode='lines', name='Máximo'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_sp500['Fecha'], y=df_sp500['Mínimo'], mode='lines', name='Mínimo'), row=1, col=1)

    # Actualizar el diseño del gráfico
    fig.update_layout(title_text="Comportamiento a lo largo del tiempo",
                    xaxis_title="Fecha",
                    yaxis_title="Valor",
                    showlegend=True)

    # Agregar botones de selección de variable
    buttons = []
    for var in [ 'Máximo', 'Mínimo']:
        buttons.append(dict(method='update',
                            label=var,
                            args=[{'visible': [col == var for col in [ 'Máximo', 'Mínimo']]}]))

    fig.update_layout(updatemenus=[dict(active=0, buttons=buttons)])

    # Mostrar el gráfico interactivo
    fig.show()

    # Codigo grafico 4
    # Seleccionar las columnas relevantes para el boxplot
    columns_to_plot = ['Último', 'Apertura', 'Máximo', 'Mínimo']

    # Crear el boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_sp500[columns_to_plot])
    plt.title('Boxplot de variables')
    plt.xlabel('Variables')
    plt.ylabel('Valores')
    plt.xticks(rotation=45)
    plt.show()

    return df_sp500
    
data_visualization()