lista = []


while True:
    numero = int(input("Digite um número: "))
    if numero not in lista:
        lista.append(numero)
        print("Valor adicionado com sucesso")
    else:
        print("Valor duplicado! Não será adicionado.")
    saida = input("Deseja sair? (S/N):")
    if saida in "Ss":
        break

lista.sort()
print(lista)    
