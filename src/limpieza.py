import pandas as pd

def limpiar_datos(df):
    """Limpia espacios, elimina duplicados y trata valores nulos."""
    # 1. Eliminar duplicados
    df = df.drop_duplicates()
    
    # 2. Normalizar nombres de columnas
    df.columns = df.columns.str.strip().str.lower()
    
    # 3. Tratamiento seguro de nulos en t_min (convertir a numérico primero)
    if 't_min' in df.columns:
        df['t_min'] = pd.to_numeric(df['t_min'], errors='coerce')
        df['t_min'] = df['t_min'].fillna(df['t_min'].mean())
        
    return df