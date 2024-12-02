import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

data = {

    "Q1": [
        1.1, 1.2, 2.2, 0.5, 0.0, 2.0, 1.0, 2.1, 1.2, 1.3, 
        1.0, 2.1, 0.0, 0.8, 0.1, 1.5, 1.3, 0.9, 2.1, 2.1, 
        0.0, 1.0, 1.5, 0.5, 2.3, 0.8, 0.2, 1.3, 1.5, 1.5, 
        2.3, 2.5, 0.0, 2.0, 1.3, 1.5, 1.5
    ],
    "Q2": [
        0.0, 1.0, 1.0, 0.2, 0.5, 2.0, 0.2, 2.1, 2.3, 0.0,
        0.7, 2.4, 0.0, 0.0, 2.0, 1.5, 2.1, 0.0, 1.0, 2.1,
        0.0, 2.2, 0.0, 1.2, 0.2, 0.2, 0.2, 0.0, 2.2, 2.0,
        1.8, 2.3, 0.5, 1.9, 0.3, 1.5, 0.5
    ],
    "Q3": [
        1.0, 2.0, 2.4, 0.0, 0.0, 0.7, 0.7, 1.0, 0.7, 2.1,
        0.0, 2.3, 0.2, 0.0, 2.0, 0.7, 1.7, 0.5, 1.5, 1.5,
        0.1, 1.4, 0.0, 1.7, 2.0, 0.6, 0.5, 1.4, 1.4, 2.0,
        1.5, 2.5, 0.7, 2.4, 2.0, 2.3, 1.0
    ],
    "Q4": [
        0.0, 0.5, 1.2, 0.5, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0,
        0.0, 2.3, 0.0, 0.0, 0.5, 1.3, 0.6, 0.2, 2.5, 0.3,
        0.0, 0.6, 0.0, 1.1, 0.5, 0.3, 0.1, 2.3, 0.0, 2.3,
        1.0, 1.5, 0.8, 2.4, 1.4, 2.2, 1.5
    ],
    "Nota": [
        2.1, 4.7, 6.8, 1.2, 0.5, 4.7, 1.9, 7.2, 4.2, 3.4,
        1.7, 9.1, 0.2, 0.8, 4.6, 5.0, 5.7, 1.6, 7.1, 6.0,
        0.1, 5.2, 1.5, 4.5, 5.0, 1.9, 1.0, 5.0, 5.1, 7.8,
        6.6, 8.8, 2.0, 8.7, 5.0, 7.5, 4.5
    ]
}

df = pd.DataFrame(data)

# Cálculos
max_score = df["Nota"].max()
min_score = df["Nota"].min()
average_score = df["Nota"].mean()

# Alunos com maior e menor nota
best_students = df[df["Nota"] == max_score]
worst_students = df[df["Nota"] == min_score]

# Desvio padrão
std_dev = df["Nota"].std()

# Médias por questão
average_q1 = df["Q1"].mean()
std_dev_q1 = df["Q1"].std()
average_q2 = df["Q2"].mean()
std_dev_q2 = df["Q2"].std()
average_q3 = df["Q3"].mean()
std_dev_q3 = df["Q3"].std()
average_q4 = df["Q4"].mean()
std_dev_q4 = df["Q4"].std()

# Exibir resultados
print("Resumo da Prova")
print("================")
print(f"Maior Nota: {max_score}")
print(f"Menor Nota: {min_score}")
print(f"Nota Média: {average_score:.2f}", f"Desvio Padrão: {std_dev:.2f}")
print(f"Média Q1: {average_q1:.2f}", f"Desvio Padrão Q1: {std_dev_q1:.2f}")
print(f"Média Q2: {average_q2:.2f}", f"Desvio Padrão Q2: {std_dev_q2:.2f}")
print(f"Média Q3: {average_q3:.2f}", f"Desvio Padrão Q3: {std_dev_q3:.2f}")
print(f"Média Q4: {average_q4:.2f}", f"Desvio Padrão Q4: {std_dev_q4:.2f}")
print(sorted(df["Nota"].values))

# Criar a grade de valores para o eixo x
x_nota = np.linspace(min_score - 1, max_score + 1, 500)
x_q1 = np.linspace(df["Q1"].min() - 0.5, df["Q1"].max() + 0.5, 500)
x_q2 = np.linspace(df["Q2"].min() - 0.5, df["Q2"].max() + 0.5, 500)
x_q3 = np.linspace(df["Q3"].min() - 0.5, df["Q3"].max() + 0.5, 500)
x_q4 = np.linspace(df["Q4"].min() - 0.5, df["Q4"].max() + 0.5, 500)

# Calcular as PDFs
pdf_nota = norm.pdf(x_nota, loc=average_score, scale=std_dev)
pdf_q1 = norm.pdf(x_q1, loc=average_q1, scale=std_dev_q1)
pdf_q2 = norm.pdf(x_q2, loc=average_q2, scale=std_dev_q2)
pdf_q3 = norm.pdf(x_q3, loc=average_q3, scale=std_dev_q3)
pdf_q4 = norm.pdf(x_q4, loc=average_q4, scale=std_dev_q4)

# Plotar todas as distribuições em um único gráfico
plt.figure(figsize=(10, 6))

plt.plot(x_nota, pdf_nota, label="Nota Final", color='blue')
plt.plot(x_q1, pdf_q1, label="Q1", color='green')
plt.plot(x_q2, pdf_q2, label="Q2", color='red')
plt.plot(x_q3, pdf_q3, label="Q3", color='purple')
plt.plot(x_q4, pdf_q4, label="Q4", color='orange')

plt.title("Distribuições das Notas e Questões")
plt.xlabel("Valor")
plt.ylabel("Densidade de Probabilidade")
plt.grid(True)
plt.legend()

plt.show()