import pandas as pd 

df = pd.read_excel("~/Documentos/jesus.xls", index_col=[0])
al = df['Apellidos']
print(df) 