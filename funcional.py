# %%
import time
import numpy as np
import pandas as pd
from tqdm import tqdm
from itertools import combinations, permutations

# %% dados
# import dados.ex1_funcional as ex # layout 2x3, 6 setores
# import dados.ex2_funcional as ex # layout 3x3, 9 setores – demora alguns minutos para otimizar exaustivamente
import dados.ex3_funcional as ex # layout 3x4, 12 setores – não é viável otimizar exaustivamente

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

def endereco(setor, layout=ex.layout):
    """
    Retorna o endereço (tuple) do setor (string) dentro do layout (array 2d).
    """
    i, j = np.where(layout == setor)
    result = (i[0], j[0])

    return result

def dist_ind(s1, s2, layout=ex.layout, l=ex.l, c=ex.c):
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

def dist_dir(s1, s2, layout=ex.layout, l=ex.l, c=ex.c):
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

# distancia total/custos totais
def get_df_ind(layout, l=ex.l, c=ex.c):
    """
    Retorna um DataFrame contendo as distâncias entre todos os pares de setores de um layout, considerando o layout de entrada e as dimensões informadas. Utiliza medidas indiretas.

    Entradas:
    - `layout`: array 2d contendo o posicionamento dos setores.
    - `l`, `c`: dimensões. largura (*"altura da linha") e comprimento (*"largura da coluna")
    *considerando um formato de matriz.
    """
    df_ind = pd.DataFrame(np.nan, index=range(len(ex.setores)), columns=range(len(ex.setores)))
    df_ind.index = ex.setores
    df_ind.columns = ex.setores

    for par in ex.pares:
        df_ind.loc[par[0], par[1]] = dist_ind(par[0], par[1], layout=layout, l=l, c=c)
    
    return df_ind

def get_df_dir(layout, l=ex.l, c=ex.c):
    """
    Retorna um DataFrame contendo as distâncias entre todos os pares de setores de um layout, considerando o layout de entrada e as dimensões informadas. Utiliza medidas diretas.

    Entradas:
    - `layout`: array 2d contendo o posicionamento dos setores.
    - `l`, `c`: dimensões. largura (*"altura da linha") e comprimento (*"largura da coluna")
    *considerando um formato de matriz.
    """
    df_dir = pd.DataFrame(np.nan, index=range(len(ex.setores)), columns=range(len(ex.setores)))
    df_dir.index = ex.setores
    df_dir.columns = ex.setores

    for par in ex.pares:
        df_dir.loc[par[0], par[1]] = dist_dir(par[0], par[1], layout=layout, l=l, c=c)
    
    return df_dir

# df_ind = get_df_ind(layout)
# df_dir = get_df_dir(layout)

# print(df_ind.sum().sum())
# print(df_dir.sum().sum())

def dist_total_ind(layout, mov=ex.movimentacoes, l=ex.l, c=ex.c):
    """
    Retorna a distância indireta total percorrida, considerando o layout informado e o número movimentações entre os pares de setores.

    Entradas:
    - `layout`: array 2d contendo o posicionamento dos setores.
    - `mov`: DataFrame com as movimentações entre os pares de setores.
    - `l`, `c`: dimensões. largura (*"altura da linha") e comprimento (*"largura da coluna")
    *considerando um formato de matriz.
    """
    result = (mov * get_df_ind(layout, l, c)).sum().sum()

    return result

def dist_total_dir(layout, mov=ex.movimentacoes, l=ex.l, c=ex.c):
    """
    Retorna a distância direta total percorrida, considerando o layout informado e o número movimentações entre os pares de setores.

    Entradas:
    - `layout`: array 2d contendo o posicionamento dos setores.
    - `mov`: DataFrame com as movimentações entre os pares de setores.
    - `l`, `c`: dimensões. largura (*"altura da linha") e comprimento (*"largura da coluna")
    *considerando um formato de matriz.
    """
    result = (mov * get_df_dir(layout, l, c)).sum().sum()

    return result

def custos_totais_ind(layout, custos=ex.custos_diarios, l=ex.l, c=ex.c):
    """
    Retorna os custos totais, considerando distâncias indiretas, utilizando o layout informado e os custos entre os pares de setores.

    Entradas:
    - `layout`: array 2d contendo o posicionamento dos setores.
    - `custos`: DataFrame com os custos entre os pares de setores.
    - `l`, `c`: dimensões. largura (*"altura da linha") e comprimento (*"largura da coluna")
    *considerando um formato de matriz.
    """
    result = (custos * get_df_ind(layout, l, c)).sum().sum()

    return result

def custos_totais_dir(layout, custos=ex.custos_diarios, l=ex.l, c=ex.c):
    """
    Retorna os custos totais, considerando distâncias diretas, utilizando o layout informado e os custos entre os pares de setores.

    Entradas:
    - `layout`: array 2d contendo o posicionamento dos setores.
    - `custos`: DataFrame com os custos entre os pares de setores.
    - `l`, `c`: dimensões. largura (*"altura da linha") e comprimento (*"largura da coluna")
    *considerando um formato de matriz.
    """
    result = (custos * get_df_dir(layout, l, c)).sum().sum()

    return result

# %% otimizar
# ATENÇÃO - o trecho abaixo pode ser muito custoso - solução exaustiva
if __name__ == '__main__':
    menor_custo_ind = np.inf
    menor_custo_dir = np.inf
    melhor_layout_ind = []
    melhor_layout_dir = []

    tol = 1e-5
    tempo_max_segundos = 600
    tempo_max_atingido = False

    start = time.perf_counter()

    for layout in tqdm(ex.permutacoes):
        # layout = np.array(layout).reshape((m, n))
        custo_temp = custos_totais_ind(layout)
        if custo_temp < menor_custo_ind:
            menor_custo_ind = custo_temp
            melhor_layout_ind = [layout]
        elif abs(custo_temp - menor_custo_ind) < tol:
            melhor_layout_ind.append(layout)
        
        custo_temp = custos_totais_dir(layout)
        if custo_temp < menor_custo_dir:
            menor_custo_dir = custo_temp
            melhor_layout_dir = [layout]
        elif abs(custo_temp - menor_custo_dir) < tol:
            melhor_layout_dir.append(layout)
        
        tempo_atual = time.perf_counter() - start
        if tempo_atual > 300:
            tempo_max_atingido = True
            break

    duration = time.perf_counter() - start

    print('Melhor layout (distâncias indiretas):')
    for l in melhor_layout_ind:
        print(l)
    print('Custos totais:', menor_custo_ind)
    print('')
    print('Melhor layout (distâncias diretas):')
    for l in melhor_layout_dir:
        print(l)
    print('Custos totais:', menor_custo_dir)

    print(f'\nTempo de execução: {duration:.5f}s')
    if tempo_max_atingido:
        print('Tempo máximo de execução atingido. A solução pode não ser ótima.')
