# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Metodologías Ágiles para el Desarrollo de Aplicaciones con Machine Learning - Prediccion Valores del Indice S&P500

## Objetivo del Proyecto
[Descripción breve del objetivo del proyecto y por qué es importante]

El presente proyecto se plantea con el objetivo de poder estudiar y predecir los comportamientos que tiene el índice S&P 500 lo cual puede resultar util para diferentes beneficiarios tales como: fondos de inversión, gestores de cartera, inversionistas individuales, analistas financieros y consultores. Con esto se busca que los diferentes operadores del mercado bursatil tengan una herramienta que ayude a la toma de decisiones que permita tener mejores resultados, teniendo un modelo que basado en un historico permita conocer si el indice subira, bajara o se mantendra en un dia especifico.

Para obtener un modelo que traiga informacion de calidad se deben resolver algunos retos tal como la prediccion con una anticipacion lo suficientemente buena para que permita tomar decisiones que se vean reflejadas del S&P 500. Esto lograria que los actores del mercado pudieran reducir el riesgo y optimizar las gananacias, de esta manera se busca reducir la incertidumbre que tiene el mercado historicamente, buscando tomar informaciones mas informadas y sustentadas con los datos que se pueden obtener para el estudio.

## Alcance del Proyecto

### Incluye:

- [Descripción de los datos disponibles]
  
 Los datos disponibles consisten en series temporales del índice S&P 500, que incluyen información diaria sobre el valor del índice, así como datos históricos sobre precios de apertura, cierre, máximo y mínimo, volumen de operaciones.Estos datos abarcan un período significativo de tiempo y se utilizarán como entrada para entrenar la red neuronal LSTM.
- [Descripción de los resultados esperados]
  
Para lograr esto, la red recurrente analizará secuencias de datos pasadas del S&P 500 y aprenderá a identificar patrones que preceden a ciertos movimientos en el mercado, como períodos de aumento, disminución o estabilidad. Luego, utilizará estos patrones aprendidos para generar un valor aproximado del indice en el dia siguiente. Esto permitirá a inversores identificar cuando comprar, vender o mantener acciones del S&P 500 en función de las tendencias identificadas en los datos históricos.
- [Criterios de éxito del proyecto]

  - Precisión y fiabilidad del modelo: El modelo debe ser preciso y confiable en la generación de sugerencias de inversión basadas en el análisis de las series temporales del S&P 500.
  
  - Adaptabilidad del modelo: El modelo debe ser capaz de adaptarse a cambios en las condiciones del mercado y continuar generando sugerencias relevantes y útiles a medida que se actualizan los datos.
    
  - Facilidad de uso: La interfaz del producto final debe ser intuitiva y fácil de usar para los usuarios, permitiendo una rápida comprensión y aplicación de las sugerencias de inversión generadas por el modelo.

### Excluye:

- [Descripción de lo que no está incluido en el proyecto]

## Metodología

[Descripción breve de la metodología que se utilizará para llevar a cabo el proyecto]


El proyecto utilizará una metodología de desarrollo de modelos de aprendizaje profundo, centrándose en el uso de redes neuronales LSTM para analizar series temporales del índice S&P 500. Se llevará a cabo un proceso de preparación y limpieza de datos para garantizar la calidad y coherencia de los datos de entrada. Luego, se procederá con la construcción, entrenamiento y validación de la red neuronal LSTM utilizando conjuntos de datos históricos del S&P 500. Se implementará un proceso de ajuste de hiperparámetros para optimizar el rendimiento del modelo. Finalmente, se evaluará el modelo utilizando métricas de rendimiento pertinentes y se realizarán pruebas exhaustivas para garantizar su precisión y confiabilidad para su posterior despliegue.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semanas | del 2 de mayo al 9 de mayo |
| Preprocesamiento, análisis exploratorio | 1 semanas | del 9 de mayo al 16 de mayo |
| Modelamiento y extracción de características | 1 semanas | del 16 de mayo al 23 de mayo |
| Despliegue | 1 semanas | del 23 de mayo al 30 de mayo |
| Evaluación y entrega final | 1 semanas | del 30 de mayo al  2 jun 2024 |

Hay que tener en cuenta que estas fechas son de ejemplo, estas deben ajustarse de acuerdo al proyecto.

## Equipo del Proyecto

Jorge Steban Moreno Lozano jorgestebanmorenolozano@gmail.com
Julian Mauricio Rodriguez Barreto jumrodriguezba@unal.edu.co
Jose Francisco Lugo Nomesque jlugon@unal.edu.co

 


