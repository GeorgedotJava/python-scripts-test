'''
3)Faça um programa para ler um numero inteiro entre 1 e 10 , 
mande mensagem de erro caso o usuário digite um numero inadequado. 
Assim que o usuário digitar um numero valido imprimir a tabuada 
de multiplicação desse numero.'''


cont = 0
while cont < 6:
    n = int(input('Informe 1 numero entre 1 e 10 '))
    print()
    if n >= 1 and n <= 10:
        for i in range(1, 11):            
            print(f'{n} x {i} = {i*n}')  
        break 
    else:
        print('Erro, o programa nao aceita numeros fora do intervalo entre 1 e 10, tente novamente')                
        False
cont += 1