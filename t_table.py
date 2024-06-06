import scipy.stats as stats

# Definindo o nível de significância e graus de liberdade
alpha = 0.01
df = 11

# Calculando o valor crítico superior para um teste bilateral
t_critical_bilateral = stats.t.ppf(1 - alpha / 2, df)
print("Valor crítico superior (bilateral):", t_critical_bilateral)

# Calculando o valor crítico inferior para um teste unilateral à esquerda
t_critical_left = stats.t.ppf(alpha, df)
print("Valor crítico inferior (unilateral à esquerda):", t_critical_left)

# Calculando o valor crítico superior para um teste unilateral à direita
t_critical_right = stats.t.ppf(1 - alpha, df)
print("Valor crítico superior (unilateral à direita):", t_critical_right)
