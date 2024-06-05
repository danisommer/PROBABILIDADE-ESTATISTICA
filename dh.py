import math

# Valores das combinações
C30_9 = math.comb(30, 9)
C24_9 = math.comb(24, 9)
C24_8 = math.comb(24, 8)

# Probabilidades
P_X_0 = C24_9 / C30_9
P_X_1 = (6 * C24_8) / C30_9

# Probabilidade total
P_accepted = P_X_0 + P_X_1

# Exibindo o resultado com 4 casas decimais
print(f'Probabilidade de aceitação do lote: {round(P_accepted, 4)}')
