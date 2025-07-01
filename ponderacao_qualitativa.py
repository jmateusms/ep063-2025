# %% importar pacotes
import numpy as np
import pandas as pd

# %% importar dados
# dados = pd.read_csv('dados/loc1.csv', header=0)
dados = pd.read_csv('dados/loc2.csv', header=0)
pesos = dados['Peso'].copy()
del(dados['Peso'])
instalacoes = dados.columns[1:]

# %% aplicar o metodo
somas = []

for inst in instalacoes:
    print(f'Instalação {inst}')
    somas.append(sum(pesos * dados[inst]))
    print(somas[-1])

melhor_i = np.argmax(somas)
melhor_inst = instalacoes[melhor_i]

print(f'Instalação escolhida: {melhor_inst} com pontuação {somas[melhor_i]}')
