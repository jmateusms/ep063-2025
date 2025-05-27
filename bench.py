import time

# %%
def quadrado(x):
    return x * x

# %%
n = 10000000
fator = n/100

reps = 20
tempos = []

for i in range(reps):
    resultados = []

    start = time.perf_counter()
    for i in range(n):
        resultados.append(quadrado(i / fator))
    end = time.perf_counter()

    tempo = end - start
    tempos.append(tempo)

    print(f'tempo: {tempo:.10f}s')

print(tempos)
