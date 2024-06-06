import numpy as np

# Dados fornecidos
consumo = np.array([10, 8, 11, 14, 15, 14, 11, 15])
peso = np.array([19, 24, 19, 15, 14, 14, 18, 11])

# Calculando o coeficiente de correlação de Pearson
correlacao = np.corrcoef(consumo, peso)[0, 1]

# Exibindo o resultado
print("Coeficiente de correlação de Pearson:", round(correlacao, 4))
