"""
¡Zeraora, Charmander, Bulbasaur, Pikachu y otros Pokemon se han escondido por nuestra Facultad! Ahora es tu oportunidad de descubrirlos y 
capturarlos. Cada Pokemon tiene un valor (positivo) asociado y estar´a disponible para ser capturado solo durante unos cuantos dıas, 
pasado este periodo, el Pokemon desaparecer´a para siempre. Teniendo en cuenta que capturar un Pokemon exige un d´ıa completo de b´usqueda, 
tienes que decidir cuales Pokemon capturar y cuando hacerlo para maximizar el valor total.
"""
# importamos las librerías necesarias 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import chardet
from matplotlib.pyplot import rcParams

file_path = "Mochila_Pokemon\pokemon.csv"
with open(file_path, "rb") as f:
    result = chardet.detect(f.read())

# Leer el archivo CSV utilizando la codificación detectada
df_Pokemon = pd.read_csv(file_path, encoding=result["encoding"], on_bad_lines="skip")

