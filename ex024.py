a = str(input('Escreva uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na frase.'.format(a.count('a')))
print('A letra A apareceu primeiro na posição {}'.format(a.find('a')+1))
print('A ultima letra A aparece na posicão {}'.format(a.rfind('a')+1))