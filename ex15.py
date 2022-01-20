import math 
a = float(input('Comprimento cateto oposto: '))
b = float(input('Comprimento cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(math.hypot(a,b)))