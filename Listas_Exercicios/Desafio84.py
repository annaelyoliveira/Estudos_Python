dados = []
pessoas = []
maior = menor = 0 

while True:
    dados.append((input("Nome:")))
    dados.append(float(input("Peso:")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else: 
        if dados[1] > maior: 
            maior = dados[1]
        if dados[1] < menor: 
            menor = dados[1]
    pessoas.append(dados[:]) #ATENÇÃO
    dados.clear()
   
    saida = input("Quer continuar? (S/N):")
    if saida in "Nn":
        break
print(pessoas)

print(f"Foram cadastradas {len(pessoas)} pessoas")

print(f"O maior peso foi de {maior}kg. Peso de ", end='')
for pessoa in pessoas: 
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}] ", end='')

print(f"\nO menor peso foi de {menor}kg. Peso de ", end='')
for pessoa in pessoas: 
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}] ", end='')


