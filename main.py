import os
from src.carga import cargar_datos, inspeccionar_datos
from src.limpieza import limpiar_datos
from src.transformaciones import aplicar_transformaciones
from src.validaciones import validar_dataset

def main():
    # 1. Ruta actualizada a la carpeta de originales (respetando el archivo sin modificar)
    ruta_entrada = os.path.join("datos", "originales", "dataset.csv")
    ruta_salida = os.path.join("datos", "procesados", "dataset_limpio.csv")
    
    print("--- INICIANDO PIPELINE DE DATOS (AVANCE 2) ---")
    
    # 2. Carga
    datos = cargar_datos(ruta_entrada)
    
    if datos is not None:
        print("Carga realizada correctamente.")
        
        # 3. Limpieza
        datos_limpios = limpiar_datos(datos)
        
        # 4. Transformaciones
        datos_transformados = aplicar_transformaciones(datos_limpios)
        
        # 5. Validación
        validar_dataset(datos_transformados)
        
        # 6. Exportación (Guardar en procesados sin tocar el original)
        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        datos_transformados.to_csv(ruta_salida, index=False, sep=';', encoding='utf-8')
        print(f"\n¡Dataset limpio exportado exitosamente en: {ruta_salida}!")
        
    else:
        print("El programa finalizó sin procesar los datos debido a un error de carga.")

if __name__ == "__main__":
    main()