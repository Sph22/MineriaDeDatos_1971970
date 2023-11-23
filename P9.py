import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def generar_grafica(df, nombre_archivo, num_registros):
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])

    #fecha de inicio para calcular los días transcurridos
    fecha_inicio = df['fecha_registro'].iloc[0]
    df['dias_pasados'] = (df['fecha_registro'] - fecha_inicio).dt.days


    df_promedio = df.groupby('dias_pasados')['persona1_edad'].mean().reset_index()

    #egresión
    X = sm.add_constant(df_promedio['dias_pasados'])
    Y = df_promedio['persona1_edad']
    modelo = sm.OLS(Y, X).fit()

    #Intervalo
    confianza_intervalo = modelo.get_prediction(X).conf_int()

    #forecasting
    dias_futuros = pd.DataFrame({'dias_pasados': range(df_promedio['dias_pasados'].max() + 1, df_promedio['dias_pasados'].max() + 100)})
    X_futuro = sm.add_constant(dias_futuros['dias_pasados'])
    prediccion_futuro = modelo.predict(X_futuro)

    #grafica
    plt.figure(figsize=(10, 6))
    plt.scatter(df_promedio['dias_pasados'], df_promedio['persona1_edad'], label='Edades', alpha=0.7)
    plt.plot(df_promedio['dias_pasados'], modelo.predict(X), color='red', label='Recta de Regresión')
    plt.plot(dias_futuros['dias_pasados'], prediccion_futuro, linestyle='dashed', color='blue', label='Forecasting')


    plt.fill_between(df_promedio['dias_pasados'], confianza_intervalo[:, 0], confianza_intervalo[:, 1], color='gray', alpha=0.3, label='Intervalo de Confianza')


    plt.xlabel('Días que han pasado desde {}'.format(fecha_inicio.date()))
    plt.ylabel('Edad de la Persona 1')
    plt.title('Regresion lineal: días pasados vs. promedio de edad de la persona con Forecasting ({} registros)'.format(num_registros))
    plt.legend()
    plt.yticks(range(int(min(Y)), int(max(Y)) + 1))
    plt.savefig(os.path.join('imagenes/Graficas', nombre_archivo))
    plt.tight_layout()
    plt.show()

#Generar gráfica con 5,000 registros
df_5k = pd.read_csv('Actualizacion-Matrimonios2010-2023.csv', nrows=5000)
generar_grafica(df_5k, 'P9RegresionLineal_con_Forecasting.png', 5000)

#generar gráfica con 60,000 registros
df_60k = pd.read_csv('Actualizacion-Matrimonios2010-2023.csv', nrows=60000)
generar_grafica(df_60k, 'P9RegresionLineal_con_Forecasting2.png', 60000)

#generar gráfica con 175,000 registros
df_175k = pd.read_csv('Actualizacion-Matrimonios2010-2023.csv', nrows=175000)
generar_grafica(df_175k, 'P9RegresionLineal_con_Forecasting3.png', 175000)
