from src.load_data import load_all_csv
from src.clean_data import *
from src.transform_data import *
from src.export_data import * 
from src.send_email import *

# 1. Load
df = load_all_csv("data/raw")

# 2. Clean
df = select_columns(df)
df = rename_columns(df)
df = clean_price(df)
df = clean_discount(df)
df = clean_text(df)
df = remove_duplicates(df)
df = remove_nulls(df)

# 3. Transform
df = create_price_bins(df)
summary = generate_summary(df)

# 4. Export (OneDrive)
ruta = "C:/Users/Dayely/OneDrive/reportes"

export_clean_data(df, f"{ruta}/dataset_limpio.xlsx")
export_summary(summary, f"{ruta}/resumen.xlsx")

print("Pipeline ejecutado correctamente")  


