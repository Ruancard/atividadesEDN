while True:
    try:
        senha = input("Digite a senha: ")
        if senha.lower() == "sair":
            print("saindo do programa... ")
            break
        if len(senha) <= 8:
            raise Exception("senha muito curta")
        else:
            print("sua senha é boa")
    except Exception as e:
        print(f'erro: "{e}"')