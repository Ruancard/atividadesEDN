#Lista de variaveis
notas = {"nota_1":7.5, "nota_2":8.0 , "nota_3":6.5}

#Calculos
soma_notas = ( notas["nota_1"] + notas["nota_2"] + notas["nota_3"] )
media = (soma_notas / len(notas))

#Resultado
print(f"A média das notas é: {media:.2f}")