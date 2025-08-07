# 🛠️ ETL em Python para Arquivo CSV Grande com Carga no SQL Server

Este projeto realiza um processo **ETL (Extract, Transform, Load)** eficiente para arquivos `.csv` de grande porte, realizando:

- Leitura por chunks (blocos)
- Tratamento de erros e dados inválidos
- Carga incremental em banco de dados **SQL Server**
- Registro de linhas com falhas em um arquivo separado

---

## 🎯 Objetivo do Projeto

O objetivo deste processo de ETL foi **disponibilizar um grande volume de dados estruturados em um banco SQL Server** para que a equipe de **Cientistas de Dados** pudesse aplicar regras de **Inteligência de Negócio (BI)** e realizar análises avançadas.

Durante o desenvolvimento, aprendi e apliquei boas práticas relacionadas a:

- Manipulação de dados extensos em Python
- Tratamento e limpeza de dados em larga escala
- Conexão segura e eficiente com bancos de dados
- Otimização de leitura de arquivos CSV grandes com `chunksize`
- Registro e rastreamento de erros para garantir integridade dos dados

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Pandas
- PyODBC
- SQL Server
- CSV (como fonte de dados)

---
