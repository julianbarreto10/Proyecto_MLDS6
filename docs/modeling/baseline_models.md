# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

Se seleccionan tres modelos para la clasificacion de los datos historicos del indice S&P 500 en 3 grupos, positivos, neutro y negativo. Esto con el fin de poder dar una estimación General del comportamiento del mercado en el dia siguente.

LSTM

La LSTM es una variante de las RNN diseñada para abordar el problema del olvido a largo plazo que afecta a las RNN estándar. Utiliza una estructura de celdas de memoria con compuertas de entrada, salida y olvido, lo que le permite recordar información relevante de largo plazo y descartar información irrelevante. En el caso del histórico del índice S&P 500, donde los patrones pueden tener dependencias a largo plazo, como ciclos económicos o tendencias a largo plazo, la LSTM podría ser útil para capturar estas relaciones temporales complejas y hacer predicciones precisas.

GRU

La GRU es una variante más ligera de la LSTM que combina algunas de las compuertas de la LSTM en una sola compuerta de actualización. Esto simplifica la arquitectura y reduce el número de parámetros, lo que puede hacer que la GRU sea más rápida de entrenar y menos propensa al sobreajuste, especialmente en conjuntos de datos más pequeños o cuando los datos son menos complejos. En el caso del índice S&P 500, donde la velocidad de entrenamiento y la capacidad de generalización pueden ser importantes debido a la gran cantidad de datos disponibles, la GRU podría ser una opción adecuada.

SimpleRNN

A diferencia de la LSTM y la GRU, el SimpleRNN no tiene mecanismos de compuertas para manejar el olvido a largo plazo, lo que puede hacerlo menos efectivo para capturar dependencias a largo plazo en los datos. Sin embargo, el SimpleRNN es computacionalmente más eficiente y puede ser más fácil de interpretar y entrenar en comparación con los modelos más complejos como la LSTM y la GRU. Para el histórico del índice S&P 500, donde los patrones pueden ser relativamente simples y no requerir una memoria a largo plazo sofisticada, el SimpleRNN podría proporcionar resultados satisfactorios con menos recursos computacionales.

## Variables de entrada

Lista de las variables de entrada utilizadas en el modelo.

 * Último
 * Apertura
 * Máximo
 * Mínimo

estas vairables forman una serie de tiempo en funcion de la fecha, la varible objetivo es Último, la cual se debe tener en cuenta su valor anterior para predecir el siguiente valor.

## Variable objetivo

la varible objetivo es Último.

## Evaluación del modelo

### Métricas de evaluación

MAE (Mean Absolute Error): El MAE mide la precisión de un modelo de predicción calculando el promedio de las diferencias absolutas entre las predicciones y los valores reales. Es intuitivo y fácil de interpretar, ya que indica cuánto se espera que las predicciones se desvíen de los valores reales en promedio.

MSE (Mean Squared Error): El MSE evalúa la calidad de un modelo de predicción tomando el promedio de los cuadrados de las diferencias entre las predicciones y los valores reales. Al elevar al cuadrado las diferencias, el MSE penaliza más los grandes errores, lo que lo hace sensible a valores atípicos y útil para destacar grandes discrepancias en las predicciones.

### Resultados de evaluación

| Modelo | MAE | MSE | 
| --- | --- | --- | 
| LSTM | 0.02647 |  0.00113 |
| GRU |  0.001158 | 0.02852 |
| SimpleRNN | **0.000843** | **0.0238** |

## Análisis de los resultados

MSE (Mean Squared Error):

El SimpleRNN tiene el menor MSE con 0.000843, lo que sugiere que en promedio, los errores al cuadrado de sus predicciones son los más pequeños entre los tres modelos. Esto indica que este modelo tiene menos errores grandes en comparación con los otros.
El LSTM sigue con un MSE de 0.00113, que es mayor que el de SimpleRNN pero menor que el de GRU.
El GRU tiene el mayor MSE con 0.001158, indicando que tiene más errores grandes en sus predicciones comparado con los otros dos modelos.
MAE (Mean Absolute Error):

Nuevamente, el SimpleRNN tiene el menor MAE con 0.0238, lo que significa que, en promedio, sus predicciones están más cerca de los valores reales.
El LSTM tiene un MAE de 0.02647, que es mayor que el de SimpleRNN pero menor que el de GRU.
El GRU presenta el mayor MAE con 0.02852, indicando que, en promedio, sus predicciones están más alejadas de los valores reales en comparación con los otros dos modelos.

## Conclusiones

SimpleRNN tiene el menor MSE y MAE, lo que sugiere que tiene la mejor precisión y el menor error promedio en sus predicciones.
El LSTM es el segundo mejor modelo, con métricas de error más altas que el SimpleRNN pero mejores que las del GRU.
El GRU es el que presenta el peor rendimiento entre los tres modelos en este caso específico, con las métricas de error más altas tanto en MSE como en MAE.

Incorporar métricas adicionales como MAPE y R², y probar diferentes optimizadores y estrategias de aprendizaje dinámico, junto con métodos de ensamblaje, puede conducir a predicciones más precisas y un rendimiento optimizado del modelo.

## Referencias

Lista de referencias utilizadas para construir el modelo baseline y evaluar su rendimiento.

Espero que te sea útil esta plantilla. Recuerda que puedes adaptarla a las necesidades específicas de tu proyecto.
