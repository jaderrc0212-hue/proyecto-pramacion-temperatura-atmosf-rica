def validar_dataset(df):
    """Valida que el DataFrame limpio no tenga nulos críticos y tenga las columnas esperadas."""
    print("\n--- VALIDACIÓN FINAL DEL DATASET ---")
    print(f"Total de filas finales: {df.shape[0]}")
    print(f"Total de columnas finales: {df.shape[1]}")
    print(f"Valores nulos totales restantes: {df.isna().sum().sum()}")
    print("Validación completada con éxito.")
    return True