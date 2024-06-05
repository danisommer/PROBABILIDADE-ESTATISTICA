from scipy.stats import poisson

# Número médio de partículas
media = 2

# P(X=5)
prob_X_5 = poisson.pmf(5, media)

# P(X>7) = 1 - P(X<=7)
prob_X_maior_que_7 = 1 - poisson.cdf(7, media)

# P(X<=9)
prob_X_menor_ou_igual_a_9 = poisson.cdf(9, media)

# P(3<X<=4) = P(X<=4) - P(X<=3)
prob_entre_3_e_4 = poisson.cdf(4, media) - poisson.cdf(3, media)

# Exibindo os resultados
print("P(X=5): {:.4f}".format(prob_X_5))
print("P(X>7): {:.4f}".format(prob_X_maior_que_7))
print("P(X<=9): {:.4f}".format(prob_X_menor_ou_igual_a_9))
print("P(3<X<=4): {:.4f}".format(prob_entre_3_e_4))
