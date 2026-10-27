import pandas as pd

def cargar_datos(ruta):
    """
    Carga un conjunto de datos desde un archivo CSV con separador de punto y coma.
    """
    try:
        datos = pd.read_csv(ruta, sep=';', on_bad_lines='skip', low_memory=False, encoding='utf-8')
        return datos
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta}'.")
    except pd.errors.EmptyDataError:
        print("Error: el archivo no contiene datos.")
    except pd.errors.ParserError:
        print("Error: no fue posible interpretar el archivo.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return None

def inspeccionar_datos(datos):
    """
    Realiza una inspección inicial del DataFrame.
    """
    if datos is None:
        print("No existen datos disponibles para inspeccionar.")
        return
    
    print("\n--- Dimensiones ---")
    print(datos.shape)
    
    print("\n--- Columnas ---")
    print(datos.columns.tolist())
    
    print("\n--- Tipos de datos ---")
    print(datos.dtypes)
    
    print("\n--- Primeros registros ---")
    print(datos.head())
    
    print("\n--- Valores nulos por columna ---")
    print(datos.isna().sum())
    
    print("\n--- Filas duplicadas ---")
    print(datos.duplicated().sum())
    
    print("\n--- Resumen estadístico ---")
    print(datos.describe(include="all"))