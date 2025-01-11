lista = [ ]

while True: 
    numero = int(input("Digite o número:"))
    lista.append(numero)
    saida = input("Quer continuar? (S/N)")
    if saida in "Nn":
        break

print(f"Foram digitados {len(lista)} números")

lista.sort(reverse=True)
print(f"Lista ordenada de forma descrescente: {lista}")

if 5 in lista:
    print("O valor 5 foi digitado")
else:
    print("O valor 5 não foi encontrado")
