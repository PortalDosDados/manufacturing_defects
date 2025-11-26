# 🏭 Análise de Defeitos de Manufatura (Manufacturing Defects Analysis)

Este projeto consiste em uma ferramenta de **Análise Exploratória de Dados (EDA)** voltada para o setor industrial. O objetivo é processar dados brutos de qualidade, identificar padrões de falhas e visualizar custos de reparo e severidade, auxiliando gestores na tomada de decisão baseada em dados (Data-Driven Decision Making).

## 📋 Visão Geral do Projeto

O script ingere um dataset de controle de qualidade e responde a perguntas críticas:

* Qual é a severidade predominante dos defeitos?
* Quais tipos de defeitos são mais frequentes?
* Qual é o impacto financeiro (custo de reparo) associado?

## 🛠 Tecnologias Utilizadas

O projeto foi desenvolvido em **Python 3** utilizando a stack de Ciência de Dados padrão:

* **Pandas:** Manipulação e limpeza de dados tabulares.
* **NumPy:** Operações numéricas de alta performance.
* **Matplotlib & Seaborn:** Visualização de dados estatísticos.

## 📂 Estrutura de Arquivos

Para garantir a execução correta, o projeto deve seguir a seguinte hierarquia de pastas (conforme definido no script):

```text
MANUFACTURING_DEFECTS/
│
├── data/                         <-- Pasta para armazenar os dados
│
├── venv/                         <-- Ambiente virtual Python
│
├── .gitattributes                <-- Configurações de atributos do Git
├── .gitignore                    <-- Arquivo para ignorar itens no Git
├── download.py                   <-- Script auxiliar para download de dados
├── main.py                       <-- Script principal de análise
├── README.md                     <-- Documentação do projeto (modificado)
└── requirements.txt              <-- Lista de dependências do projeto
