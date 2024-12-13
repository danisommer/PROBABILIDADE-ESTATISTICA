import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

data = {
    "Q1": [
        0.0, 0.0, 0.0, 0.0, 0.1, 0.2, 0.5, 0.5, 0.5, 
        0.6, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0, 1.0, 1.0, 
        1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.1, 1.2, 
        1.2, 1.2, 1.2, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 
        1.4, 1.4, 1.4, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 
        1.5, 1.6, 1.8, 1.8, 1.8, 1.8, 1.9, 1.9, 1.9, 
        1.9, 2.0, 2.0, 2.0, 2.0, 2.1, 2.1, 2.1, 2.1, 
        2.1, 2.2, 2.2, 2.2, 2.2, 2.3, 2.3, 2.3, 2.3, 
        2.3, 2.5, 2.5, 2.5
    ],
    "Q2": [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
        0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 
        0.5, 0.5, 0.7, 0.8, 0.9, 0.9, 1.0, 1.0, 1.0, 
        1.0, 1.0, 1.0, 1.0, 1.0, 1.2, 1.2, 1.2, 1.3, 
        1.3, 1.3, 1.4, 1.5, 1.5, 1.8, 1.8, 1.8, 1.9, 
        2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.1, 2.1, 2.1, 
        2.1, 2.2, 2.2, 2.3, 2.3, 2.3, 2.3, 2.4, 2.4, 
        2.4, 2.5, 2.5, 2.5
    ],
    "Q3": [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
        0.1, 0.2, 0.2, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 
        0.6, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.8, 
        0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.9, 1.0, 1.0, 
        1.0, 1.0, 1.0, 1.1, 1.2, 1.4, 1.4, 1.4, 1.5, 
        1.5, 1.5, 1.5, 1.7, 1.7, 1.7, 1.7, 1.8, 1.8, 
        1.8, 1.8, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 
        2.0, 2.1, 2.1, 2.2, 2.2, 2.3, 2.3, 2.4, 2.4, 
        2.4, 2.5, 2.5, 2.5
    ],
    "Q4": [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.1, 0.2, 0.3, 0.3, 0.3, 0.5, 0.5, 
        0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.8, 0.8, 0.9, 
        1.0, 1.0, 1.0, 1.0, 1.1, 1.1, 1.2, 1.2, 1.3, 
        1.3, 1.4, 1.4, 1.4, 1.5, 1.5, 1.5, 1.6, 1.6, 
        1.6, 1.7, 1.9, 2.0, 2.0, 2.0, 2.0, 2.1, 2.1, 
        2.1, 2.2, 2.3, 2.3, 2.3, 2.3, 2.3, 2.4, 2.4, 
        2.5, 2.5, 2.5, 2.5
    ],
    "Nota": [
        0.1, 0.2, 0.5, 0.8, 1.0, 1.0, 1.0, 1.2, 1.5, 
        1.6, 1.7, 1.9, 1.9, 2.0, 2.0, 2.1, 2.1, 2.3, 
        2.6, 2.6, 2.8, 3.2, 3.2, 3.4, 3.7, 3.7, 4.0,
        4.2, 4.3, 4.4, 4.5, 4.5, 4.6, 4.7, 4.7, 5.0, 
        5.0, 5.0, 5.0, 5.0, 5.0, 5.1, 5.1, 5.2, 5.3, 
        5.3, 5.5, 5.7, 5.7, 6.0, 6.0, 6.0, 6.0, 6.0, 
        6.2, 6.3, 6.4, 6.4, 6.6, 6.7, 6.8, 7.1, 7.2, 
        7.4, 7.5, 7.5, 7.8, 7.8, 8.0, 8.0, 8.2, 8.7, 
        8.8, 9.1, 9.2, 9.8
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