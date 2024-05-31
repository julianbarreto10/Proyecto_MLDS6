#!/usr/bin/env python3
import sys 
import pandas as pd
import numpy as np
sys.path.append('/workspaces/Proyecto_MLDS6/scripts')
import training.GRU_model as gru
import training.best_model as bst
import training.LSTM_model as lstm
import training.SimpleRNN_model as simp

model1, loss1, mae1=gru.GRU_model_()
model2, loss2, mae2=bst.SimpleRNN_model_()
model3, loss3, mae3=lstm.LSTM_model_()
model4, loss4, mae4=simp.SimpleRNN_model_()

name1= "GRU_model"
name2= "best_model"
name3= "LSTM_model"
name4= "SimpleRNN_model"

# Datos de los modelos
data = {
    "Name": [name1, name2, name3, name4],
    "MSE": [loss1, loss2, loss3, loss4],
    "MAE": [mae1, mae2, mae3, mae4],
    
}

# Crear el DataFrame
df = pd.DataFrame(data)
df.to_csv('model_data.csv', index=False)
# Mostrar el DataFrame
print(df)