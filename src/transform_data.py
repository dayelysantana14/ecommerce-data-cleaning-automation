import pandas as pd

# Crea categorías de precios para segmentar los productos
# Permite analizar el comportamiento de ventas por rangos de precio
def create_price_bins(df):
    df["rango_precio"] = pd.cut(
        df["precio"],
        bins=[0, 5, 10, 20, 50, 100],  # Intervalos definidos
        labels=["0-5", "5-10", "10-20", "20-50", "50+"]  # Etiquetas de cada rango
    )
    return df


# Genera un resumen agregado del precio promedio por categoría (ranking)
# Facilita el análisis comparativo entre distintos segmentos de productos
def generate_summary(df):
    return pd.pivot_table(
        df,
        values="precio",
        index="ranking",
        aggfunc="mean"
    )