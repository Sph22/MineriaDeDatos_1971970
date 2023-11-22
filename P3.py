import pandas as pd

df = pd.read_csv('Actualizacion-Matrimonios2010-2023.csv')

edad_promedio_persona1 = df['persona1_edad'].mean()
conteo_sexo_persona1 = df['persona1_sexo'].value_counts()
tipo_matrimonio_mas_comun = df['tipo_matrimonio'].mode()[0]
min_persona1_edad = int(df['persona1_edad'].min())
max_persona2_edad = int(df['persona2_edad'].max())
sumatoria_persona1_edad = df['persona1_edad'].sum()
varianza_persona2_edad = df['persona2_edad'].var()
desviacion_estandar_persona2_edad = df['persona2_edad'].std()
asimetria_persona1_edad = df['persona1_edad'].skew()
kurtosis_persona2_edad = df['persona2_edad'].kurtosis()

print('Edad Promedio persona 1:', edad_promedio_persona1)                                              #Media
print('Conteo de hombres:\n',conteo_sexo_persona1)                                                     #Conteo
print('Tipo de matrimonio mas comun:',tipo_matrimonio_mas_comun)                                       #Moda
print('Edad mínima de la persona 1:', min_persona1_edad)                                               #Mínimo
print('Edad máxima de la persona 2:', max_persona2_edad)                                               #Máximo
print('Sumatoria de la persona 1 (edad):', sumatoria_persona1_edad)                                    #Sumatoria
print('Varianza de la persona 2 (edad):', varianza_persona2_edad)                                      #Varianza
print('Desviación estándar de la persona 2 (edad):', desviacion_estandar_persona2_edad)                #DsvEst
print('Asimetria de la persona 1 (edad):', asimetria_persona1_edad)                                    #Asimetria
print('Kurtosis de la persona 2 (edad):', kurtosis_persona2_edad)                                      #Kurtosis
