dados = []
pessoas = []

nomesPesados = []
nomesMenorPeso = []
while True:
    dados.append(str(input("Nome:")))
    dados.append(float(input("Peso:")))
    pessoas.append(dados[:]) #ATENÇÃO
    dados.clear()
   
    saida = input("Quer continuar? (S/N):")
    if saida in "Nn":
        break
print(pessoas)

print(f"Foram cadastradas {len(pessoas)} pessoas")

menorPeso = pessoas[0][1]
maiorPeso = pessoas[0][1]

for pessoa in pessoas:
    if pessoa[1] > maiorPeso:
        maiorPeso = pessoa[1] 
        nomesPesados.append(pessoa[0])
    if pessoa[1] < menorPeso:
        menorPeso = pessoa[1]
        nomesMenorPeso.append(pessoa[0])

print(f"O maior peso foi de {maiorPeso}kg. Peso de {nomesPesados}")
print(f"O menor peso foi de {menorPeso}kg. Peso de {nomesMenorPeso}")

#RESOLUÇÃO PROFESSOR

dados = []
pessoas = []
maior = menor = 0 

while True:
    dados.append(str(input("Nome:")))
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
print(f"O maior peso foi de {maior}kg. Peso de", end='')
for pessoa in pessoas: 
    if pessoa[1] == maior:
        print(f"{pessoa[0]}", end='')
print()
print(f"O menor peso foi de {maior}kg. Peso de", end='')
for pessoa in pessoas: 
    if pessoa[1] == menor:
        print(f"{pessoa[0]}", end='')