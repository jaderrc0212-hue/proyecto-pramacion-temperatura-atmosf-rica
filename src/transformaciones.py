import pandas as pd

def aplicar_transformaciones(df):
    """Aplica transformaciones de fechas y variables derivadas."""
    # Convertir columna fecha si existe
    if 'fecha' in df.columns:
        df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
        df['anio'] = df['fecha'].dt.year
        df['mes'] = df['fecha'].dt.month
        df['dia'] = df['fecha'].dt.day
        
    print("Transformaciones aplicadas correctamente.")
    return df