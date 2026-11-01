import os
from src.carga import cargar_datos
from src.limpieza import limpiar_datos
from src.transformaciones import aplicar_transformaciones
from src.validaciones import validar_dataset

def main():
    # 1. Rutas de los archivos
    ruta_entrada = os.path.join("datos", "originales", "dataset.csv")
    ruta_salida = os.path.join("datos", "procesados", "dataset_limpio.csv")
    
    print("--- INICIANDO PIPELINE DE DATOS (AVANCE 2) ---")
    
    # 2. Carga
    datos = cargar_datos(ruta_entrada)
    
    if datos is not None:
        print("Carga realizada correctamente.")
        
        # --- MÉTRICAS DEL "ANTES" (Para tu tabla del informe) ---
        print("\n[ESTADÍSTICAS - ANTES DEL PROCESO]")
        print(f"Filas: {datos.shape[0]}")
        print(f"Columnas: {datos.shape[1]}")
        print(f"Valores nulos: {datos.isnull().sum().sum()}")
        print(f"Filas duplicadas: {datos.duplicated().sum()}")
        print("-" * 40 + "\n")
        
        # 3. Limpieza
        datos_limpios = limpiar_datos(datos)
        
        # 4. Transformaciones
        datos_transformados = aplicar_transformaciones(datos_limpios)
        
        # 5. Validación (imprime los datos del "Después" que ya tenías configurados)
        validar_dataset(datos_transformados)

if __name__ == "__main__":
    main()