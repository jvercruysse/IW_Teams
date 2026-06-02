import pandas as pd
stereig = pd.read_csv('stereigenschappen.csv', sep=';')

# VRAAG DE KOLOMMEN MET DE MASSAS EN DE TEMPERATUREN OP
mass = stereig['Massa']
temp = stereig['Temp']

print(mass)
print(temp)
