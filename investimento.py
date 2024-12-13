total_nao_investido = 850  # Montante inicial em reais
total_investido = 2020  # Total investido inicialmente (em reais)
salario_mensal = 1100  # Salário mensal (em reais)
depositos_mensais = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]  # Depósitos mensais para cada mês
gastos_mensais = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Gastos mensais para cada mês
taxa_mensal = 0.01  # Taxa de rendimento mensal fixa (1% ao mês)
meses = len(depositos_mensais)  # Tempo investido (12 meses)

for i in range(meses):
    total_investido += depositos_mensais[i]
    total_investido *= (1 + taxa_mensal)
    total_nao_investido += (salario_mensal - depositos_mensais[i] - gastos_mensais[i])

print(f"{(total_nao_investido + total_investido):.2f}")
