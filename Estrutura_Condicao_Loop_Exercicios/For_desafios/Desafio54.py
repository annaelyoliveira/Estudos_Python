maior = menor = 0
for i in range (0,7):
    ano = int(input("Digite o ano de nascimento: "))
    conta = 2024 - ano 
    if conta >= 18:
        maior += 1
    else: 
        menor += 1
print(f"{maior} pessoas são maior de idade. \n{menor} pessoas são menor de idade")