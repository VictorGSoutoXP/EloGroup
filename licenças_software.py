#Contexto:
# Com o atual crescimento da companhia, nos deparamos com a necessidade de auditar as licenças de softwares da empresa, 
# com o objetivo de entender quais colaboradores realmetne têm acesso ao sistema e o utiliza de forma recorrente, a fim de ceder licenças apenas quem de fato o utiliza.
import pandas as pd
from datetime import timedelta

# Dados da imagem
data = [
    ['2020-12-06', 'A1', 'U1'],
    ['2021-01-15', 'A1', 'U2'],
    ['2021-01-06', 'A1', 'U3'],
    ['2021-01-02', 'A1', 'U1'],
    ['2020-12-24', 'A1', 'U2'],
    ['2020-12-08', 'A1', 'U1'],
    ['2020-12-09', 'A1', 'U1'],
    ['2021-01-10', 'A2', 'U4'],
    ['2021-01-11', 'A2', 'U4'],
    ['2021-01-12', 'A2', 'U4'],
    ['2021-01-15', 'A2', 'U5'],
    ['2020-12-17', 'A2', 'U4'],
    ['2020-12-25', 'A3', 'U6'],
    ['2020-12-25', 'A3', 'U6'],
    ['2020-12-06', 'A3', 'U6'],
    ['2021-01-01', 'A3', 'U7'],
    ['2021-01-14', 'A3', 'U6'],
    ['2021-02-07', 'A1', 'U1'],
    ['2021-02-10', 'A1', 'U2'],
    ['2021-02-01', 'A2', 'U4'],
    ['2021-02-01', 'A2', 'U5'],
    ['2020-12-05', 'A1', 'U8'],
]

# Criar DataFrame
df = pd.DataFrame(data, columns=['Date', 'account_id', 'user_id'])
df['Date'] = pd.to_datetime(df['Date'])

# Identificar usuários ativos por 3 dias consecutivos
usuarios_ativos = set()

for user, grupo in df.groupby('user_id'):
    datas = grupo['Date'].sort_values().tolist()
    for i in range(len(datas) - 2):
        if datas[i + 1] == datas[i] + timedelta(days=1) and datas[i + 2] == datas[i] + timedelta(days=2):
            usuarios_ativos.add(user)
            break

# Exibir resultado
print(f"Usuário com atividade por 3 dias consecutivos: {', '.join(sorted(usuarios_ativos))}")
print(f"Total de usuários ativos por 3 dias consecutivos: {len(usuarios_ativos)}")
