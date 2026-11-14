import pandas as pd
import unicodedata

ruta = "datos/procesados/dataset_limpio.csv"
try:
    # Leemos sin low_memory para evitar el conflicto con el motor de python
    df = pd.read_csv(ruta, sep=None, engine='python')
    print("¡Archivo leído con éxito!\n")
    
    print("--- COLUMNAS DETECTADAS EN EL CSV ---")
    for col in df.columns:
        print(f"Nombre original: {repr(col)} -> Normalizado: {repr(unicodedata.normalize('NFC', str(col)).strip().lower())}")
    
    print(f"\nTotal de filas en el dataset: {len(df)}")
    
    print("\n--- PRIMERAS 3 FILAS ---")
    print(df.head(3))
    
except Exception as e:
    print(f"Error al leer el archivo: {e}")