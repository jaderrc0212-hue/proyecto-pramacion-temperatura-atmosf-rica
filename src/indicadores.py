import pandas as pd
import os

def calcular_indicadores(df_path="datos/procesados/dataset_limpio.csv", output_path="resultados/indicadores.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(df_path)
    
    indicadores = []
    
    # 1. Total de registros válidos
    indicadores.append({
        'Indicador': 'Total de Registros Válidos',
        'Método': 'len(df)',
        'Resultado': len(df),
        'Interpretación': 'Cantidad total de observaciones limpias disponibles para el análisis.'
    })
    
    # 2. Promedio de la variable principal (forzando conversión numérica)
    if 't_max' in df.columns:
        df['t_max'] = pd.to_numeric(df['t_max'], errors='coerce')
        prom_max = df['t_max'].mean()
        indicadores.append({
            'Indicador': 'Temperatura Máxima Promedio',
            'Método': 'df["t_max"].mean()',
            'Resultado': round(prom_max, 2) if pd.notnull(prom_max) else 0,
            'Interpretación': 'Indica la tendencia térmica superior global del periodo analizado.'
        })
        
    # 3. Porcentaje de casos con amplitud térmica alta (> 15°C)
    if 'amplitud_termica' in df.columns:
        df['amplitud_termica'] = pd.to_numeric(df['amplitud_termica'], errors='coerce')
        casos_altos = (df['amplitud_termica'] > 15).sum()
        pct = (casos_altos / len(df)) * 100
        indicadores.append({
            'Indicador': 'Porcentaje de Amplitud Térmica Alta (>15°C)',
            'Método': '(df["amplitud_termica"] > 15).sum() / len(df) * 100',
            'Resultado': f"{round(pct, 2)}%",
            'Interpretación': 'Mide la frecuencia de días con alta oscilación térmica en las estaciones.'
        })
        
    # 4. Valor máximo absoluto de temperatura
    if 't_max' in df.columns:
        val_max = df['t_max'].max()
        indicadores.append({
            'Indicador': 'Temperatura Máxima Absoluta',
            'Método': 'df["t_max"].max()',
            'Resultado': val_max,
            'Interpretación': 'Identifica el registro extremo superior detectado en el territorio.'
        })
        
    # 5. Cantidad de años distintos analizados
    if 'anio' in df.columns:
        total_anios = df['anio'].nunique()
        indicadores.append({
            'Indicador': 'Total de Años en el Dataset',
            'Método': 'df["anio"].nunique()',
            'Resultado': total_anios,
            'Interpretación': 'Representa la amplitud temporal histórica cubierta por el monitoreo.'
        })
        
    df_ind = pd.DataFrame(indicadores)
    df_ind.to_csv(output_path, index=False, encoding='utf-8')
    print("[INDICADORES] Generados y guardados correctamente en:", output_path)
    return df_ind

    df_ind = pd.DataFrame(indicadores)
    df_ind.to_csv(output_path, index=False, encoding='utf-8')
    print("[INDICADORES] Generados y guardados correctamente en:", output_path)
    return df_ind

if __name__ == "__main__":
    calcular_indicadores()