numero = int(input("Digite um número inteiro: "))
numeroMaior = 0
soma = 0
contador = 0 
while (numero !=0):
    for i in range (1, numero): 
        if (numero > i):
            numeroMaior = numero
        soma = numero+ numeroMaior
    numero = int(input("Digite um número inteiro: "))
print(f'Maior número {numeroMaior} \n Soma: {soma} /nMédia dos números digitados {soma}')

        

    
