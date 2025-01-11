from time import sleep
for i in range (10, -1, -1):
    print(i)
    #sleep (0.5)
print("BUMM")

for i in range (1,11):
    print(i, end =" ")

soma = 0
contador = 0
for i in range (1, 501, 2):   #se fizer o interval de 1,10 pulando no passo 2 ent vai ficar (1, 3, 5) ou seja números ìmpar
    if i % 3 ==0:
        soma += i
        contador += 1
print(f"soma: {soma} quantos números impares são divísiveis por 3?: {contador}")

for i in range (1, 10, 2):
    print(i, end=" ")

lista = []
for i in range (1, 51):
    if i % 2 == 0:
        lista.append(i) 
print ("Números pares entre 1  e 50:", lista)

soma = 0
for i in range (1, 501, 2):
    if i % 3 == 0:
        soma += i
print(soma) 

num = int(input("Digite um número: "))
for i in range (1,11):
    print (f"{num} * {i} = {num*i}")

num = 0 
soma = 0
for i in range (1, 3):
    num = int(input("Digite um número inteiro: "))
    if num%2 == 0:
        soma += num
print(soma)

num = int(input("Digite o primeiro termo: "))
PA = int(input("Digite a progressão (em número): "))
decimo = num + (10 - 1) * PA
for i in range (num, decimo+1, PA):
    print(i, end = " ")

contador = 0 
num = int(input("Digite um número: "))
for i in range (1, num+1):
    if num % i == 0: 
        contador += 1
print(f"O número {num} foi divísivel {contador} vezes")
if contador == 2: 
    print("primo")
else: 
    print("Não primo")

