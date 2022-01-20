from typing import final


a = str(input('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é {}'.format(a[0]))
print('Seu ultimo nome é {}'.format(a[len(a)-1]))
