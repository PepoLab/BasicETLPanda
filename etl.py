import pandas as pd
from sqlalchemy import create_engine
import urllib

# ETAPA 1 - EXTRAÇÃO
df = pd.read_csv('dados.csv')

# ETAPA 2 - TRANSFORMAÇÃO
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
df['nova_coluna'] = df['coluna_existente'].apply(lambda x: x * 2)

# ETAPA 3 - CARGA (Windows Authentication no SQL Server)
server = 'NOME_DO_SERVIDOR\\INSTANCIA'  # exemplo: 'localhost\\SQLEXPRESS'
database = 'NOME_DO_BANCO'

params = urllib.parse.quote_plus(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
)

engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')

df.to_sql('nome_da_tabela_destino', engine, if_exists='replace', index=False)

print("ETL concluído com sucesso.")