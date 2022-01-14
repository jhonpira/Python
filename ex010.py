a = float(input('Qual o preço do produto: R$'))
b = a * 5/100
c = a - b
print('O produto que custava R${:.2f}, na promocão com desconto de 5% vai custar R${:.2f}'.format(a, c))