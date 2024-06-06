import numpy as np
from scipy.stats import f, t

# Dados fornecidos
notas_turma_A = np.array([78, 66, 73, 79, 81, 81, 76, 76])
notas_turma_B = np.array([61, 55, 56, 57, 54, 68, 58, 50])

# Tamanho das amostras
n_A = len(notas_turma_A)
n_B = len(notas_turma_B)

# Variâncias das amostras
var_A = np.var(notas_turma_A, ddof=1)
var_B = np.var(notas_turma_B, ddof=1)

# Teste de igualdade de variâncias (Teste F)
f_statistic = var_A / var_B
dfn = n_A - 1
dfd = n_B - 1
f_critical_upper = f.ppf(0.975, dfn, dfd)

# Teste de igualdade de médias (Teste t para variâncias iguais)
mean_A = np.mean(notas_turma_A)
mean_B = np.mean(notas_turma_B)
pooled_var = ((n_A - 1) * var_A + (n_B - 1) * var_B) / (n_A + n_B - 2)
se = np.sqrt(pooled_var * (1/n_A + 1/n_B))

t_statistic = (mean_A - mean_B) / se
df_t = n_A + n_B - 2
t_critical_upper = t.ppf(0.975, df_t)

# Resultados
print(f"Valor da estatística teste F: {round(f_statistic,4)}")
print(f"Valor da estatística teste t: {round(t_statistic,4)}")
print(f"Valor crítico superior do teste F: {round(f_critical_upper,4)}")
print(f"Valor crítico superior do teste t: {round(t_critical_upper,4)}")
