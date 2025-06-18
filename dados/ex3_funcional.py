
# não é viável otimizar exaustivamente
import numpy as np
import pandas as pd
from itertools import combinations, permutations

layout = np.array([
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"],
    ["I", "J", "K", "L"]
])
# m = "linhas"
# n = "colunas"
m, n = layout.shape
l = 10 # largura ("altura da linha")
c = 5 # comprimento ("largura da coluna")

def formatar_layout(l, m=m, n=n):
    return np.array(l).reshape((m, n))

setores = layout.flatten()
pares = list(combinations(setores, 2)) # cuidado
# permutacoes = list(permutations(setores)) # MUITO CUIDADO - custo computacional (memória)
# obs: cada item da lista acima será uma tuple 1d -> transformar em array e fazer reshape
# permutacoes = [np.array(l).reshape((m, n)) for l in permutations(setores)]

custos = pd.read_csv('dados/custos9.csv', header=0, index_col=0)
movimentacoes = pd.read_csv('dados/movimentacoes9.csv', header=0, index_col=0)
custos_diarios = custos * movimentacoes
