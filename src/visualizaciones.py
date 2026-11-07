import pandas as pd
import matplotlib.pyplot as plt
import os

def generar_graficos(df_path=None, output_dir="resultados/graficos/"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Buscar el archivo disponible
    df = None
    for ruta in ["datos/originales/dataset.csv", "datos/procesados/dataset_limpio.csv"]:
        if os.path.exists(ruta):
            for sep in [';', ',', '\t']:
                try:
                    temp = pd.read_csv(ruta, sep=sep, encoding='utf-8', low_memory=False)
                    if len(temp.columns) > 1 and len(temp) > 0:
                        df = temp
                        break
                except:
                    try:
                        temp = pd.read_csv(ruta, sep=sep, encoding='latin-1', low_memory=False)
                        if len(temp.columns) > 1 and len(temp) > 0:
                            df = temp
                            break
                    except:
                        continue
            if df is not None:
                break
                
    if df is None or df.empty:
        print("[ERROR] No se pudo leer el dataset.")
        return

    print("\n[GRÁFICOS] Procesando y limpiando datos...")
    
    # Normalizar nombres de columnas
    df.columns = [str(c).strip().lower() for c in df.columns]
    
    col_max = next((c for c in df.columns if 'max' in c), None)
    col_min = next((c for c in df.columns if 'min' in c), None)
    col_anio = next((c for c in df.columns if 'año' in c or 'anio' in c or 'year' in c), None)
    
    print(f"Columnas detectadas -> Máx: {col_max}, Mín: {col_min}, Año: {col_anio}")
    
    # Función robusta para limpiar y convertir columnas numéricas
    def limpiar_columna_numerica(serie):
        if serie is None:
            return pd.Series(dtype=float)
        # Convertir a texto, reemplazar comas por puntos, y quitar cualquier cosa que no sea número, punto o signo menos
        s_limpia = (
            serie.astype(str)
            .str.strip()
            .str.replace(',', '.', regex=False)
            .str.replace(r'[^0-9.\-]', '', regex=True)
        )
        return pd.to_numeric(s_limpia, errors='coerce')

    if col_max:
        df[col_max] = limpiar_columna_numerica(df[col_max])
        print(f"Datos válidos en {col_max}: {df[col_max].dropna().count()}")
        
    if col_min:
        df[col_min] = limpiar_columna_numerica(df[col_min])
        print(f"Datos válidos en {col_min}: {df[col_min].dropna().count()}")
        
    if col_anio:
        df[col_anio] = limpiar_columna_numerica(df[col_anio])

    plt.style.use('ggplot')
    
    # Gráfico 1: Histograma de Temperatura Máxima
    if col_max and df[col_max].dropna().count() > 0:
        plt.figure(figsize=(8, 5))
        plt.hist(df[col_max].dropna(), bins=30, color='skyblue', edgecolor='black')
        plt.title('Distribución de Temperaturas Máximas')
        plt.xlabel('Temperatura Máxima (°C)')
        plt.ylabel('Frecuencia')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'grafico_01.png'), dpi=300)
        plt.close()
        print("-> [ÉXITO] Se generó grafico_01.png")
        
    # Gráfico 2: Evolución histórica por año
    if col_anio and col_max:
        df_anual = df.groupby(col_anio)[col_max].mean().reset_index().dropna()
        if not df_anual.empty:
            plt.figure(figsize=(9, 5))
            plt.plot(df_anual[col_anio], df_anual[col_max], marker='o', color='firebrick', linewidth=2)
            plt.title('Evolución Histórica de la Temperatura Máxima Promedio')
            plt.xlabel('Año')
            plt.ylabel('Temperatura Promedio (°C)')
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'grafico_02.png'), dpi=300)
            plt.close()
            print("-> [ÉXITO] Se generó grafico_02.png")
        
    # Gráfico 3: Dispersión entre Mínima y Máxima
    if col_min and col_max:
        df_sub = df[[col_min, col_max]].dropna()
        if not df_sub.empty:
            plt.figure(figsize=(8, 5))
            plt.scatter(df_sub[col_min], df_sub[col_max], alpha=0.3, color='forestgreen', edgecolors='none')
            plt.title('Relación entre Temperatura Mínima y Máxima')
            plt.xlabel('Temperatura Mínima (°C)')
            plt.ylabel('Temperatura Máxima (°C)')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'grafico_03.png'), dpi=300)
            plt.close()
            print("-> [ÉXITO] Se generó grafico_03.png")
            
    print("[GRÁFICOS] ¡Imágenes creadas con éxito en resultados/graficos/!")

if __name__ == "__main__":
    generar_graficos()