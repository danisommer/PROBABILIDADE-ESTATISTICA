from scipy.stats import norm

# Dados fornecidos
durabilidades = [1978, 1993, 1993, 1990, 1985, 1985, 1988, 1986, 1986, 1989, 1986, 1988]
media_amostral = sum(durabilidades) / len(durabilidades)
desvio_padrao_amostral = ((sum((x - media_amostral) ** 2 for x in durabilidades)) / (len(durabilidades) - 1)) ** 0.5
n = len(durabilidades)
media_hipotese = 1988
significancia = 0.10

# Calculando a estatística do teste (z)
z = (media_amostral - media_hipotese) / (desvio_padrao_amostral / (n ** 0.5))

# Encontrando o ponto crítico (z_crítico)
z_critico = norm.ppf(1 - significancia)

# Determinando se rejeitamos ou não a hipótese nula
rejeita = z > z_critico

# Exibindo os resultados
print("Valor da estatística teste:", round(z, 4))
print("Valor (ponto) crítico do teste:", round(z_critico, 4))
if rejeita:
    print("Rejeita a hipótese nula")
else:
    print("Não rejeita a hipótese nula")
