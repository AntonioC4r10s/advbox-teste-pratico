import streamlit as st
import os
from transform import transformacao_processos, transformacao_clientes

BACKUP_DIR = 'data/backup/'

os.makedirs(BACKUP_DIR, exist_ok=True)

st.set_page_config(page_title="Interface de Geração de Planilhas", page_icon="📊", layout="centered")

st.title("Interface de Geração de Planilhas de Migração")
st.write(
    """
    Bem-vindo à interface de geração de planilhas de migração para a Advbox. Este software foi desenvolvido para auxiliar na migração de dados do escritório jurídico 92577, facilitando o processo de importação de dados essenciais de clientes e processos para a plataforma Advbox.

    O objetivo principal é garantir que todas as informações relevantes sejam extraídas e formatadas de acordo com os padrões exigidos pela Advbox. A operação será realizada com base em dados contidos na base Backup_de_dados_92577, utilizando as tabelas vinculadas corretamente para assegurar a integridade e a precisão da informação.

    Para a migração, é fundamental observar as orientações contidas nas planilhas padrões da Advbox, que incluem, entre outros aspectos, a formatação de datas no padrão nacional (DD/MM/AAAA) e a verificação de campos obrigatórios.
    """
)

st.subheader("Clientes")
st.write(
    """
    A tabela de clientes inclui todos os contatos do escritório, abrangendo informações como telefone, celular, endereço, e-mail, e outros dados relevantes. É essencial que todas as pessoas relacionadas a processos sejam incluídas nesta tabela.
    
    Ao gerar a planilha de clientes, os dados extraídos serão organizados e tratados de acordo com as especificações da Advbox, proporcionando uma migração mais eficiente e completa.
    """
)

st.subheader("Processos")
st.write(
    """
    A tabela de processos contém todos os casos jurídicos do escritório.
    Os nomes dos clientes e das partes contrárias devem ser consistentes em ambas as planilhas geradas. A integração de dados entre as tabelas será realizada de forma a garantir a correta correspondência e estruturação das informações.
    """
)

st.subheader("Gerar Arquivos de Migração")
if st.button("Gerar CLIENTES.xlsx"):
    st.write("Iniciando a geração do arquivo CLIENTES.xlsx...")
    transformacao_clientes()
    st.write(f"O arquivo CLIENTES.xlsx foi gerado com sucesso e está disponível em: {os.path.join(BACKUP_DIR, 'CLIENTES.xlsx')}")

if st.button("Gerar PROCESSOS.xlsx"):
    st.write("Iniciando a geração do arquivo PROCESSOS.xlsx...")
    transformacao_processos()
    st.write(f"O arquivo PROCESSOS.xlsx foi gerado com sucesso e está disponível em: {os.path.join(BACKUP_DIR, 'PROCESSOS.xlsx')}")

st.subheader("Download dos Arquivos")

st.write(
"""
Se já cocluiu a geração dos arquivos eles estão salvos na pasta 'data\output'.
"""
)

