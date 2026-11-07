import pandas as pd
import os

def calcular_estadisticas(df_path="datos/procesados/dataset_limpio.csv", output_path="resultados/estadisticas.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(df_path)
    
    # Seleccionar columnas numéricas relevantes (ej: t_min, t_max, amplitud_termica)
    columnas_numericas = ['t_min', 't_max', 'amplitud_termica'] if 'amplitud_termica' in df.columns else df.select_dtypes(include=['number']).columns
    
    stats = []
    for col in columnas_numericas:
        if col in df.columns:
            s = df[col].dropna()
            stats.append({
                'variable': col,
                'count': len(s),
                'mean': s.mean(),
                'median': s.median(),
                'min': s.min(),
                'max': s.max(),
                'range': s.max() - s.min(),
                'std': s.std(),
                'q25': s.quantile(0.25),
                'q50': s.quantile(0.50),
                'q75': s.quantile(0.75)
            })
            
    df_stats = pd.DataFrame(stats)
    df_stats.to_csv(output_path, index=False, encoding='utf-8')
    print("[ESTADÍSTICAS] Generadas y guardadas correctamente en:", output_path)
    return df_stats

if __name__ == "__main__":
    calcular_estadisticas()