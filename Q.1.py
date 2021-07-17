import math
print('Programa para calculo das raizes de uma equacao de 2 grau')
print('Por favor informe os coeficientes da equacao')
a = int(input('a:'))
print()
b = int(input('b:'))
print()
c = int(input('c:'))
print()
delta = math.pow(b, 2) - 4 * (a * c)

if delta < 0:
    print(f'Delta = {delta}')
    print('Nao existem raizes reais para essa equacao')
else:
    x1 = ((-b) + math.sqrt(delta))/(2*a)
    x2 = ((-b) - math.sqrt(delta))/(2*a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')