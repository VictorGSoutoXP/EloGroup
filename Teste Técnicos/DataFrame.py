import pandas as pd
from datetime import timedelta

# DataFrame com os dados da imagem
data = {
    'Date': [
        '2020-12-06', '2021-01-15', '2021-01-06', '2021-01-02', '2020-12-24',
        '2020-12-08', '2020-12-09', '2021-01-10', '2021-01-11', '2021-01-12',
        '2021-01-15', '2020-12-17', '2020-12-25', '2020-12-25', '2020-12-25',
        '2021-01-01', '2020-12-06', '2021-01-14', '2021-02-07', '2021-02-10',
        '2021-02-01', '2021-02-01'
    ],
    'account_id': [
        'A1', 'A1', 'A1', 'A1', 'A1',
        'A1', 'A1', 'A2', 'A2', 'A2',
        'A2', 'A2', 'A3', 'A3', 'A3',
        'A3', 'A3', 'A3', 'A1', 'A1',
        'A2', 'A2'
    ],
    'user_id': [
        'U1', 'U2', 'U3', 'U1', 'U2',
        'U1', 'U1', 'U4', 'U4', 'U4',
        'U5', 'U4', 'U6', 'U6', 'U6',
        'U7', 'U6', 'U6', 'U1', 'U2',
        'U4', 'U5'
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Agrupar por usuário
resultados = set()

for user, group in df.groupby('user_id'):
    dias = sorted(group['Date'].unique())
    for i in range(len(dias) - 2):
        if dias[i+1] == dias[i] + timedelta(days=1) and dias[i+2] == dias[i] + timedelta(days=2):
            resultados.add(user)

print("Usuários ativos por 3 dias consecutivos:", resultados)

# Resposta da primeira questão U4 