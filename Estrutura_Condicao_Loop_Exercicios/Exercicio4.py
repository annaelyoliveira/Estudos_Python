salario = float(input("Digite o salário do colaborador:"))
percento = 0

if(salario <= 280):
    percento = 20
elif(salario > 280 and salario <= 700):
    percento = 15
elif (salario > 700 and salario <= 1500):
    percento = 10
else:
    percento = 5

aumento = (percento/100) * salario
salarioNovo = aumento + salario
print("Seu salário era ", salario, "reais." 
          "\nVocê recebeu um percentual de aumento de", percento,"%." 
          "\nO valor do aumento foi de:", aumento, "reais."
          "\nVocê agora receberá o salário de:" , salarioNovo, "reais.")