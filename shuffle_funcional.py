# %% importar pacotes e dados
import numpy as np
import time
from random import shuffle
from tqdm import tqdm
from funcional import custos_totais_ind, custos_totais_dir, ex
# TODO: melhorar a forma de escolha do exemplo
# atual: selecionar exemplo no arquivo `funcional.py`

# %% funções
def gerar_solucao(setores=ex.setores):
    solucao = setores.copy()
    shuffle(solucao)
    solucao = ex.formatar_layout(solucao)

    return solucao

def checar_solucao_duplicada(solucao, lista):
    solucao_duplicada = np.any(np.all(solucao == lista, axis=1))
    
    return solucao_duplicada

# %% solucao inicial: testar randomicamente
if __name__ == '__main__':
    menor_custo_ind = np.inf
    menor_custo_dir = np.inf
    melhor_layout_ind = []
    melhor_layout_dir = []

    tol = 1e-5
    tempo_max_segundos = 5

    solucoes_testadas = 0
    intervalo_progresso = 1000

    progress = tqdm(total=tempo_max_segundos, bar_format='{n:.3f}s')

    start = time.perf_counter()

    tempo_atual = 0
    tempo_anterior = 0

    while tempo_atual < tempo_max_segundos:
        layout = gerar_solucao()

        custo_temp = custos_totais_ind(layout)
        if custo_temp < menor_custo_ind:
            menor_custo_ind = custo_temp
            melhor_layout_ind = [layout]
        elif abs(custo_temp - menor_custo_ind) < tol:
            if not checar_solucao_duplicada(layout, melhor_layout_ind):
                melhor_layout_ind.append(layout)
        
        custo_temp = custos_totais_dir(layout)
        if custo_temp < menor_custo_dir:
            menor_custo_dir = custo_temp
            melhor_layout_dir = [layout]
        elif abs(custo_temp - menor_custo_dir) < tol:
            if not checar_solucao_duplicada(layout, melhor_layout_dir):
                melhor_layout_dir.append(layout)
        
        solucoes_testadas += 1

        if solucoes_testadas % intervalo_progresso == 0:
            tempo_atual = time.perf_counter() - start
            progress.update(tempo_atual - tempo_anterior)
            tempo_anterior = tempo_atual
    
    print('Melhor layout (distâncias indiretas):')
    for l in melhor_layout_ind:
        print(l)
    print('Custos totais:', menor_custo_ind)
    print('')
    print('Melhor layout (distâncias diretas):')
    for l in melhor_layout_dir:
        print(l)
    print('Custos totais:', menor_custo_dir)

    print('Soluções testadas:', solucoes_testadas)

    print(f'\nTempo de execução: {time.perf_counter() - start:.5f}s')
