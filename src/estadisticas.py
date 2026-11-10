import pandas as pd
import os
import re

def calcular_estadisticas(df_path="datos/procesados/dataset_limpio.csv", output_path="resultados/estadisticas.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    if os.path.exists(df_path):
        try:
            df = pd.read_csv(df_path, sep=',', encoding='utf-8')
        except:
            df = pd.read_csv(df_path, sep=';', encoding='utf-8')
    else:
        df = pd.read_csv("datos/originales/dataset.csv", sep=None, engine='python', encoding='utf-8')

    print("\n[ESTADÍSTICAS] Limpiando símbolos y procesando temperaturas...")
    df.columns = [str(c).strip().lower() for c in df.columns]
    
    for col in df.columns:
        if df[col].dtype == object:
            # Reemplazar comas por puntos y eliminar cualquier símbolo de texto o grados que estorbe
            df[col] = df[col].astype(str).str.replace(',', '.', regex=False)
            df[col] = df[col].apply(lambda x: re.sub(r'[^0-9\.\-]', '', x) if pd.notnull(x) else x)
            df[col] = df[col].replace(['', '.', '-', '.-'], pd.NA)
            
        df[col] = pd.to_numeric(df[col], errors='coerce')

    stats = df.describe().T
    stats.reset_index(inplace=True)
    stats.rename(columns={'index': 'variable', '50%': 'median'}, inplace=True)
    
    stats.to_csv(output_path, index=False)
    print(f"[ESTADÍSTICAS] ¡Éxito! Estadísticas reales actualizadas en: {output_path}")

if __name__ == "__main__":
    calcular_estadisticas()