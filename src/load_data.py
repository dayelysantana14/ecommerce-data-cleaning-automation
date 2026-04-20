import pandas as pd
import os

# Carga y concatena todos los archivos CSV dentro de una carpeta
# Permite trabajar con múltiples fuentes de datos como un único DataFrame
def load_all_csv(folder_path):
    dfs = []  # Lista para almacenar los DataFrames individuales

    # Recorre todos los archivos en la carpeta especificada
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):  # Filtra solo archivos CSV
            path = os.path.join(folder_path, file)  # Construye la ruta completa
            df = pd.read_csv(path)  # Lee el archivo CSV
            dfs.append(df)  # Agrega el DataFrame a la lista

    # Combina todos los DataFrames en uno solo
    return pd.concat(dfs, ignore_index=True)

# ruta = "../archive"
# df_total = load_all_csv(ruta) 

# # EDA
# print(df_total.shape)
# print(df_total.head())
# print(df_total.info())
# print("Cantidad de nulos")
# print(df_total.isnull().sum())
# print("Cantidad de duplicados")
# print(df_total.duplicated().sum())