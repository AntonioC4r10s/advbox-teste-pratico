import pandas as pd


def migracao_clientes():
    '''Faz a extração dos dados de clientes requeridos para o novo modelo e retorna
    dois dataframes, o primeiro é um dadaframe com os dados brutos dos clientes,
    o segundo contem os dados dos clientes em um modelo pré-estruturado conforme
    o modelo de migração.'''

    df_clientes_migracao = pd.read_csv('data/backup/v_clientes_CodEmpresa_92577.csv', encoding='mac_roman', delimiter=';')

    # colunas_clientes_migracao = ['razao_social', 'cnpj', 'cpf', 'rg', 
    #                             'nacionalidade', 'nascimento', 'estado_civil',
    #                             'profissao', 'telefone1', 'email1', 'uf', 
    #                             'cidade', 'bairro', 'cep', 'pis', 'nome_mae',
    #                             'email2']
    # # df_clientes_migracao = df_clientes_migracao[colunas_clientes_migracao]
    df_clientes_migracao['pis'] = df_clientes_migracao['pis'].apply(lambda x: str(int(x)) if pd.notnull(x) else x)
    df_modelo_clientes = pd.read_excel('data/CLIENTES.xlsx')
    df_modelo_clientes['NOME'] = df_clientes_migracao['razao_social'] # lembrar de tirar os duplicados
    df_modelo_clientes['CPF CNPJ'] = df_clientes_migracao['cpf'].fillna(df_clientes_migracao['cnpj'])
    df_modelo_clientes['RG'] = df_clientes_migracao['rg']
    df_modelo_clientes['NACIONALIDADE'] = df_clientes_migracao['nacionalidade']
    df_modelo_clientes['DATA DE NASCIMENTO'] = df_clientes_migracao['nascimento']
    df_modelo_clientes['ESTADO CIVIL'] = df_clientes_migracao['estado_civil']
    df_modelo_clientes['PROFISSÃO'] = df_clientes_migracao['profissao']
    df_modelo_clientes['TELEFONE'] = df_clientes_migracao['telefone1']
    df_modelo_clientes['EMAIL'] = df_clientes_migracao['email1']
    df_modelo_clientes['ESTADO'] = df_clientes_migracao['uf']
    df_modelo_clientes['CIDADE'] = df_clientes_migracao['cidade']
    df_modelo_clientes['BAIRRO'] = df_clientes_migracao['bairro']
    df_modelo_clientes['CEP'] = df_clientes_migracao['cep']
    df_modelo_clientes['PIS PASEP'] = df_clientes_migracao['pis']
    df_modelo_clientes['NOME DA MÃE'] = df_clientes_migracao['nome_mae']
    df_modelo_clientes['ANOTAÇÕES GERAIS'] = df_clientes_migracao['email2']
    # print(df_modelo_clientes)

    return df_clientes_migracao, df_modelo_clientes

