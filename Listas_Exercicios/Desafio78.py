lista = []

for i in range (0,5):
    lista.append(int(input("Digite um número inteiro: ")))

print(lista)

copia2= lista[:]
copia2.sort(reverse=True)
print(f"O maior número é: {copia2[0]}")
copia1= lista[:]
copia1.sort()
print(f"O menor número é: {copia1[0]}")


print(f"O maior valor {copia2[0]} está na posição(s): ", end= "")
for c, v in enumerate(lista): 
    if v == copia2[0]:
        print(f"{c}..", end="")

print(f"O menor valor {copia1[0]} está na posição(s): ", end="")
for c, v in enumerate(lista): 
    if v == copia1[0]:
       print(f"{c}..", end="")
 

#resolução do professor

valores = []
maior = 0
menor = 0 
print("\n")
for i in range (0,5):
    valores.append(int(input(f"Digite o número da posição {i}: ")))
    if i == 0:
        maior = menor = valores[i]
    else: 
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor= valores[i]
print(f"Lista: {valores} \nO maior valor digitado foi {maior} e está nas posições: ", end="")
for i, v in enumerate(valores):
    if v == maior: 
        print(f"{i}..", end="")
print(f"O menor valor digitado foi {menor} e está nas posições: ", end="")
for i, v in enumerate(valores):
    if v == menor: 
        print(f"{i}..", end="")




