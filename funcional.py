# %%
import numpy as np
import pandas as pd
from itertools import combinations

# %% dados
layout = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
]
layout = np.array(layout)
setores = layout.flatten()
pares = list(combinations(setores, 2)) # cuidado

m = 2 # "linhas"
n = 3 # "colunas"
l = 10 # largura ("altura da linha")
c = 5 # comprimento ("largura da coluna")

custos = pd.read_csv('dados/custos.csv', index_col=0)

# %% funcoes
# listar enderecos
def listar_enderecos(layout):
    """
    Função que lista os endereços, em tuple, dos setores (strings) que estão presentes no layout.

    Entrada: lista de listas ou array 2d.
    Saída: dicionário.
    """
    enderecos = dict()

    for i, linha in enumerate(layout):
        for j, setor in enumerate(linha):
            enderecos[setor] = (i, j)
    
    # forma alternativa
    # for i in range(len(layout)):
    #     for j in range(len(layout[i])):
    #         enderecos[layout[i, j]] = (i, j)
    
    return enderecos

# print(listar_enderecos(layout))

def endereco(setor, layout=layout):
    """
    Retorna o endereço (tuple) do setor (string) dentro do layout (array 2d).
    """
    i, j = np.where(layout == setor)
    result = (i[0], j[0])

    return result

def dist_ind(s1, s2, layout=layout, l=l, c=c):
    """
    Calcula a distância indireta entre dois setores.

    Entradas:
    - `s1`, `s2`: tuple ou string dos setores de origem e destino.
    - `layout`: array 2d do layout
    - `l`, `c`: dimensões. largura ("altura da linha") e comprimento ("largura da coluna").

    ex: s1 = (0, 0), s2 = (0, 1)
    """
    if type(s1) in [str, np.str_]:
        s1 = endereco(s1, layout)
    if type(s2) in [str, np.str_]:
        s2 = endereco(s2, layout)

    di = c * abs(s2[1] - s1[1])
    dj = l * abs(s2[0] - s1[0])

    result = di + dj

    return result

def dist_dir(s1, s2, layout=layout, l=l, c=c):
    """
    Calcula a distância indireta entre dois setores.

    Entradas:
    - `s1`, `s2`: tuple ou string dos setores de origem e destino.
    - `layout`: array 2d do layout
    - `l`, `c`: dimensões. largura ("altura da linha") e comprimento ("largura da coluna").
    
    ex: s1 = (0, 0), s2 = (0, 1)
    """
    if type(s1) in [str, np.str_]:
        s1 = endereco(s1, layout)
    if type(s2) in [str, np.str_]:
        s2 = endereco(s2, layout)

    di = c * abs(s2[1] - s1[1])
    dj = l * abs(s2[0] - s1[0])

    result = np.sqrt(di**2 + dj**2)

    return result

# s1, s2 = (0, 0), (1, 2)
# print(f'dist_ind: {dist_ind(s1, s2):.2f}')
# print(f'dist_dir: {dist_dir(s1, s2):.2f}')

# s1, s2 = 'A', 'F'
# print(f'dist_ind: {dist_ind(s1, s2):.2f}')
# print(f'dist_dir: {dist_dir(s1, s2):.2f}')

# %% distancia total
l = 7
c = 5
def dist_total_ind(layout, l=l, c=c, pares=pares):
    result = 0

    for par in pares:
        result = result + dist_ind(par[0], par[1], layout=layout, l=l, c=c)
    
    return result

def dist_total_dir(layout, l=l, c=c, pares=pares):
    result = 0

    for par in pares:
        result = result + dist_dir(par[0], par[1], layout=layout, l=l, c=c)
    
    return result

# print(dist_total_ind(layout))
# print(dist_total_dir(layout))


def get_df_ind(layout, l=l, c=c):
    df_ind = pd.DataFrame(np.nan, index=range(len(setores)), columns=range(len(setores)))
    df_ind.index = setores
    df_ind.columns = setores

    for par in pares:
        df_ind.loc[par[0], par[1]] = dist_ind(par[0], par[1], layout=layout, l=l, c=c)
    
    return df_ind

def get_df_dir(layout, l=l, c=c):
    df_dir = pd.DataFrame(np.nan, index=range(len(setores)), columns=range(len(setores)))
    df_dir.index = setores
    df_dir.columns = setores

    for par in pares:
        df_dir.loc[par[0], par[1]] = dist_dir(par[0], par[1], layout=layout, l=l, c=c)
    
    return df_dir

# df_ind = get_df_ind(layout)
# df_dir = get_df_dir(layout)

# print(df_ind.sum().sum())
# print(df_dir.sum().sum())

# %% testar layouts
layout = np.array([
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
])

print('##### Custos totais ####')

print('### Layout 1 ###')
c1 = (custos * get_df_ind(layout)).sum().sum()
c2 = (custos * get_df_dir(layout)).sum().sum()
print('distância indireta:', round(c1, 2), sep='\n')
print('distância direta:', round(c2, 2), sep='\n')
print('')

layout = np.array([
    ['A', 'B', 'E'],
    ['F', 'C', 'D'],
])

print('### Layout 2 ###')
c1 = (custos * get_df_ind(layout)).sum().sum()
c2 = (custos * get_df_dir(layout)).sum().sum()
print('distância indireta:', round(c1, 2), sep='\n')
print('distância direta:', round(c2, 2), sep='\n')
print('')

layout = np.array([
    ['F', 'E', 'C'],
    ['D', 'B', 'A'],
])

print('### Layout 1 ###')
c1 = (custos * get_df_ind(layout)).sum().sum()
c2 = (custos * get_df_dir(layout)).sum().sum()
print('distância indireta:', round(c1, 2), sep='\n')
print('distância direta:', round(c2, 2), sep='\n')
