numero = int(input("Digite o número: "))
contador = numero 
fatorial = 1

while contador > 0:
    print('{}'.format(contador), end = "")
    print(' * ' if contador > 1 else ' = ', end ='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')