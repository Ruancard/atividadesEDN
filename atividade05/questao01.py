def conta(valor_conta, porcentagem_gorjeta):
    gorjeta = (valor_conta * (porcentagem_gorjeta / 100))
    return (gorjeta)

#codigo main
valor_conta = float(input("Digite o valor total da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem que você deseja dar de gorjeta: "))
gorjeta = conta(valor_conta, porcentagem_gorjeta)
print(f"O valor da gorjeta é: R${gorjeta:.2f}")