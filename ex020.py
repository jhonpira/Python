from ntpath import join
from tkinter import N


nome = input('Seu nome completo: ') #.stip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é',nome.upper())
print('Seu nome em minúsculas é',nome.lower())
print('Seu nome tem ao todo',len(''.join(nome.split())),'letras') #len(nome)- nome.count(' ')
a = nome.split()
print('Seu primeiro nome é', a[0], 'e ele tem',len(a [0]),'letras') 