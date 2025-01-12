valor = float(input("Digite o valor: ")) * 100

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    quantidade = int(valor // nota)
    valor %= nota
    print(f"{quantidade} nota(s) de R$ {nota / 100:.2f}")

print("MOEDAS:")
for moeda in moedas:
    quantidade = int(valor // moeda)
    valor %= moeda
    print(f"{quantidade} moeda(s) de R$ {moeda / 100:.2f}")




    