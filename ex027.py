from termcolor import colored
a = float(input('Qual é a velocidade atual do carro? '))
if a<=80:
    print(colored('Tenha um bom dia! Dirija com segurança!','yellow'))
else: 
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h\nVocê deve pagar uma multa de\33[m \033[33mR${}!'.format((a-80)*7),)