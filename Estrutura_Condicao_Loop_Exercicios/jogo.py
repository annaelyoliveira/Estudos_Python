numSecreto = 7

for i in range (2):
    numAdvinha = int(input("Digite um número inteiro e advinhe qual número estou pensando, você tem 3 tentativas"))
    if numAdvinha < numSecreto:
        print("Você digitou um número menor que o meu")
    elif numAdvinha > numSecreto:
        print("Você digitou um número maior que o meu")
    else:
        print("Parabéns você acertou")


