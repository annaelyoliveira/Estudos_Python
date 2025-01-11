peso = float(input("Digite o peso:"))
altura = float(input("Digite a altura:"))

IMC = peso/(altura**2)

if IMC < 18.5:
    print("Baixo peso")
elif IMC >= 18.5 and IMC <= 24.99:
    print("Normal")
elif IMC >= 25 and IMC <= 29.99:
    print("Sobrepeso")
else:
    print("Obesidade")