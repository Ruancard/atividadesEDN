while True:
    try:
        numero1 = float (input("Digite o primeiro número: "))
        numero2 = float (input("Digite o segundo número: "))
        operacao = input("Digite o operador (+, -, *, /): ")

        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            resultado = numero1 / numero2
        else:
            raise Exception()
        
        print(f"O resultado é: {resultado}")
        break
    
    except ValueError:
        print("Erro: Você deve digitar apenas números")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida")
    except Exception:
        print("Erro: Você deve digitar apenas operações válidas (+, -, *, /)")