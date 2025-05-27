# %%
import numpy as np

# %% dados
layout = [
    ['A', 'B'],
    ['C', 'D'],
    ['E', 'F']
]

m = 3 # "linhas"
n = 2 # "colunas"
l = 10
c = 5

# %% funcoes
def dist_ind(s1, s2, l=l, c=c):
    # ex: s1 = (0, 0), s2 = (0, 1)
    dx = l * abs(s2[1] - s1[1])
    dy = c * abs(s2[0] - s1[0])

    result = dx + dy

    return result

def dist_dir(s1, s2, l=l, c=c):
    # ex: s1 = (0, 0), s2 = (0, 1)
    dx = l * abs(s2[1] - s1[1])
    dy = c * abs(s2[0] - s1[0])

    result = np.sqrt(dx**2 + dy**2)

    return result

s1, s2 = (0, 0), (1, 1)

print(f'dist_ind: {dist_ind(s1, s2):.2f}')
print(f'dist_dir: {dist_dir(s1, s2):.2f}')

# %%
