
while True: 
    sexo = input("Digite o sexo da pessoa (F/M): ")
    if sexo in "Ff" or sexo in "Mn":
        break
    else: 
        print("Tente novamente!")