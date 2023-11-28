import pandas as pd

df = pd.read_csv('Matrimonios2010-2023.csv')


df = df.drop('anio_registro', axis=1)
df = df.drop('mes_registro', axis=1)
df = df.drop('latitud', axis=1)
df = df.drop('longitud', axis=1)


"""
reemplazos = {
    'SEPARACION DE BIENES': 'SB',
    
}
"""

"""
df['regimen_matrimonio'] = df['regimen_matrimonio'].replace(reemplazos)
"""

#Guarda el archivo ya normalizado
df.to_csv('Actualizacion-Matrimonios2010-2023.csv', index=False)

