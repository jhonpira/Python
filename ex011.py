a = float(input('Qual o salário do funcionário: R$'))
b = a*15/100
c = a + b
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(a, c))