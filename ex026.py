from time import sleep
from turtle import color
from termcolor import colored
import random
print(colored('-=-'*18, 'yellow'))
print(colored('Vou pensar em um número entre 0 e 5. Tente adivinhar...', 'blue'))
print(colored('-=-'*18, 'yellow'))
a =(int(input('Em que numero eu pensei? ')))
print(colored('PROCESSANDO...', 'magenta'))
sleep(3)
b = [0,1,2,3,4,5]
c = random.choice(b) #choice ou radint (0,5)
if a == c:
    print(colored('PARABÉNS! Você conseguiu me vencer!','yellow'))
else:
    print(colored('GANHEI! Eu pensei no numero {} e não no {}!'.format(c,a),'red') )  