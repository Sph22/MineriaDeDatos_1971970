import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os  # Importar el módulo os para manejar directorios

df = pd.read_csv('Actualizacion-Matrimonios2010-2023.csv')
output_dir = 'imagenes/Graficas'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def grafica_conteo_sexo(df):
    #Cuenta registros por género
    conteo_sexo_persona1 = df['persona1_sexo'].value_counts()
    #Gráfica de barras
    plt.bar(conteo_sexo_persona1.index, conteo_sexo_persona1.values)
    #Cosas Grafica
    plt.xlabel('Género')
    plt.ylabel('Cantidad de Registros')
    plt.title('Cantidad de Registros por Género')
    plt.savefig(os.path.join(output_dir, 'grafica_conteo_sexo.png'))

    #muestra la gráfica
    plt.show()

def grafica_registros_por_mes(df):

    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
    df['mes'] = df['fecha_registro'].dt.strftime('%Y-%m')
    #filtrar por hombres
    hombres_df = df[df['persona1_sexo'] == 'Hombre']
    conteo_nacimientos_hombres = hombres_df['mes'].value_counts().sort_index()
    #filtrar por mujeres
    mujeres_df = df[df['persona1_sexo'] == 'Mujer']
    conteo_nacimientos_mujeres = mujeres_df['mes'].value_counts().sort_index()
    #gráficas de puntos para hombres y mujeres
    plt.figure(figsize=(12, 6))  # Ajusta el tamaño de la figura
    #Gráfica  hombres
    plt.scatter(conteo_nacimientos_hombres.index, conteo_nacimientos_hombres.values, marker='o', s=50, label='Hombres')
    #Gráfica hombres
    plt.scatter(conteo_nacimientos_mujeres.index, conteo_nacimientos_mujeres.values, marker='o', s=50, label='Mujeres')
    plt.xlabel('Mes de Registro')
    plt.ylabel('Cantidad de Registros')
    plt.title('Cantidad de Registros por Mes (Hombres vs. Mujeres)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'grafica_registros_por_mes.png'))
    plt.show()

def grafica_histograma_edad(df):
    plt.figure(figsize=(10, 6))  # Ajustar el tamaño
    #cosas del histograma
    plt.hist(df['persona1_edad'], bins=20, edgecolor='k', alpha=0.7)
    #etiquetas
    plt.xlabel('Edad de la Persona 1')
    plt.ylabel('Cantidad de Personas')
    plt.title('Histograma de Edades de la Persona 1')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'grafica_histograma_edad.png'))
    plt.show()

def grafica_distribucion_registros_por_nacionalidad(df):
    #filtrar por hombres
    hombres_df = df[df['persona1_sexo'] == 'Hombre']
    pivot_table = pd.pivot_table(hombres_df, values='persona1_sexo', index='persona1_nacionalidad', aggfunc='count')
    pivot_table = pivot_table.sort_values(by='persona1_sexo', ascending=False)
    #aplico escala logarítmica a los valores
    pivot_table['log_persona1_sexo'] = pivot_table['persona1_sexo'].apply(lambda x: max(1, x))  # Evitar log(0)
    plt.figure(figsize=(12, 6))
    ax = plt.gca()
    ax.set_yscale('log')
    pivot_table.plot(kind='area', y='log_persona1_sexo', colormap='Set3', legend=False, ax=ax)
    #etiquetas
    plt.xlabel('Nacionalidad')
    plt.ylabel('Cantidad de Hombres (en escala logarítmica)')
    plt.title('Distribución de Hombres por Nacionalidad')
    etiquetas_a_mostrar = 10
    etiquetas = pivot_table.index[::len(pivot_table) // etiquetas_a_mostrar]
    ax.set_xticks(pivot_table.index.get_indexer(etiquetas))
    ax.set_xticklabels(etiquetas, rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'grafica_distribucion_registros_por_nacionalidad.png'))
    plt.show()

def grafica_personas_registro_nacionalidad(df):
    df['fecha'] = pd.to_datetime(df['fecha_registro'])
    persona1_hombre = df[df['persona1_sexo'] == 'Hombre']
    persona1_mujer = df[df['persona1_sexo'] == 'Mujer']
    persona2_hombre = df[df['persona2_sexo'] == 'Hombre']
    persona2_mujer = df[df['persona2_sexo'] == 'Mujer']
    intervalo = '3M'
    persona1_hombre = persona1_hombre.resample(intervalo, on='fecha')['persona1_sexo'].count()
    persona1_mujer = persona1_mujer.resample(intervalo, on='fecha')['persona1_sexo'].count()
    persona2_hombre = persona2_hombre.resample(intervalo, on='fecha')['persona2_sexo'].count()
    persona2_mujer = persona2_mujer.resample(intervalo, on='fecha')['persona2_sexo'].count()
    # Aplicar escala logarítmica a los valores en el eje y
    persona1_hombre = np.log1p(persona1_hombre)
    persona1_mujer = np.log1p(persona1_mujer)
    persona2_hombre = np.log1p(persona2_hombre)
    persona2_mujer = np.log1p(persona2_mujer)
    plt.figure(figsize=(12, 6))
    # Trazar las líneas para cada categoría
    plt.plot(persona1_hombre.index, persona1_hombre.values, label='Persona 1 - Hombre')
    plt.plot(persona1_mujer.index, persona1_mujer.values, label='Persona 1 - Mujer')
    plt.plot(persona2_hombre.index, persona2_hombre.values, label='Persona 2 - Hombre')
    plt.plot(persona2_mujer.index, persona2_mujer.values, label='Persona 2 - Mujer')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad (en escala Logarítmica)')
    plt.title('Géneros de Personas (Agrupado por cada 3 Meses)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'grafica_personas_registro_nacionalidad.png'))
    plt.show()



# Llamar a las funciones con tu DataFrame 'df'
grafica_conteo_sexo(df)
grafica_registros_por_mes(df)
grafica_histograma_edad(df)
grafica_distribucion_registros_por_nacionalidad(df)
grafica_personas_registro_nacionalidad(df)


