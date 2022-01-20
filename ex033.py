print('-=-'*14)
print('Analisador de triângulos...')
print('-=-'*14)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR triãngulo!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo')