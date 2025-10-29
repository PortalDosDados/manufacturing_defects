import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Autenticação
api = KaggleApi()
api.authenticate()

dataset = 'fahmidachowdhury/manufacturing-defects'
file_name = 'defects_data.csv'
destination = './data'

# Cria pasta de destino se não existir
os.makedirs(destination, exist_ok=True)

# Baixa o arquivo CSV diretamente (não é zip)
api.dataset_download_file(dataset, file_name, path=destination, force=False)

print(f"{file_name} baixado com sucesso em {destination}!")
