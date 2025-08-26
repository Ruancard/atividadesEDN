def calcula_desconto(preco, porcentagem_desconto):
    desconto = (preco * (porcentagem_desconto / 100))
    total = preco - desconto
    return desconto, total

preco = float(input("Digite o preço do produto: "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))
desconto, total = calcula_desconto(preco, porcentagem_desconto)
print(f'o valor total ficou R${total}, com o desconto de R${desconto}')