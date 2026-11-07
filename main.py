import os
from src.carga import cargar_datos
from src.limpieza import limpiar_datos
from src.transformaciones import aplicar_transformaciones
from src.validaciones import validar_dataset

# Nuevos imports para el Avance 3
from src.estadisticas import calcular_estadisticas
from src.indicadores import calcular_indicadores
from src.visualizaciones import generar_graficos

def main():
    print("--- INICIANDO PIPELINE DE DATOS COMPLETO (AVANCES 2 y 3) ---")
    
    # 1. Rutas de los archivos
    ruta_entrada = os.path.join("datos", "originales", "dataset.csv")
    ruta_salida = os.path.join("datos", "procesados", "dataset_limpio.csv")
    
    # 2. Carga
    datos = cargar_datos(ruta_entrada)
    if datos is not None:
        print("Carga realizada correctamente.")
        
        # 3. Limpieza
        datos_limpios = limpiar_datos(datos)
        
        # 4. Transformaciones
        datos_transformados = aplicar_transformaciones(datos_limpios)
        
        # 5. Validaciones y guardado del dataset limpio (Avance 2)
        validar_dataset(datos_transformados, ruta_salida)
        
        print("\n--- INICIANDO MÓDULOS DE ANÁLISIS (AVANCE 3) ---")
        
        # 6. Calcular y exportar estadísticas
        calcular_estadisticas(ruta_salida, "resultados/estadisticas.csv")
        
        # 7. Calcular y exportar indicadores
        calcular_indicadores(ruta_salida, "resultados/indicadores.csv")
        
        # 8. Generar y guardar gráficos
        generar_graficos(ruta_salida, "resultados/graficos/")
        
        print("\n=== ¡PROCESO COMPLETADO CON ÉXITO! ===")
        print("Verifique los archivos en datos/procesados/, resultados/ y resultados/graficos/")

if __name__ == "__main__":
    main()