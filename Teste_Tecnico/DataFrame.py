# Contexto
# A EloGroup lançou um aplicativo interno para cadastro e acompanhamento de projetos, visando ter maior assertividade na governança e gestão dos projetos.
import pandas as pd

# Dados corrigidos conforme a tabela visível no desafio (datas em 2022/2023)
data = {
    'Date': [
        '2023-01-01', '2023-01-01', '2023-01-06', '2023-01-02',
        '2022-12-24', '2022-12-08', '2022-11-09', '2023-01-10', '2023-01-11',
        '2023-01-12', '2023-01-15', '2022-12-17', '2022-12-25', '2022-12-25',
        '2022-12-06', '2023-01-01', '2022-12-06', '2023-01-14',
        '2023-02-07', '2023-02-10', '2023-02-01', '2023-01-01', '2022-12-05'
    ],
    'account_id': [
        'A1', 'A1', 'A1', 'A1',
        'A1', 'A1', 'A1', 'A2', 'A2',
        'A2', 'A2', 'A2', 'A3', 'A3',
        'A3', 'A3', 'A3', 'A4',
        'A1', 'A1', 'A2', 'A2', 'A1'
    ],
    'user_id': [
        'USER1', 'USER2', 'USER3', 'USER1',
        'USER2', 'USER1', 'USER1', 'USER4', 'USER4',
        'USER4', 'USER5', 'USER4', 'USER6', 'USER6',
        'USER7', 'USER6', 'USER6', 'USER6',
        'USER1', 'USER2', 'USER4', 'USER5', 'USER8'
    ]
}

# Cria o DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Filtra dados por mês
dez_2022 = df[(df['Date'].dt.year == 2022) & (df['Date'].dt.month == 12)]
jan_2023 = df[(df['Date'].dt.year == 2023) & (df['Date'].dt.month == 1)]

# Calcula taxa de retenção por account_id
retencao = []

for conta in df['account_id'].unique():
    usuarios_dez = set(dez_2022[dez_2022['account_id'] == conta]['user_id'])
    usuarios_jan = set(jan_2023[jan_2023['account_id'] == conta]['user_id'])

    if usuarios_dez:
        taxa = len(usuarios_dez & usuarios_jan) / len(usuarios_dez)
        retencao.append((conta, round(taxa * 100, 2)))  # percentual
    else:
        retencao.append((conta, 0.0))  # nenhum usuário em dez/22

# Mostra resultados ordenados
retencao.sort(key=lambda x: x[1], reverse=True)

for conta, taxa in retencao:
    print(f'Account: {conta} - Taxa de Retenção: {taxa}%')

# Qual teve a maior retenção?
print("\nAccount com maior retenção:", retencao[0][0])
