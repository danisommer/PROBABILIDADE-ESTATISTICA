import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

notas = np.array([1]*4 + [2]*7 + [3]*13 + [4]*11 + [5]*4)

kde = gaussian_kde(notas, bw_method=0.5)

x = np.linspace(0, 6, 1000)

y = kde(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='b', lw=2)
plt.fill_between(x, y, color='blue', alpha=0.3)
plt.title("Curva de Distribuição das Notas da Turma")
plt.xlabel("Nota")
plt.ylabel("Densidade de Probabilidade")
plt.grid(True)
plt.show()
