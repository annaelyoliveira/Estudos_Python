lista = [ ] 

for i in range (0,5):
    numero = int(input("Digite um valor: "))
    if i == 0 or numero > lista[-1]:
        lista.append(numero)
        print("Adicionado ao final da lista")
    else: 
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f"Adicionado na posição {posicao} da lista")
                break
            posicao += 1
print(f"Os valores digitados em ordem foram {lista}")
        