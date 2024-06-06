from sklearn.linear_model import LinearRegression
import numpy as np

# Dados fornecidos
capacidade = np.array([37.5, 48.8, 34.3, 36.3, 43.5, 47.1, 51.8, 39.6])
velocidade = np.array([13, 17, 10, 12, 16, 17, 19, 13])

# Ajustando o modelo de regressão linear
modelo = LinearRegression().fit(velocidade.reshape(-1, 1), capacidade)

# Coeficiente de determinação ajustado
r_squared = modelo.score(velocidade.reshape(-1, 1), capacidade)
n = len(velocidade)
p = 1  # número de variáveis independentes (neste caso, apenas a velocidade)
r_squared_ajustado = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)

# Exibindo o coeficiente de determinação ajustado
print("Coeficiente de determinação ajustado:", round(r_squared_ajustado, 4))
