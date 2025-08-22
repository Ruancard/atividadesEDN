#Variaveis
idade = float(input("digite sua idade: "))

#Condicionais
if idade >= 60:
    print("você é um idoso")
if idade >= 18:
    print("você é um adulto.")
elif idade >= 13:
    print("Você é um adolescente.")
elif idade >= 2:
    print("Você é uma criança.")
elif idade >= 0:
    print("Você é um bebê.")
else:
    print("Você nem nasceu.")

#Fim do programa
print("Fim do programa.")