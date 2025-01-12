matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna = maior = 0
for i in range  (0,3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite o valor:"))
for i in range (0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]}]", end = '')
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]

    print()

print(f"Soma valores pares: {pares}")

for c in range (0,3):
    coluna += matriz[c][2]
print(f"Soma dos valores da terceira coluna: {coluna}")

for c in range (0,3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"Maior valor da segunda linha: {maior}")