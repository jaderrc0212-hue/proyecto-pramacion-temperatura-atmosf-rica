import pandas as pd

def validar_dataset(df, ruta_salida):
    """Valida el dataset limpio, muestra métricas y lo exporta a CSV."""
    print("\n--- VALIDACIÓN FINAL DEL DATASET ---")
    print(f"Total de filas finales: {df.shape[0]}")
    print(f"Total de columnas finales: {df.shape[1]}")
    print(f"Valores nulos totales restantes: {df.isna().sum().sum()}")
    
    # Guardar el archivo limpio en la ruta correspondiente
    df.to_csv(ruta_salida, index=False, encoding='utf-8')
    print(f"Dataset guardado exitosamente en: {ruta_salida}")
    print("Validación completada con éxito.")
    return True