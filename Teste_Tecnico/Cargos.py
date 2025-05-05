#Contexto:
# A EloGroup foi acionada por uma grande de minério com o propósito de realizar um projeto de People Analytics, que visa analisar as pessoas, os cargos,
# salários e quantidade de mulheres em cargos de liderença para, assim, garantir equidade dos salários.
import pandas as pd
import locale

# Define locale brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Tabela Workers com dados reais do enunciado
workers = pd.DataFrame({
    'worker_id': [1,2,3,4,5,6,7,8,9,10,11,12],
    'name': ['Lucas','Arthur','Alfred','Thiago','Thais','Angela','Ramon','Bernado','Ligia','Rafael','Nadine','Luan'],
    'last_name': ['Mendes','Vern','Singal','Kumar','Argônio','Patel','Silva','Costa','Lamas','Meira','Schmit','Lien'],
    'salary': [100000, 80000, 300000, 500000, 500000, 200000, 75000, 90000, 70000, 65000, 75000, 85000],
    'joining_date': ['20/02/2014','11/06/2014','20/02/2014','20/02/2014','11/06/2014','11/06/2014','20/01/2014',
                     '10/04/2014','11/04/2015','11/04/2015','20/03/2014','21/03/2014'],
    'department': ['RH','Administrador','RH','Administrador','Administrador','Contas a pagar','Contas a pagar',
                   'TI','TI','TI','Contas a pagar','RH']
})

# Tabela Titles conforme o desafio
titles = pd.DataFrame({
    'worker_ref_id': [1,2,3,4,5,6,7,8],
    'worker_title': ['Gerente','Executivo','Executivo','Gerente','Gerente Associado','Gerente de projetos','Líder','Líder'],
    'affected_from': ['20/02/2016','11/06/2016','11/06/2016','11/06/2016','11/06/2016','11/06/2016','11/06/2016','11/06/2016']
})

# Merge entre workers e titles
merged = pd.merge(workers, titles, how='inner', left_on='worker_id', right_on='worker_ref_id')

# Calcula média salarial por cargo
media_por_cargo = (
    merged.groupby('worker_title')['salary']
    .mean()
    .reset_index()
    .sort_values(by='salary', ascending=False)
    .reset_index(drop=True)
)

# Formata como R$ e adiciona ranking
media_por_cargo['salario_formatado'] = media_por_cargo['salary'].apply(lambda x: locale.currency(x, grouping=True))
media_por_cargo['ranking'] = media_por_cargo.index + 1

# Exibe o resultado final
print("🏆 Ranking dos Cargos com Maiores Salários Médios:\n")
print(media_por_cargo[['ranking', 'worker_title', 'salario_formatado']])

# Resposta:
# A questão pede que seja calculado o cargo com maior salário médio,
# usando apenas os dados disponíveis nas duas tabelas.
# Como foi feito um INNER JOIN, somente trabalhadores com cargo definido foram considerados.
# Com base nesses dados, o cargo com maior salário médio é: O único Gerente Associado é a Thais, com R$ 5.000.000

