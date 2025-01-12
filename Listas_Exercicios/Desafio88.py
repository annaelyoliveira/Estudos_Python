import random
jogos = []
jogo = []

jogadas = int(input("Quantos jogos quer  que eu sorteie? "))
print(f"------ SORTEANDO {jogadas} JOGOS ------")
for i in range (1, jogadas+1):
    for c in range (0,6):
        numero = random.randint(1, 60)
        if numero not in jogos:
            jogo.append(numero)
    jogos.append(jogo[:])
    jogo.clear()

for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")

print(f"------ BOA SORTE -------")