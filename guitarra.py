import numpy as np
import matplotlib.pyplot as plt

# Definir uma função logarítmica para representar a relação Preço x Qualidade
def qualidade(preco, a=10, b=50):
    return a * np.log(preco) + b

# Intervalo de preços realistas para guitarras, pedais e pedaleiras (em R$)
precos = np.linspace(300, 50000, 100)  # De R$ 500 a R$ 15.000

# Calcular a qualidade percebida para cada preço
qualidades = qualidade(precos)

# Calcular a taxa de crescimento da qualidade (derivada)
derivada_qualidade = np.gradient(qualidades, precos)

# Encontrar o ponto onde a taxa de crescimento desacelera significativamente
ponto_otimo_index = np.argmax(derivada_qualidade < (0.01 * max(derivada_qualidade)))  # Onde a melhoria já é baixa

# Obter o preço correspondente ao ponto ótimo
ponto_otimo_preco = precos[ponto_otimo_index]

# Plotar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(precos, qualidades, label="Qualidade Percebida", color="blue")
plt.axvline(x=ponto_otimo_preco, color="red", linestyle="--", label=f"Ponto Ótimo: R${ponto_otimo_preco:.2f}")
plt.xlabel("Preço (R$)")
plt.ylabel("Qualidade Percebida")
plt.title("Relação entre Preço e Qualidade no Mundo das Guitarras")
plt.legend()
plt.grid()
plt.show()

# Exibir o ponto ótimo de preço no console
print(f"Ponto Ótimo de Preço: R${ponto_otimo_preco:.2f}")

# Preços específicos para análise
preco_3000 = 3000
preco_10000 = 10000
preco_300 = 300
preco_50000 = 50000

# Calcular a qualidade percebida para os preços dados
qualidade_3000 = qualidade(preco_3000)
qualidade_10000 = qualidade(preco_10000)
qualidade_300 = qualidade(preco_300)
qualidade_50000 = qualidade(preco_50000)

# Calcular o ganho percentual de qualidade para os pares de preços e exibir
ganho_percentual_3000_10000 = ((qualidade_10000 - qualidade_3000) / qualidade_3000) * 100
ganho_percentual_300_3000 = ((qualidade_3000 - qualidade_300) / qualidade_300) * 100
ganho_percentual_10000_50000 = ((qualidade_50000 - qualidade_10000) / qualidade_10000) * 100

# Exibir os resultados dos ganhos percentuais no console
print(f"Ganho Percentual de Qualidade de R$3000 para R$10000: {ganho_percentual_3000_10000:.2f}%")
print(f"Ganho Percentual de Qualidade de R$300 para R$3000: {ganho_percentual_300_3000:.2f}%")
print(f"Ganho Percentual de Qualidade de R$10000 para R$50000: {ganho_percentual_10000_50000:.2f}%")
