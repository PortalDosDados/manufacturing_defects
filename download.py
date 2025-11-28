import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Autenticação
api = KaggleApi()
api.authenticate()

dataset = 'fahmidachowdhury/manufacturing-defects'
file_name = 'defects_data.csv'
destination = './data'

# Cria pasta de destino se não existir
os.makedirs(destination, exist_ok=True)

# Baixa o arquivo CSV diretamente
api.dataset_download_file(dataset, file_name, path=destination, force=False)

print(f"{file_name} baixado com sucesso em {destination}!")

# Caminho do arquivo original
arquivo_original = './data/defects_data.csv'

# Lê o CSV
df = pd.read_csv(arquivo_original)

# 1) Converter a coluna de data para datetime (robusto para M/D/YYYY ou YYYY-MM-DD)
# Tenta primeiro formato americano, depois ISO; se já estiver em datetime, segue
try:
    df['defect_date'] = pd.to_datetime(df['defect_date'], format='%m/%d/%Y', errors='raise')
except Exception:
    df['defect_date'] = pd.to_datetime(df['defect_date'], errors='coerce')

# Verifica se houve alguma falha na conversão
if df['defect_date'].isna().any():
    linhas_invalidas = df[df['defect_date'].isna()]
    print("Aviso: algumas datas não puderam ser convertidas. Linhas afetadas:")
    print(linhas_invalidas.head())

# 2) Formatar para padrão brasileiro (substitui a coluna original)
df['defect_date'] = df['defect_date'].dt.strftime('%d/%m/%Y')

# 3) Remover coluna auxiliar se existir
if 'defect_date_br' in df.columns:
    df = df.drop(columns=['defect_date_br'])

# 4) Traduzir títulos das colunas
traducao_colunas = {
    'defect_id': 'id_defeito',
    'product_id': 'id_produto',
    'defect_type': 'tipo_defeito',
    'defect_date': 'data_defeito',
    'defect_location': 'local_defeito',
    'severity': 'severidade',
    'inspection_method': 'metodo_inspecao',
    'repair_cost': 'custo_reparo',
}
df = df.rename(columns=traducao_colunas)

# 5) Salvar no mesmo local com novo nome
pasta = os.path.dirname(arquivo_original)
novo_arquivo = os.path.join(pasta, 'defeitos_dados.csv')
df.to_csv(novo_arquivo, index=False, encoding='utf-8-sig')

print(f"Arquivo traduzido e com datas no padrão brasileiro salvo em: {novo_arquivo}")