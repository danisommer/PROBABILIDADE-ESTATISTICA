from scipy.stats import norm

def calcular_valor_z(area, media, desvio_padrao):
    # Usando a função ppf (Percent Point Function) para calcular o valor z
    valor_z = norm.ppf(area, loc=media, scale=desvio_padrao)
    return valor_z

# Valores fornecidos
area = 0.8
media = 18.74
desvio_padrao = 1.01

# Calculando o valor z correspondente
valor_z = calcular_valor_z(area, media, desvio_padrao)
print("O valor z correspondente é:", valor_z)