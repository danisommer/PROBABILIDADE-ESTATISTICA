import math
from scipy.stats import norm

# Dados fornecidos
x_barra = 4971.22
mu_0 = 4970.67
sigma = math.sqrt(100.18)
n = 26

# Cálculo da estatística de teste z
z = (x_barra - mu_0) / (sigma / math.sqrt(n))
z = round(z, 4)

# Cálculo do p-valor para um teste bilateral
p_valor = 2 * (1 - norm.cdf(abs(z)))
p_valor = round(p_valor, 4)

print(f"O valor da estatística de teste z é: {round(z,4)}")
print(f"O p-valor para um teste bilateral é: {round(p_valor,4)}")
