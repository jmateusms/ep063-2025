# exemplo básico. a fazer/sugestões:
# fazer plot da rede de instalações + resultado em cor diferente
# definir como plotar quando houver 2 X ou 2 Y diferentes
# otimizar loops para evitar iterações desnecessárias
# deixar mais intuitivo/simples quando há uma ou duas medianas
# reduzir uso de memória (evitando as cópias dos dados)

# %% importar pacotes
import pandas as pd

# %% importar dados
# dados = pd.read_csv('dados/loc5.csv', header=0)
dados = pd.read_csv('dados/loc6.csv', header=0)
instalacoes = dados['Localização']
volumes = dados['Volume']
X = dados['X']
Y = dados['Y']

dadosX = dados.copy()
dadosX.sort_values(by='X', inplace=True)

dadosY = dados.copy()
dadosY.sort_values(by='Y', inplace=True)

# %% aplicar o método
mediana1 = sum(volumes) / 2
if mediana1 % 2 == 0:
    mediana2 = mediana1 + 1
else:
    mediana2 = mediana1

soma = 0
x1 = x2 = None

for i in range(len(dadosX)):
    soma += dadosX.iloc[i]['Volume']
    if soma > mediana1 and x1 is None:
        x1 = dadosX.iloc[i]['X']
    if soma > mediana2 and x2 is None:
        x2 = dadosX.iloc[i]['X']

soma = 0
y1 = y2 = None

for i in range(len(dadosY)):
    soma += dadosY.iloc[i]['Volume']
    if soma > mediana1 and y1 is None:
        y1 = dadosY.iloc[i]['Y']
    if soma > mediana2 and y2 is None:
        y2 = dadosY.iloc[i]['Y']

print(x1, x2, y1, y2)
