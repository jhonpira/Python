a = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(a))

if a<=200:
    print('E o preço da passagem será de R${:.2f}'.format(a*0.50))
else:
    print('E o preço da passagem será de R${:.2f}'.format(a*0.45))    