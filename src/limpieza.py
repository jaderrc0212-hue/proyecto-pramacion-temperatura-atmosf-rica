import pandas as pd
import os

def limpiar_datos(df_o_path="datos/originales/dataset.csv"):
    print("\n--- INICIANDO LIMPIEZA DE DATOS ---")
    
    # Cargar correctamente especificando el separador punto y coma (;) del archivo original
    if isinstance(df_o_path, str):
        if os.path.exists(df_o_path):
            df_limpio = pd.read_csv(df_o_path, sep=';', encoding='utf-8')
        else:
            # Plan B por si acaso busca en otra ruta
            df_limpio = pd.read_csv("datos/originales/dataset.csv", sep=';', encoding='utf-8')
    else:
        df_limpio = df_o_path.copy()

    # Normalizar nombres de columnas (quitar espacios y pasar a minúsculas)
    df_limpio.columns = [str(c).strip().lower() for c in df_limpio.columns]
    
    # Reemplazar comas por puntos en todo el DataFrame si son strings para no perder decimales
    for col in df_limpio.columns:
        if df_limpio[col].dtype == 'object':
            try:
                df_limpio[col] = df_limpio[col].astype(str).str.replace(',', '.', regex=False)
            except Exception:
                pass

    # Convertir columnas de temperatura y numéricas a formato numérico real de forma segura
    for col in df_limpio.columns:
        if any(k in col for k in ['max', 'min', 'med', 'año', 'anio', 'altura', 'lat', 'lon', 'codigo', 'mes', 'dia']):
            df_limpio[col] = pd.to_numeric(df_limpio[col], errors='coerce')

    # Eliminar duplicados si los hay
    df_limpio = df_limpio.drop_duplicates()
    
    # Guardar automáticamente el dataset limpio para que las estadísticas lo lean perfecto
    os.makedirs("datos/procesados", exist_ok=True)
    df_limpio.to_csv("datos/procesados/dataset_limpio.csv", index=False)
    
    print(f"Filas tras limpieza: {df_limpio.shape}")
    print("--- LIMPIEZA FINALIZADA ---")
    return df_limpio

if __name__ == "__main__":
    limpiar_datos()