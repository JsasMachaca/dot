import pandas as pd
from random import randint


d = {"Nombre":["Jesus","Martin","Pedro","Lucas"], "Apellidos":["Machaca", "Lopez", "Quispe", "Ponce"]}
df_invent = pd.DataFrame(d)
df_invent["Direccion"]= ["Jr. Pedro 123", "Jr. no se me ocurre otro", "Jr. alabaré 321", "jr. luis rwsudf 098"]
df_invent["Edad"] = [randint(16,18) for i in range(len(d["Nombre"]))]
h = df_invent.set_index("Nombre")
print(df_invent)
#print(df_invent[df_invent["Edad"] == 17]["Nombre"])
