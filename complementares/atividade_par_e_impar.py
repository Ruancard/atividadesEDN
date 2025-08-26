#variaveis
pares = 0
impares = 0

#Laço de repetição
while True:
    try:
        entrada = input('Digite um numero inteiro ou "fim" para sair: ')

        if entrada.lower() == "fim":
            break
        numero = int(entrada)

        #Contabiliza numeros pares
        if numero % 2 == 0:
            print(f"o numero {numero} é par")
            pares += 1

        #Contabiliza numeros impares
        if numero % 2 != 0:
            print(f"o numero {numero} é impar")
            impares += 1

    #Tratativa de erros        
    except ValueError:
        print("Digite um caracter valido")

#Resultado
print(f"foram digitados {pares} numeros pares e {impares} numeros impares.")