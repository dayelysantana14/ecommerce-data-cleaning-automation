import os

# Exporta el dataset limpio a un archivo Excel
# Crea automáticamente la carpeta destino si no existe
def export_clean_data(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)  # Asegura que la ruta exista
    df.to_excel(path, index=False)  # Guarda el DataFrame sin índice


# Exporta el resumen (tabla agregada) a un archivo Excel
# También valida la existencia de la carpeta destino
def export_summary(summary, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)  # Crea carpeta si no existe
    summary.to_excel(path)  # Exporta el resumen