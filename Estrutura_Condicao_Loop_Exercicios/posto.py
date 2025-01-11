qntdLitro = float(input("Quantos litros vc quer abastecer: "))
tipoCombustível = input("Quer colocar 1. Álcool 2. Gasolina 3. Aditivada 4. Diesel: ")

if tipoCombustível == 1:
    print(f'Você vai pagar {qntdLitro*5.50} reais')
if tipoCombustível == 2:
    print(f'Você vai pagar {qntdLitro*8} reais')
if tipoCombustível == 3:
    print(f'Você vai pagar {qntdLitro*9.5} reais')
else:
    print(f'Você vai pagar {qntdLitro*9} reais')
