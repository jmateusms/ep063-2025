# exemplo inacabado - a fazer:
# automatizar a comparação entre a lista de instalações (sempre comparando 2 a 2)
# exibir o resultado indicando qual a melhor de todas (é preciso definir um critério para isso)

# %% importar pacotes
import numpy as np
import pandas as pd
from itertools import combinations

# %% importar dados
# dados = pd.read_csv('dados/loc1.csv', header=0)
# dados = pd.read_csv('dados/loc2.csv', header=0)
# dados = pd.read_csv('dados/loc3.csv', header=0)
dados = pd.read_csv('dados/loc4.csv', header=0)
pesos = dados['Peso'].copy()
del(dados['Peso'])
instalacoes = dados.columns[1:]

# %% aplicar o metodo
# A vs B
CM_AB = 1

for i in range(len(pesos)):
    CM_AB *= (dados['A'][i] / dados['B'][i]) ** pesos[i]

print(CM_AB)

# A vs C
CM_AC = 1

for i in range(len(pesos)):
    CM_AC *= (dados['A'][i] / dados['C'][i]) ** pesos[i]

print(CM_AC)

# B vs C
CM_BC = 1

for i in range(len(pesos)):
    CM_BC *= (dados['B'][i] / dados['C'][i]) ** pesos[i]

print(CM_BC)
