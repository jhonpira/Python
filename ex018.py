import random


a = str(input('Primeiro nome: '))
b = str(input('Segundo nome: '))
c = str(input('Terceiro nome: '))
d = str(input('Quarto nome: '))
nomes = [a, b, c, d]
random.shuffle(nomes)
print('A ordem de apresentação será\n{}'.format(nomes))