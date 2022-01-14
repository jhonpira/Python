a = float(input('Uma distância em metros: '))
b = a/1000
c = a/100
d = a/10
e = a*10
f = a*100
g = a*1000
print('A medida de {} m corresponde a \n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(a,b,c,d,e,f,g))
