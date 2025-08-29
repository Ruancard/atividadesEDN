import pandas as pd

def processar_log_treinamento(nome_arquivo):
    try:
        leitor = pd.read_csv(nome_arquivo)
        media_tempo = leitor['tempo_execucao'].mean()
        desvio_padrao = leitor['tempo_execucao'].std()
        return media_tempo, desvio_padrao
    except FileNotFoundError:
        print(f'Arquivo não encontrado')
        return None


nome_arquivo = 'atividade07/logs_treinamento.csv'
media, desvio = processar_log_treinamento(nome_arquivo)
print(f'''
    Média de tempo: {media}
    Desvio padrão: {desvio}
''')