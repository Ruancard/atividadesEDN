#Variaveis
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))

#Calculo
imc = (peso / (altura ** 2))

#Condicionais
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "obeso"