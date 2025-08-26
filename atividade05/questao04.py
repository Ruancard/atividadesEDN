from datetime import datetime, date

def calcular_dias_vivos(data_nascimento_str):
    try:
        # Converte a string da data para um objeto date
        data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
        
        # Obtém a data atual
        data_atual = date.today()

        # Calcula a diferença entre as duas datas
        diferenca = data_atual - data_nascimento

        # Retorna o número de dias
        return diferenca.days

    except ValueError:
        return "Formato de data inválido. Por favor, use 'DD/MM/AAAA'."

#Input
data_nascimento_usuario = input("Digite sua data de nascimento (DD/MM/AAAA): ")

#Chama a função e armazena o resultado
dias_vivos = calcular_dias_vivos(data_nascimento_usuario)

#Resultado
if isinstance(dias_vivos, int):
    print(f"Você está vivo há {dias_vivos} dias.")
else:
    print(dias_vivos)
