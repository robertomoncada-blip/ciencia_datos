import panda as pd

def cargar_datos(ruta):
    """Lee el dataset y devuelve un DataFrame."""
    return pd.read_csv(ruta)

df = cargar_datos('data/raw/AI_Impact_on_Jobs_2030.csv')
print(df.shape, df.dtypes)

