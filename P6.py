import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

if not os.path.exists('imagenes/Graficas'):
    os.makedirs('imagenes/Graficas')

df = pd.read_csv('Actualizacion-Matrimonios2010-2023.csv', nrows=185000)
df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])

#fecha de inicio para calcular los días transcurridos
fecha_inicio =  df['fecha_registro'].iloc[0]
df['dias_pasados'] = (df['fecha_registro'] - fecha_inicio).dt.days

#prom edades
df_promedio = df.groupby('dias_pasados')['persona1_edad'].mean().reset_index()

#regresión lineal
X = sm.add_constant(df_promedio['dias_pasados'])
Y = df_promedio['persona1_edad']

#modelo de regresion
modelo = sm.OLS(Y, X).fit()

print(modelo.summary())

plt.figure(figsize=(10, 6))
plt.scatter(df_promedio['dias_pasados'], df_promedio['persona1_edad'], label='Promedios por Día')
plt.plot(df_promedio['dias_pasados'], modelo.predict(X), color='red', label='Recta de Regresión')
plt.xlabel('Días que han pasado desde {}'.format(fecha_inicio.date()))
plt.ylabel('Promedio de Edad de la Persona 1')
plt.title('Regresion lineal: dias pasados vs. promedio de edad de la persona')
plt.legend()

#para que sean enteros
plt.yticks(range(int(min(Y)), int(max(Y))+1))
plt.savefig(os.path.join('imagenes/Graficas', 'Regresion lineal.png'))

plt.tight_layout()
plt.show()
