qntProduto = int(input("Digite qnts produtos comporu:"))
vista = input("Foi a vista (S/N): ")
clube = input("Tem cadastro no clube? (S/N): ")
valor = float(input("Digite o valor total da compra: "))

if qntProduto >= 3 and vista == "S" or clube == "S":
    print(f'Desconto de 20% o valor da compra é de: {valor} e vai ficar {valor - (20/100)*valor}')
else: 
    print("Não teve desconto")
