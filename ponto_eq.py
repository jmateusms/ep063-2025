# exemplo de estrutura do script

# %% dados
...

# %% funções
def lucro(q, cf, cv, pv):
    return - cf + q * (pv - cv)

def ponto_eq(cf, cv, pv):
    return cf / (pv - cv)

# %% aplicar o método
