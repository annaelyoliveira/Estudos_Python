num1 = int(input("Número:"))
num2 = int(input("Número:"))
num3 = int(input("Número:"))

if (num1 > 0 and num2 > 0 and num3 > 0):
    print("Todos são positivos: Sim")
else: 
    print("Todos são positivos: Não")
if (num1 < 0 or num2 < 0 or num3< 0):
    print("Pelo o menos um é negativo: Sim")
else: 
    print("Pelo o menos um é negativo: Não")
if num1 % 2 == 0 and num2 %2 == 0 and num3 % 2 == 0:
    print("Todos são pares: Sim")
else: 
    print("Todos são pares: Não")
