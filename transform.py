import pandas as pd
from extract import migracao_clientes
from unidecode import unidecode
import re
import os
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Font


'''Função para ajustar o gênero em um texto. Altera 'bras' para 'brasileira' ou 'brasileiro' dependendo da terminação.'''
def ajustar_genero(texto):
    if pd.isna(texto):
        return texto
    if texto.endswith('a'):
        return texto.replace('bras', 'brasileira')
    elif texto.endswith('o'):
        return texto.replace('bras', 'brasileiro')
    else:
        return texto.replace('bras', 'brasileiro')


'''Função para corrigir caracteres especiais em um texto usando a biblioteca unidecode.'''
def corrigir_caracteres(texto):
    if pd.isnull(texto):
        return texto
    return unidecode(texto)


'''Função principal para transformar o DataFrame de clientes. Aplica transformações de formatação e salva em um arquivo Excel.'''
def trasformacao_clientes():
    _, df_modelo_clientes = migracao_clientes()
    df_modelo_clientes = df_modelo_clientes.dropna(subset=['NOME'])
    df_modelo_clientes = df_modelo_clientes.drop_duplicates(subset='NOME', keep='first')
    if 'NACIONALIDADE' in df_modelo_clientes.columns:
        df_modelo_clientes['NACIONALIDADE'] = df_modelo_clientes['NACIONALIDADE'].apply(ajustar_genero)
    df_modelo_clientes['DATA DE NASCIMENTO'] = pd.to_datetime(df_modelo_clientes['DATA DE NASCIMENTO'], format='%d/%m/%Y %H:%M')
    df_modelo_clientes['DATA DE NASCIMENTO'] = df_modelo_clientes['DATA DE NASCIMENTO'].dt.strftime('%d/%m/%Y')
    df_modelo_clientes['PROFISSÃO'] = df_modelo_clientes['PROFISSÃO'].apply(lambda x: x.encode('mac_roman').decode('utf-8') if pd.notnull(x) else x)
    df_modelo_clientes['PROFISSÃO'] = df_modelo_clientes['PROFISSÃO'].apply(corrigir_caracteres)
    df_modelo_clientes['ESTADO'] = df_modelo_clientes['ESTADO'].apply(lambda x: x.upper() if pd.notnull(x) else x)
    df_modelo_clientes['CIDADE'] = df_modelo_clientes['CIDADE'].replace('Floripa', 'Florianopolis')
    df_modelo_clientes['CIDADE'] = df_modelo_clientes['CIDADE'].apply(lambda x: x.encode('mac_roman').decode('utf-8') if pd.notnull(x) else x)
    df_modelo_clientes['BAIRRO'] = df_modelo_clientes['BAIRRO'].apply(lambda x: x.encode('mac_roman').decode('utf-8') if pd.notnull(x) else x)
    df_modelo_clientes['CEP'] = df_modelo_clientes['CEP'].apply(
        lambda x: f'{re.sub("[^0-9]", "", str(x))[:5].zfill(5)}-{re.sub("[^0-9]", "", str(x))[5:].zfill(3)}' 
        if pd.notnull(x) and len(re.sub("[^0-9]", "", str(x))) >= 8 else x
    )

    df_modelo_clientes['PIS PASEP'] = df_modelo_clientes['PIS PASEP'].apply(
        lambda x: f'{re.sub("[^0-9]", "", str(x))[:3].zfill(3)}.{re.sub("[^0-9]", "", str(x))[3:7].zfill(4)}.{re.sub("[^0-9]", "", str(x))[7:10].zfill(3)}-{re.sub("[^0-9]", "", str(x))[10:11].zfill(1)}'
        if pd.notnull(x) and len(re.sub("[^0-9]", "", str(x))) >= 11 else x
    )

    output_dir = 'data/output'
    os.makedirs(output_dir, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    for row in dataframe_to_rows(df_modelo_clientes, index=False, header=True):
        ws.append(row)
    header_row = ws[1]
    for cell in header_row:
        cell.font = Font(name='Arial', bold=True, size=10)
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        for cell in row:
            cell.font = Font(name='Arial', size=10)
    file_path = os.path.join(output_dir, 'CLIENTES.xlsx')
    wb.save(file_path)

    return df_modelo_clientes
