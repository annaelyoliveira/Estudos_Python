letra = input("Digite uma letra:")

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
   print("A letra é uma vogal")
else:
    print("A letra é uma consoante")


num1 = int(input("Digite um número:"))
num2 = int(input("Digite um número:"))
num3 = int(input("Digite um número:"))
if num1 > num2 and num1 > num3 and num2 > num3:
    print(f'Número maior {num1, num2, num3}')
elif num2 > num1 and num2 > num3 and num1 > num3:
    print(f'Número maior {num2, num1, num3}')
elif num3 > num1 and num3 > num2 and num1 > num2: 
    print(f'Número maior {num3, num1, num2}')
elif num1 > num2 and num1 > num3 and num3 > num2:
    print(f'Número maior {num1, num3, num2}') 
elif num2 > num1 and num2 > num3 and num3 > num1:
    print(f'Número maior {num2, num3, num1}')
else: 
    print(f'Número maior {num3, num2, num1}')
 
