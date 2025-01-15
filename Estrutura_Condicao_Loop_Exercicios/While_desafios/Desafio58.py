import random
contador = 0 
numero_aleatorio = random.randint(0,10)
print("------- Estou pensando em um número entre 0 e 10, tente adivinhar ---------")

while True: 
    numero = int(input("Digite o número que você acha que é: "))
    contador += 1
    if numero == numero_aleatorio:
        break
print(f"Você acertou com {contador} tentativas, muito bem!")