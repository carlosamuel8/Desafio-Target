import json

# Carregar os dados do arquivo JSON
with open('dados.json', 'r') as file:
    dados = json.load(file)

# Filtrar os dias com faturamento maior que zero
faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Cálculos
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = len([valor for valor in faturamento if valor > media_mensal])

# Resultados
print(f"Menor valor de faturamento ocorrido em um dia do mês R$: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento ocorrido em um dia do mês R$: {maior_faturamento:.2f}")
print(f"Número de dias no mês em que o faturamento diário foi superior à média mensal R$: {dias_acima_da_media}")
