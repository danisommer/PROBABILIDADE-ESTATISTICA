import numpy as np
import scipy.stats as stats

# Dados
notas = np.array([67, 69, 65, 72, 70, 67, 74, 70, 71, 67, 73])
n = len(notas)
alpha = 0.10
variancia_hipotetica = 8

# Calcular a variância da amostra
variancia_amostra = np.var(notas, ddof=1)

# Calcular a estatística do teste
chi2_teste = (n - 1) * variancia_amostra / variancia_hipotetica
print(f"Estatística do teste: {round(chi2_teste,4)}")

# Calcular os valores críticos para um teste bilateral
chi2_critical_inferior = stats.chi2.ppf(alpha / 2, n - 1)
chi2_critical_superior = stats.chi2.ppf(1 - alpha / 2, n - 1)
print(f"Valor crítico inferior: {round(chi2_critical_inferior, 4)}")
print(f"Valor crítico superior: {round(chi2_critical_superior,4)}")

# Decisão
if chi2_teste < chi2_critical_inferior or chi2_teste > chi2_critical_superior:
    print("Rejeita H0")
else:
    print("Não rejeita H0")
