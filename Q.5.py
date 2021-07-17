
cont = 0
soma = 0
while cont < 6:
    n = int(input('Informe 1 numero entre 1 e 1000 '))
    print()
    if n >= 1 and n <= 1000:
        print(f'Imprimindo numeros primos entre 1 e {n}')
        for x in range(2, n+1):
            cont = 0
            for y in range(1, x + 1):
                if x%y==0:
                    cont += 1
            if cont <= 2:                
                print(x)
        break 
    else:
        print('Erro, o programa nao aceita numeros fora do intervalo entre 1 e 1000, tente novamente')                
        False
cont += 1