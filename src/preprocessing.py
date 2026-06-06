import pandas as pd

def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    # eliminar duplicados
    df = df.drop_duplicates()

    # imputación
    num_cols = df.select_dtypes(include=['float64','int64']).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df
