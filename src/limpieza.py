import pandas as pd

def limpiar_datos(df):
    """Limpia el dataset corrigiendo comas decimales y asegurando valores numéricos."""
    print("\n--- INICIANDO LIMPIEZA DE DATOS ---")
    
    df_limpio = df.copy()
    
    # Normalizar nombres de columnas (quitar espacios y pasar a minúsculas)
    df_limpio.columns = [str(c).strip().lower() for c in df_limpio.columns]
    
    # Reemplazar comas por puntos en todo el DataFrame si son strings, para no perder decimales
    for col in df_limpio.columns:
        if df_limpio[col].dtype == 'object':
            try:
                df_limpio[col] = df_limpio[col].astype(str).str.replace(',', '.', regex=False)
            except Exception:
                pass
                
    # Convertir columnas de temperatura y año a numérico de forma segura
    for col in df_limpio.columns:
        if any(k in col for k in ['max', 'min', 'med', 'año', 'anio', 'year', 'altura', 'lat', 'lon']):
            df_limpio[col] = pd.to_numeric(df_limpio[col], errors='coerce')
            
    # Eliminar duplicados si los hay
    df_limpio = df_limpio.drop_duplicates()
    
    print(f"Filas tras limpieza: {df_limpio.shape[0]}")
    print("--- LIMPIEZA FINALIZADA ---")
    return df_limpio

if __name__ == "__main__":
    pass