saque = int(input("Digite a quantia que deseja sacar: "))

if(saque == 2 and saque < 5):
    print("Você recebeu: 1 nota de 2")
if(saque == 5 and saque < 10):
     print("Você recebeu: 1 nota de 5")
if(saque == 10 and saque < 20):
      print("Você recebeu: 5 notas de 2")
if(saque == 20 and saque < 50):
     print("Você recebeu: 2 notas de 20 e 1 nota de 10")
if(saque == 50 and saque < 100):
     print("Você recebeu: 2 notas de 20, 1 nota de 10 e duas notas de 50")
if(saque == 100 and saque < 200):
     print("Você recebeu: 2 notas de 20, 1 nota de 10 e duas notas de 50")