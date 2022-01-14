a = int(input('Quantos dias alugados? '))
b = float(input('Quantos km rodados? '))
c = b * 0.15
d = a * 60
e = d + c
print('O total a pagar é R${:.2f}'.format(e))