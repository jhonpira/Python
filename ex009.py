a = float(input('Largura da parede: '))
b = float(input('Altura da parede: '))
c = a*b
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(a, b, c))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(c/2))