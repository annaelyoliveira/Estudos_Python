maior = 0

for i in range (0,5):
    peso = int(input("Digite o peso: "))
    if peso > maior:
       maior = peso
    if peso < maior:
       menor = peso

print(f"Maior peso: {maior} \nMenor peso: {menor}") 