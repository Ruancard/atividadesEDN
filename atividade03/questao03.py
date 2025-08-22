#Inputs
temperatura  = float(input("digite a temperatura que deseja converter: "))
origem = input("Digite o numero correspondente a unidade de temperatura de origem: \n1)celsius \n2)Fahrenheit \n3)Kelvin \n")
destino = input("Digite o numero correspondente a unidade de temperatura de destino: \n1)celsius \n2)Fahrenheit \n3)Kelvin \n")


#Condicionais
if origem == destino:
    resultado = temperatura
match origem:
    case "1":
        match destino:
            case "2":
                resultado = ((temperatura * 9/5) + 32)
            case "3":
                resultado = (temperatura + 273.15)
            case _:
                print("opção invalidad")
    case "2":
        match destino:
            case "1":
                resultado = ((temperatura - 32) * 5/9)
            case "3":
                resultado = ((temperatura -32) *5/9 + 273.15)
            case _:
                print("opção invalidad")
    case "3":
        match destino:
            case "1":
                resultado = ( temperatura -273.15)
            case "2":
                resultado = (( temperatura - 273.15) *9/5 + 32)
            case _:
                print("opção invalidad")
    case _:
        print("opção invalidad")

#Resultado
print(resultado)