# 📊 Incident Analysis: SQL vs Pandas

Projeto de análise de incidentes operacionais utilizando **SQL (SQLite)** e **Python (Pandas)**, com o objetivo de responder perguntas de negócio e comparar abordagens de análise de dados.

---

## 🎯 Objetivo

Este projeto tem como objetivo:

- Criar queries SQL para responder perguntas de negócio  
- Realizar análises com Pandas  
- Comparar resultados entre SQL e Python  
- Identificar padrões e gargalos operacionais  

---

## 📂 Estrutura dos Dados

A base de dados representa incidentes operacionais e contém as seguintes colunas:

| Coluna | Descrição |
|------|------|
| id | Identificador do incidente |
| canal | Canal onde ocorreu (App Mobile, Web, API) |
| tipo_incidente | Tipo do incidente |
| prioridade | Nível de prioridade |
| tempo_resolucao | Tempo para resolução (horas) |
| sla | Tempo máximo esperado (SLA) |
| clientes_afetados | Número de clientes impactados |

---

## 🗄️ Tecnologias Utilizadas

- Python  
- Pandas  
- SQLite  
- SQL  
- Git / GitHub  

---

## 🔎 Perguntas de Negócio

O projeto responde às seguintes perguntas:

### 1. Quais são os incidentes mais críticos?
Filtrando incidentes de alta prioridade e agrupando por tipo.

### 2. Qual o maior tempo de resolução?
Identificando o maior tempo registrado entre os incidentes.

### 3. Qual o tempo médio de resolução por canal?
Comparando performance entre App Mobile, Web e API.

---

## 🧠 Abordagens Utilizadas

### 🔹 SQL

Consultas utilizando:

- `SELECT`
- `WHERE`
- `GROUP BY`
- `ORDER BY`
- `AVG`
- `MAX`

---

### 🔹 Pandas

Análises utilizando:

- `groupby()`
- `mean()`
- `max()`
- filtros condicionais
- ordenação de dados

---

## ⚖️ Comparação: SQL vs Pandas

| SQL | Pandas |
|-----|--------|
| Ideal para consultas em banco de dados | Ideal para análise exploratória |
| Mais performático em grandes volumes | Mais flexível para manipulação |
| Sintaxe declarativa | Sintaxe programática |

---

## 📊 Principais Insights

- Incidentes de alta prioridade concentram-se em poucos tipos  
- Determinados canais apresentam maior tempo de resolução  
- Alguns incidentes possuem alto impacto em clientes  
- Possíveis gargalos operacionais podem ser identificados  

---

## 🚨 Possíveis Melhorias

- Priorizar correção de incidentes críticos  
- Reduzir tempo de resolução em canais com maior média  
- Monitorar incidentes recorrentes  
- Criar alertas para eventos críticos  

---

## 👩‍💻 Autora

Projeto desenvolvido por **Iza** como prática de análise de dados, SQL e exploração de KPIs operacionais.
