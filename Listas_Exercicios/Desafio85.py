listaUnica = []
listaPares = []
listaImpares = []
for i in range (0,7):
    numero = int(input("Digite o número: "))
    if numero % 2 == 0:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)

#Ordenando as listas de impar e par em ordem crescente
listaPares.sort()
listaImpares.sort()


#Criando uma única lista composta com as duas listas impar e par
listaUnica.append(listaPares[:]) 
listaUnica.append(listaImpares[:]) 
listaPares.clear()
listaImpares.clear()

print(listaUnica)

   
#Resolução do professor

num = [[], []]
valor = 0 
for i in range(1,8):
    valor = int(input(f"Digite o {i}º valor:"))
    if valor % 2 == 0:
        num[0].append(valor)
    else: 
        num[1].append(valor)


print(f"Valores: {num}")
num[0].sort()
num[1].sort()
print(f"Valores pares: {num[0]}")
print(f"Valores impares: {num[1]}")