#Laço de repetição
while True:
    try:
        senha = input('Digite a senha ou "fim" para encerrar o programa: ')
        if senha.lower() == "fim":
            print("saindo do programa... ")
            break
        if len(senha) < 8:
            raise Exception("senha muito curta")
        
        tem_numero = False
        for caractere in senha:
            if caractere in '0123456789':
                tem_numero = True
                break

        if tem_numero == False:
            raise Exception("A senha deve conter pelo menos um número.")
        
        else:
            print("sua senha é boa")

    #Tratativa de erros
    except Exception as e:
        print(f'erro: "{e}"')