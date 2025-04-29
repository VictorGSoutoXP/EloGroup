import pandas as pd

# Dados simulados com base na tabela da imagem
data = [
    ['2023-01-01', 'A1', 'USER1'],
    ['2023-01-01', 'A1', 'USER2'],
    ['2023-01-06', 'A1', 'USER3'],
    ['2023-01-02', 'A1', 'USER1'],
    ['2022-12-24', 'A1', 'USER2'],
    ['2022-12-08', 'A1', 'USER1'],
    ['2022-12-09', 'A1', 'USER1'],
    ['2023-01-10', 'A2', 'USER4'],
    ['2023-01-11', 'A2', 'USER4'],
    ['2023-01-12', 'A2', 'USER4'],
    ['2023-01-15', 'A2', 'USER5'],
    ['2022-12-17', 'A2', 'USER4'],
    ['2022-12-25', 'A3', 'USER6'],
    ['2022-12-25', 'A3', 'USER6'],
    ['2022-12-06', 'A3', 'USER6'],
    ['2022-12-06', 'A3', 'USER7'],
    ['2023-01-14', 'A4', 'USER6'],
    ['2023-02-07', 'A1', 'USER1'],
    ['2023-02-10', 'A1', 'USER2'],
    ['2023-01-01', 'A4', 'USER6'],
    ['2023-01-02', 'A4', 'USER6'],
    ['2023-01-02', 'A2', 'USER5'],
    ['2022-12-05', 'A1', 'USER8'],
]

df = pd.DataFrame(data, columns=['Date', 'account_id', 'user_id'])
df['Date'] = pd.to_datetime(df['Date'])

# Separar dezembro/22 e janeiro/23
dez = df[(df['Date'].dt.month == 12) & (df['Date'].dt.year == 2022)]
jan = df[(df['Date'].dt.month == 1) & (df['Date'].dt.year == 2023)]

# Agrupar usuários únicos por account_id em cada mês
dez_users = dez.groupby('account_id')['user_id'].apply(set)
jan_users = jan.groupby('account_id')['user_id'].apply(set)

# Calcular taxa de retenção por account_id
retencao = {}

for acc in dez_users.index:
    if acc in jan_users:
        qtd_dez = len(dez_users[acc])
        qtd_retentos = len(dez_users[acc].intersection(jan_users[acc]))
        taxa = (qtd_retentos / qtd_dez) * 100 if qtd_dez > 0 else 0
        retencao[acc] = round(taxa, 2)
    else:
        retencao[acc] = 0.0

# Resultado
print("Taxa de retenção por account_id:")
for k, v in retencao.items():
    print(f"{k}: {v}%")

# Identificar maior taxa
maior = max(retencao.values())
melhores = [k for k, v in retencao.items() if v == maior]
print("Maior taxa de retenção:", melhores)
