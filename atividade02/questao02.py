#variaveis
nome = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

#Calculos
valor_desconto = ((porcentagem_desconto / 100) * preco_original)
preco_final = (preco_original - valor_desconto)

#Resultado
print(f"Preço final: R${preco_final:.2f}")