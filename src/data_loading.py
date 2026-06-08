
# src/data_loading.py

import pandas as pd

def cargar_datos(ruta):
    """
    Carga un archivo CSV y retorna un DataFrame
    """
    try:
        df = pd.read_csv(ruta)
    except FileNotFoundError:
        print(
            f"No se encontro el archivo '{ruta}'. "
            "Verifica que el CSV este en la misma carpeta del notebook."
        )
        return None
    print(f"Datos cargados: {df.shape[0]} filas y {df.shape[1]} columnas.")
    return df
