# a fazer/sugestões
# fazer plot da rede de instalações + CG em cor diferente
# [desafio] para casos com coordenadas reais, exibir os pontos sobre o mapa da região
# [desafio] permitir que o usuário entre com as localizações usando endereços
# dica: sistemas GIS

# %% importar pacotes
import pandas as pd

# %% importar dados
# dados = pd.read_csv('dados/loc5.csv', header=0)
dados = pd.read_csv('dados/loc6.csv', header=0)
instalacoes = dados['Localização']
volumes = dados['Volume']
X = dados['X']
Y = dados['Y']

# %% aplicar o método
X_CG = sum(X * volumes) / sum(volumes)
Y_CG = sum(Y * volumes) / sum(volumes)

print((X_CG, Y_CG))
