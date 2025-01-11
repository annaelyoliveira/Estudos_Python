
contador1 = 0
contador2 = 0

expressao = str(input("Digite a expressao: "))

for simbolo in expressao:
    if simbolo == "(": 
        contador1+= 1
    if simbolo == ")":
        contador2+= 1
if contador1 > contador2 or contador2 > contador1:
    print("Sua expressão está errada!")
else:
    print("Sua expressão está certa!")
    

#resolução do professor com PILHA

pilha = []

expressao = str(input("Digite a expressao: "))

for simbolo in expressao: #se tiver um ( vai adicionar na pilha, se aparecer um ) vai retirar o ( da pilha, ou seja o parenteses abrindo encontrou seu par
    if simbolo == "(": #adicionar ( abrindo na pilha
        pilha.append("(")
    elif simbolo == ")": # ( abrindo encontrou seu par ) fechando, retiro o ( abrindo da pilha ***que não estiver vazia***
        if len(pilha) > 0: #pilha com item
            pilha.pop()
        else: #pilha vazia
            pilha.append(")")
            break
if len(pilha) == 0: #pois se tiver vazia cada ( abrindo encontrou seu par ) fechando
    print("Sua expressão está válida")
else: 
    print("Sua expressão está errada")
