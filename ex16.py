import math
a = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem SENO de {:.2f}'.format(a, math.sin(math.radians(a))))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(a, math.cos(math.radians(a))))
print('O ângulo de {} tem tangente de {:.2f}'.format(a, math.tan(math.radians(a))))