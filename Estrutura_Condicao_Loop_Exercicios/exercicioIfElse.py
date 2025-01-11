valorCompra = float(input("Digite o valor da compra:"))


if valorCompra > 100:
  print("O valor final é:", (valorCompra - ((10/100)* valorCompra)))
else:
  print("Valor original:", valorCompra)
