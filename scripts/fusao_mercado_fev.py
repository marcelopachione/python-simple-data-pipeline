from processa_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

print(f"Inicio do Processamento")

# Extracting the data from the files
empresaA = Dados(path_json, 'json')
empresaB = Dados(path_csv, 'csv')


# Transform
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

empresaB.rename_columns(key_mapping)

dados_fusaso = Dados.join(empresaA, empresaB)

## Load
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusaso.salvando_dados('data_processed/dados_combinados.csv')

print(f"Arquivo Salvo em {path_dados_combinados}")

print(f"Fim do Processamento")