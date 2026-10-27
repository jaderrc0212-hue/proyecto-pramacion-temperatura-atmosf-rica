from src.carga import cargar_datos, inspeccionar_datos

def main():
    # Ruta relativa al archivo dentro de la carpeta datos/
    ruta = "datos/dataset.csv"
    
    print("Iniciando proceso de carga...")
    datos = cargar_datos(ruta)
    
    if datos is not None:
        print("Carga realizada correctamente.")
        inspeccionar_datos(datos)
    else:
        print("El programa finalizó sin procesar los datos.")

if __name__ == "__main__":
    main()