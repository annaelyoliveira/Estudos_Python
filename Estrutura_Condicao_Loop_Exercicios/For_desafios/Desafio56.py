soma = 0
mais_velho = 0 
mulher_20 = 0
for i in range (0,4):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: (F/M)")
    if idade > mais_velho and sexo =="M":
        mais_velho = idade
        nome_mais_velho = nome
    if sexo== "F" and idade <= 20:
        mulher_20 += 1
    soma += idade
    

print(f"A média de idade do grupo é {soma/4}")
print(f"O nome do homem mais velho é {nome_mais_velho}")
print(f"{mulher_20} mulheres têm menos de 20 anos")
