import pandas as pd

# Selecciona únicamente las columnas relevantes del dataset original
def select_columns(df):
    columns = [
        "goods-title-link--jump",
        "price",
        "discount",
        "rank-title"
    ]
    return df[columns]


# Renombra las columnas a nombres más claros y consistentes en español
def rename_columns(df):
    return df.rename(columns={
        "goods-title-link--jump": "producto",
        "price": "precio",
        "discount": "descuento",
        "rank-title": "ranking"
    })


# Limpia y convierte la columna de precios a formato numérico
def clean_price(df):
    df["precio"] = df["precio"].astype(str)  # Asegura que todos los valores sean texto
    df["precio"] = df["precio"].str.replace("$", "", regex=False)  # Elimina símbolo $
    df["precio"] = pd.to_numeric(df["precio"], errors="coerce")  # Convierte a número
    return df


# Limpia y convierte la columna de descuentos a formato numérico
def clean_discount(df):
    df["descuento"] = df["descuento"].astype(str)  # Convierte a texto
    df["descuento"] = df["descuento"].str.replace("%", "", regex=False)  # Elimina %
    df["descuento"] = df["descuento"].str.replace("-", "", regex=False)  # Elimina signo negativo
    df["descuento"] = pd.to_numeric(df["descuento"], errors="coerce")  # Convierte a número
    return df


# Normaliza el texto del nombre del producto (minúsculas y sin espacios extra)
def clean_text(df):
    df["producto"] = df["producto"].str.lower().str.strip()
    return df


# Elimina registros con valores nulos en columnas clave (precio)
def remove_nulls(df):
    return df.dropna(subset=["precio"])


# Elimina registros duplicados para evitar inconsistencias
def remove_duplicates(df):
    return df.drop_duplicates()