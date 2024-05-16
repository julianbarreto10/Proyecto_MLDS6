# Definición de los datos

## Origen de los datos

Los datos históricos del comportamiento del índice S&P 500 fueron recopilados a través de los conjuntos de datos disponibles en la plataforma Investing, específicamente utilizando la sección de "Datos históricos del S&P 500". Este conjunto de datos ofrece una visión detallada y exhaustiva del rendimiento del índice, proporcionando información crucial como el valor del índice en diferentes períodos de tiempo, así como los valores de apertura y cierre en el mercado financiero. El conjunto de datos históricos del comportamiento del índice S&P500 (Datos históricos del S&P 500) se descargaron y se cargaron en Google Drive para poder acceder a ellos de manera abierta y y directa.

## Especificación de los scripts para la carga de datos

Inicialmente se carga al programa como un archivo CSV desde Google Drive, se cambia el formato de las colummnas inicialmente definidad como texto por  su  formato correspondiente, "fecha" a formato de fecha , "ultimo" y "apertura" a formato float. finalmente se grafico los datos como una serie de tiempo guardado en la imgaen serie_tiempo_sp500.png
## Referencias a rutas o bases de datos origen y destino



### Rutas de origen de datos

- datos de origen: https://drive.google.com/uc?export=view&id=1QvQewt31IAGzqxgutnzyVjcr9E7p5UPC
  
- [ ] Especificar la estructura de los archivos de origen de los datos.
      
Los datos que estamos manejando son principalmente datos financieros relacionados con el comportamiento del índice S&P 500 en diferentes puntos temporales. Estos datos incluyen una serie de columnas que proporcionan información específica sobre el rendimiento del índice en el mercado financiero. Aquí hay una descripción de las columnas que componen el conjunto de datos:

Fecha: Esta columna indica la fecha en la que se registraron los datos o el período de tiempo al que se refieren las observaciones.

Último: Representa el valor del índice S&P 500 al cierre del período de tiempo especificado. Este valor refleja el precio del índice al final del día de negociación.

Apertura: Indica el valor del índice S&P 500 al comienzo del período de tiempo especificado. Es el precio con el que se inicia la sesión de negociación.

Máximo: Refleja el valor más alto alcanzado por el índice S&P 500 durante el período de tiempo determinado. Representa el punto máximo de la cotización durante el día de negociación.

Mínimo: Indica el valor más bajo alcanzado por el índice S&P 500 durante el período de tiempo especificado. Representa el punto más bajo de la cotización durante el día de negociación.

Vol.: Esta columna puede representar el volumen de negociación, es decir, la cantidad total de acciones del índice S&P 500 que se intercambiaron durante el período de tiempo determinado. La unidad de medida puede variar según el contexto.

% var.: Indica la variación porcentual del valor del índice S&P 500 en comparación con un período de referencia, como el día anterior o el período de apertura. Representa el cambio porcentual en el precio del índice durante el período de tiempo especificado.

- [ ] Describir los procedimientos de transformación y limpieza de los datos.
      
se reviso cuales columnas tienen datos faltantes y se elimino, la unica con datos faltante es "Vol.", posteriomente se termino de cambiar el formato de las demas colimnas a float, eliminado caracteres como "%", y cambiando "," por "." para los decimales. tambien se elimino el "." en lo valores de miles.
El conjunto de datos tiene una variable a estimar y es la variable continua objetivo "Último" la cual trae informacion del comportamiento del indice al momento del cierre del mercado de valores. por lo que definio una nueva variable para definir si al momento de cerrar el mercado hay un cambio postivo, negativo o neutro en el indice.
