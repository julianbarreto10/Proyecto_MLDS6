# Diccionario de datos

## df_sp500

La tabal muestra todas las variables incluidas en el dataframe desde su carga desde google drive, ademas de la varaible "SENT" la cual fue agregada para evaluar el comportamiento entre dias del indice.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| Fecha | fecha en la que se registraron los precios históricos. | Fecha "YYYY-MM-DD" | 1994-04-04 - 2014-02-10 | df_sp500 |
| Último |  precio al que se negociaron las acciones al final del día de operaciones. | float | (400,200) | df_sp500 |
| Apertura | precio con el que se inicia la sesión de negociación.| float | (400,200) |df_sp500 |
| Máximo | punto máximo de la cotización durante el día de negociación |  float | (400,200) |df_sp500 |
| Mínimo	|  punto más bajo de la cotización durante el día de negociación. |  float | (400,200) |df_sp500 |
| 	% var.	| cantidad total de acciones del índice S&P 500 que se intercambiaron durante el período de tiempo determinado | float | (-5 , 5) |df_sp500  |
| SENT	|  cambio del indice entre dia |  texto | positivo - negatico - neutro |df_sp500 |




