import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../manufacturing_defects/data/defects_data.csv')

# Exibindo as primeiras informações do dataset

print(df.info())

print(df.shape) # Dataset possuí 1000 linhas e 8 colunas

print(df.describe()) 

'''
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   defect_id          1000 non-null   int64
 1   product_id         1000 non-null   int64
 2   defect_type        1000 non-null   object
 3   defect_date        1000 non-null   object
 4   defect_location    1000 non-null   object
 5   severity           1000 non-null   object
 6   inspection_method  1000 non-null   object
 7   repair_cost        1000 non-null   float64
'''

print(df.head())

# Plotando defeitos por severidade

# Contagem de severidades
severity_counts = df['severity'].value_counts()

# Criação do gráfico
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=severity_counts.index, y=severity_counts.values, palette='viridis')

# Adicionando rótulos nas barras
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', fontsize=10, padding=3)

plt.title('Distribuição de Defeitos por Severidade', fontsize=14)
plt.xlabel('Severidade')
plt.ylabel('Quantidade de Defeitos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotando tipos de defeitos

# Contagem de severidades
defect_type_counts = df['defect_type'].value_counts()


# Criação do gráfico
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=defect_type_counts.index, y=defect_type_counts.values, palette='viridis')

# Adicionando rótulos nas barras
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', fontsize=10, padding=3)

plt.title('Distribuição de Defeitos por Tipo', fontsize=14)
plt.xlabel('Tipo')
plt.ylabel('Quantidade de Defeitos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()