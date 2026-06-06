
# src/data_loading.py

import pandas as pd

def cargar_datos(ruta):
    """
    Carga un archivo CSV y retorna un DataFrame
    """
    df = pd.read_csv(ruta)
    return df

