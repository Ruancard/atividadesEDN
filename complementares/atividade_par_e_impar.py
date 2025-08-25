pares = 0
impares = 0

while True:
    try:
        entrada = input('Digite um numero inteiro ou "fim" para sair: ')

        if entrada.lower() == "fim":
            break
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"o numero {numero} é par")
            pares += 1
        if numero % 2 != 0:
            print(f"o numero {numero} é impar")
            impares += 1
    except ValueError:
        print("Digite um caracter valido")
print(f"foram digitados {pares} numeros pares e {impares} numeros impares.")