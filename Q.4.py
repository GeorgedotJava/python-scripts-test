
cont = 0
soma = 0
while cont < 6:
    n = int(input('Informe 1 numero entre 1 e 100 '))
    print()
    if n >= 1 and n <= 100:
        for i in range(1, n+1):            
             soma += i
        print(f'soma dos inteiros entre 1 e {n} = {soma}')
        break 
    else:
        print('Erro, o programa nao aceita numeros fora do intervalo entre 1 e 100, tente novamente')                
        False
cont += 1