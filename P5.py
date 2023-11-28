import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
#import matplotlib.pyplot as plt

df = pd.read_csv('Actualizacion-Matrimonios2010-2023.csv', nrows=22000)

#modelo de ANOVA
modelo = ols('persona1_edad ~ fecha_registro', data=df).fit()

#Anova
anova_table = sm.stats.anova_lm(modelo, typ=2)

print("Tabla de ANOVA:")
print(anova_table)
