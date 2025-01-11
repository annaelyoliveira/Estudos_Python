lista = []

while True:
    lista.append(int(input("Digite um número: ")))
    saida = input("Quer continuar? (S/N)")
    if saida in "Nn":
        break

pares = []
impares = []

for c,v in enumerate(lista):
    if v % 2 == 0: 
        pares.append(v)
    else: 
        impares.append(v)

print(f"Lista completa: {lista}")
print(f"Lista pares: {pares}")
print(f"Lista impares: {impares}")