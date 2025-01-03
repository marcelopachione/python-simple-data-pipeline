import json
import csv

class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nomes_colunas = self.get_columns()
        #self.renomeia_colunas = self.rename_columns()
    
    def leitura_json(self):
        dados_json = []

        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json
    
    def leitura_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    def leitura_dados(self): 
        dados = []

        if self.tipo_dados == 'csv': 
            dados = self.leitura_csv()
            
        elif self.tipo_dados == 'json': 
            dados = self.leitura_json()
            
        return dados

    def get_columns(self):
        return list(self.dados[-1].keys())

    def rename_columns(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
        
        self.dados = new_dados
        self.nomes_colunas = self.get_columns()

    # def size_data(dados):
    #     return len(dados)

    # def join(dadosA, dadosB):
    #     combined_list = []
    #     combined_list.extend(dadosA)
    #     combined_list.extend(dadosB)
    #     return combined_list

    # def transformando_dados_tabela(dados, nomes_colunas):
        
    #     dados_combinados_tabela = [nomes_colunas]

    #     for row in dados:
    #         linha = []
    #         for coluna in nomes_colunas:
    #             linha.append(row.get(coluna, 'Indisponivel'))
    #         dados_combinados_tabela.append(linha)
        
    #     return dados_combinados_tabela

    # def salvando_dados(dados, path):
    #     with open(path, 'w') as file:
    #         writer = csv.writer(file)
    #         writer.writerows(dados)