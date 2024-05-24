# Reporte del Modelo Final

## Resumen Ejecutivo

En esta sección se presentará un resumen de los resultados obtenidos del modelo SimpleRNN para la prediccion del Indice S&P500.
## Descripción del Problema

El principal objetivo es desarrollar un modelo predictivo de alta precisión para el S&P 500 utilizando redes neuronales recurrentes, específicamente el modelo SimpleRNN. Este modelo fue seleccionado debido a su capacidad demostrada para capturar dependencias temporales en secuencias de datos, mostrando mejores resultados en términos de MSE y MAE en comparación con modelos más complejos como LSTM y GRU en este contexto particular. La simplicidad y efectividad del SimpleRNN lo hacen ideal para implementaciones en tiempo real, proporcionando predicciones precisas con menor complejidad computacional. Esto permite a los actores del mercado bursátil tomar decisiones más informadas y sustentadas, reduciendo el riesgo y optimizando las ganancias basándose en predicciones fiables del comportamiento del índice S&P 500.
## Descripción del Modelo

El modelo final desarrollado para resolver el problema planteado es una red neuronal SimpleRNN, diseñada específicamente para analizar series temporales del índice S&P 500. La metodología utilizada sigue un enfoque de desarrollo de modelos de aprendizaje profundo, comenzando con un proceso de preparación y limpieza de datos para garantizar la calidad y coherencia de los datos de entrada. Posteriormente, se procede con la construcción, entrenamiento y validación del modelo SimpleRNN utilizando conjuntos de datos históricos del S&P 500. Se implementa un proceso de ajuste de hiperparámetros para optimizar el rendimiento del modelo, permitiendo explorar diferentes configuraciones para encontrar la mejor combinación de parámetros. Finalmente, se evalúa el modelo utilizando métricas de rendimiento pertinentes, como el error cuadrático medio (MSE) y el error absoluto medio (MAE), y se realizan pruebas exhaustivas para garantizar su precisión y confiabilidad antes de su despliegue. Este enfoque metodológico permite construir un modelo robusto y eficaz para predecir el comportamiento del índice S&P 500

## Evaluación del Modelo


El modelo SimpleRNN ha sido evaluado utilizando dos métricas principales: el Error Cuadrático Medio (MSE) y el Error Absoluto Medio (MAE). Estas métricas proporcionan información importante sobre la precisión y el rendimiento del modelo en la predicción del comportamiento del índice S&P 500.

Error Cuadrático Medio (MSE):

El MSE del modelo SimpleRNN es de 0.000843. Esta métrica cuantifica la magnitud promedio de los errores al cuadrado entre las predicciones del modelo y los valores reales del índice S&P 500. Un MSE más bajo indica que el modelo genera predicciones más cercanas a los valores reales, lo que sugiere una mayor precisión en las predicciones.
Error Absoluto Medio (MAE):

El MAE del modelo SimpleRNN es de 0.0238. Esta métrica representa el promedio de las diferencias absolutas entre las predicciones del modelo y los valores reales del índice S&P 500. Un MAE más bajo indica que el modelo tiene una menor discrepancia absoluta en sus predicciones, lo que implica una mayor precisión y confiabilidad en las predicciones.
Interpretando los resultados, observamos que el modelo SimpleRNN ha obtenido valores muy bajos tanto en MSE como en MAE, lo que sugiere que el modelo es altamente preciso en la predicción del comportamiento del índice S&P 500. Estas métricas indican que las predicciones del modelo están muy cerca de los valores reales, lo que demuestra su eficacia en capturar las tendencias y patrones en los datos históricos del índice. En resumen, el modelo SimpleRNN ha demostrado ser una herramienta valiosa y confiable para la predicción del índice S&P 500, proporcionando a los inversores una base sólida para la toma de decisiones informadas en el mercado bursátil.

## Conclusiones y Recomendaciones

El modelo SimpleRNN ha demostrado ser altamente preciso en la predicción del comportamiento del índice S&P 500, con valores bajos tanto en MSE como en MAE. Sus puntos fuertes incluyen su capacidad para capturar dependencias temporales en series temporales financieras y su eficiencia computacional en comparación con modelos más complejos. Sin embargo, una limitación potencial podría ser su susceptibilidad a problemas de desvanecimiento y explosión de gradientes en secuencias largas. Recomendaciones futuras podrían incluir la exploración de técnicas de regularización adicionales para mitigar estos problemas y la investigación de enfoques de ensamblado para mejorar aún más la precisión del modelo. Este modelo tiene un amplio potencial de aplicación en la toma de decisiones financieras, como la gestión de carteras, la planificación de inversiones y la identificación de oportunidades de mercado.

## Referencias

En esta sección se deben incluir las referencias bibliográficas y fuentes de información utilizadas en el desarrollo del modelo.
