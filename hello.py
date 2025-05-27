# %% imports
import math
from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %% hello, world
print('hello, world!') # comentario

x = 'abc'
y = 'def'

print(2*x + y)

# %% types
my_bool = True # or False
my_int = 10
my_float = 10.0
my_str = '10'
my_fstr = f'int: {my_int}, float: {my_float}'
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {10, 20, 30}
my_dict = {
    'key': 'value',
    'a': 10,
    'b': 20,
    'c': 30
}

print(type(my_int))
print(type(my_float))
print(type(my_str))
print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dict))

# %% operations
basic_operations = 10 + 20 / 3 - 2 * 5
power_operator = 2 ** 3 # 8
square_root = sqrt(2) # or math.sqrt(2) - depende de como foi importado
int_div = 2 // 5 # div inteira
int_div_remain = 2 % 5 # resto

# logic operations
a = True
b = False

print(f'a: {a}')
print(f'b: {b}')
print(f'not a: {not a}')
print(f'not b: {not b}')
print(f'a and b: {a and b}')
print(f'a or b: {a or b}')

# %% control flow tools
# if statement
a = False
b = False
if a:
    print('a is True')
elif b:
    print('a is False, but b is True')
else:
    print('a and b are False')

nota = 10
if nota >= 7:
    print('passou por media')
elif nota >= 3:
    print('recuperacao')
else:
    print('reprovou')


print('test')

# for loop
for i in range(10):
    print(i)

for i in [10, 20, 30]:
    print(i)

for i in range(5):
    for j in range(3):
        print(f'{i}{j}')

minhas_notas = [10, 7, 5, 3.5, 2.5, 9, 9.5, 6, 6.5]
for i, nota in enumerate(minhas_notas):
    if nota >= 7:
        print(f'aluno {i + 1} passou por media')
    elif nota >= 3:
        print(f'aluno {i + 1} recuperacao')
    else:
        print(f'aluno {i + 1} reprovou')

# %% generate names
# from faker import Faker
# fake = Faker('pt_BR')
# nomes = []
# for i in range(len(notas)):
#     nomes.append(fake.name())
meus_nomes = [
    'Ana Luiza Correia',
    'Eloah Peixoto',
    'Gabriela Cavalcante',
    'Kamilly Araújo',
    'Dr. Eduardo Montenegro',
    'Vinícius Vieira',
    'Ana Beatriz Sousa',
    'Caio Montenegro',
    'Isabelly Moura'
]

# %% functions p1
def avaliar_notas(notas):
    for i, nota in enumerate(notas):
        if nota >= 7:
            print(f'aluno {i + 1} passou por media')
        elif nota >= 3:
            print(f'aluno {i + 1} recuperacao')
        else:
            print(f'aluno {i + 1} reprovou')

avaliar_notas(minhas_notas)

# %% functions p2
def avaliar_alunos(notas, nomes):
    for nome, nota in zip(nomes, notas):
        if nota >= 7:
            print(f'aluno {nome} passou por media')
        elif nota >= 3:
            print(f'aluno {nome} recuperacao')
        else:
            print(f'aluno {nome} reprovou')

avaliar_alunos(minhas_notas, meus_nomes)

# %% functions p3
def avaliar(notas, nomes=None):
    if nomes is None:
        nomes = list(range(1, len(notas) + 1))
    
    for nome, nota in zip(nomes, notas):
        if nota >= 7:
            print(f'aluno {nome} passou por media')
        elif nota >= 3:
            print(f'aluno {nome} recuperacao')
        else:
            print(f'aluno {nome} reprovou')

print('sem nomes:')
avaliar(minhas_notas)
print('\ncom nomes:')
avaliar(minhas_notas, meus_nomes)

# %% numpy
my_list = [10, 20, 30]
my_array = np.array(my_list)

print(my_array)
print(type(my_array))

print(2 * my_list)
print(2 * my_array + 5)

array1 = np.array([1.5, 2, 4.3, 2.1])
array2 = np.array([2.2, 3.5, 2, 5])

print(array1 + array2)

# %% plots
x = np.linspace(0, 10, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.show()

x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
plt.scatter(x, y)
plt.show()

plt.hist(x)
plt.show()

plt.hist(y)
plt.show()

bins = np.linspace(-4, 4, 15)
plt.hist(x, bins=bins, color='red', alpha=.5, label='X', density=True)
plt.hist(y, bins=bins, color='blue', alpha=.5, label='Y', density=True)
plt.legend()
plt.show()

# %%
