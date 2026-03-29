import sqlite3
import pandas as pd

# PASSO 1: Criar banco de dados e tabela

# criando conexão com banco SQLite (oarquivo será criado automaticamente)
conn = sqlite3.connect("incidentes.db")

# criando cursor (permite executar comandos SQL)
cursor = conn.cursor()

# criando tabela de incidentes
cursor.execute("""
CREATE TABLE IF NOT EXISTS incidentes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    canal TEXT,
    tipo_incidente TEXT,
    prioridade TEXT,
    tempo_resolucao REAL,
    sla REAL,
    clientes_afetados INTEGER
    )
""")

#----------------------------------------
# PASSO 2: Inserir dados na tabela

dados = [
    ("App Mobile", "Erro Login", "Alta", 2.0, 2.0, 500),
    ("Web", "Lentidão", "Média", 5.0, 4, 200),
    ("API", "Timeout", "Alta", 6.0, 2, 1000),
    ("App Mobile", "Erro Login", "Alta", 3.0, 2, 800),
    ("Web", "Erro Pagamento", "Alta", 4.5, 4, 600),
]

cursor.executemany("""
INSERT INTO incidentes 
    (canal, tipo_incidente, prioridade, tempo_resolucao, sla, clientes_afetados)
VALUES 
    (?, ?, ?, ?, ?, ?)
""", dados)

conn.commit()

#----------------------------------------
# PASSO 3: Perguntas de negócio com SQL

# 1. Quais incidentes mais críticos?
query1 = """
SELECT tipo_incidente, COUNT(*) as total FROM incidentes
WHERE prioridade = 'Alta'
GROUP BY tipo_incidente
ORDER BY total DESC
"""

df_sql_criticos = pd.read_sql(query1, conn)
print("\nIncidentes mais críticos:")
print(df_sql_criticos)

# 2. Qual o maior tempo de resolução?
query2 = """
SELECT MAX(tempo_resolucao) as maior_tempo FROM incidentes
"""

df_sql_tempo = pd.read_sql(query2, conn)
print("\nMaior tempo de resolução:")
print(df_sql_tempo)

# 3. Qual o tempo médio de resolução por canal?
query3 = """
SELECT canal, AVG(tempo_resolucao) as tempo_medio FROM incidentes
GROUP BY canal
ORDER BY tempo_medio DESC
"""

df_sql_canal = pd.read_sql(query3, conn)
print("\nTempo médio por canal:")
print(df_sql_canal)

#----------------------------------------
# PASSO 4: Comparação com Pandas

# criar DataFrame
df = pd.read_sql("SELECT * FROM incidentes", conn)

# 1. Quais incidentes mais críticos? pandas
df_criticos = (
    df[df["prioridade"] == "Alta"]
    .groupby("tipo_incidente")
    .size()
    .reset_index(name="total")
    .sort_values(by="total", ascending=False)
)

print("\n[PANDAS] Incidentes mais críticos:")
print(df_criticos)

# 2. Maior tempo de resolução? pandas

print("\n[PANDAS] Maior tempo de resolução:")
print(df["tempo_resolucao"].max())

# 3. Tempo médio de resolução por canal? pandas

df_canal = (
    df.groupby("canal")["tempo_resolucao"]
    .mean()
    .reset_index()
    .sort_values(by="tempo_resolucao", ascending=False)
)

print("\n[PANDAS] Tempo médio por canal:")
print(df_canal)