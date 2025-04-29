import pandas as pd

# Tabela Workers com salários corrigidos (valores reais com todos os zeros)
workers = pd.DataFrame({
    'worker_id': [1,2,3,4,5,6,7,8,9,10,11,12],
    'name': ['Lucas','Arthur','Alfred','Thiago','Thais','Angela','Ramon','Bernado','Ligia','Rafael','Nadine','Luan'],
    'last_name': ['Mendes','Vern','Singal','Kumar','Argônio','Patel','Silva','Costa','Lamas','Meira','Schmit','Lien'],
    'salary': [1000000, 800000, 3000000, 5000000, 5000000, 2000000, 750000, 900000, 700000, 650000, 750000, 850000],
    'joining_date': ['20/02/2014','11/06/2014','20/02/2014','20/02/2014','11/06/2014','11/06/2014','20/01/2014',
                     '10/04/2014','11/04/2015','11/04/2015','20/03/2014','21/03/2014'],
    'department': ['RH','Administrador','RH','Administrador','Administrador','Contas a pagar','Contas a pagar',
                   'TI','TI','TI','Contas a pagar','RH']
})

# Tabela Titles
titles = pd.DataFrame({
    'worker_ref_id': [1,2,3,4,5,6,7,8],
    'worker_title': ['Gerente','Executivo','Executivo','Gerente','Gerente Associado','Gerente de projetos','Líder','Líder'],
    'affected_from': ['20/02/2016','11/06/2016','11/06/2016','11/06/2016','11/06/2016','11/06/2016','11/06/2016','11/06/2016']
})

# Merge entre as tabelas usando apenas registros com cargos definidos
merged = pd.merge(workers, titles, how='inner', left_on='worker_id', right_on='worker_ref_id')

# Agrupamento por cargo e cálculo da média salarial
media_por_cargo = merged.groupby('worker_title')['salary'].mean().reset_index()

# Encontrar o(s) cargo(s) com maior salário médio
salario_max = media_por_cargo['salary'].max()
cargos_top = media_por_cargo[media_por_cargo['salary'] == salario_max]

# Impressão do resultado
print("Cargos com os maiores salários médios:")
print(cargos_top)


# Resposta:
# A questão pede que seja calculado o cargo com maior salário médio,
# usando apenas os dados disponíveis nas duas tabelas.
# Como foi feito um INNER JOIN, somente trabalhadores com cargo definido foram considerados.
# Com base nesses dados, o cargo com maior salário médio é: O único Gerente Associado é a Thais, com R$ 5.000.000

