

# 2) Faça um programa para ler dois valores inteiros positivos entre 1 e 100 . Faça o seu
# programa de uma forma funcione bem, não importa a ordem que os números são
# informados, podendo o usuário digitar primeiro o menor e depois o maior , ou o
# contrario e mesmo assim seu programa deve funcionar. Se o usuário digitar um valor
# negativo mandar mensagem de erro e pedir novo valor, assim que o usuário digitar
# valores validos, informar o somatório dos números impares e o somatório dos números
# pares dentro desse intervalo.

cont = 0
soma_par = 0
soma_impar = 0
while cont < 8:
    print('Informe 2 numeros entre 1 e 100 ')
    n1 = int(input())
    n2 = int(input())
    if n1 >= 1 and n1 <= 100 and n2 >= 1 and n2 <= 100:
        if n1 > n2:
            n1, n2 = n2, n1
            for i in range(n1, n2+1):
                if i % 2 == 0:                    
                    soma_par += i                    
                else:                    
                    soma_impar += i                    
        else:
            for i in range(n1, n2+1):
                if i % 2 == 0:                    
                    soma_par += i                
                else:                    
                    soma_impar += i                
        break 
    else:
        print('Erro, o programa nao aceita numeros negativos, tente novamente')                
        False
    # print()
    
cont += 1
print(f'somatorio dos numeros pares entre {n1} e {n2} = {soma_par}')
print(f'somatorio dos numeros impares entre {n1} e {n2} = {soma_impar}')