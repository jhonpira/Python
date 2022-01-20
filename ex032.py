from re import A


sal = float(input('Qual o salário do funcionário? R$'))
a = sal *10/100
b = sal *15/100
if sal > 1250.00:
    print('Quem ganhava R${:.2f}, passou a ganhar R${:.2f} agora'.format(sal, sal + a))
else:
    print('Quem ganhava R${:.2f}, passou a ganhar R${:.2f} agora'.format(sal, sal + b))