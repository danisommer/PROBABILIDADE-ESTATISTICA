import numpy as np

# Dados fornecidos
idades = np.array([33, 22, 8, 33, 49, 50, 24, 17, 18, 42, 48, 10, 32, 27, 17, 49])
alugueis = np.array([1827, 1906, 1967, 1818, 1755, 1747, 1888, 1966, 1946, 1776, 1748, 2014, 1868, 1862, 1930, 1726])

# Calculando a correlação de Pearson
correlacao = np.corrcoef(idades, alugueis)[0, 1]

# Calculando os coeficientes da regressão linear
A = np.vstack([idades, np.ones(len(idades))]).T
m, c = np.linalg.lstsq(A, alugueis, rcond=None)[0]

# Imprimindo os resultados
print("O coeficiente de correlação de Pearson:", round(correlacao, 4))
print("O coeficiente linear estimado:", round(c, 4))
print("O coeficiente angular estimado:", round(m, 4))

# Calculando o valor estimado do aluguel para uma casa com 9 anos
anos = 9
valor_estimado = m * anos + c
print("O valor estimado do aluguel para uma casa com 9 anos:", round(valor_estimado, 4))
