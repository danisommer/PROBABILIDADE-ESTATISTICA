# Script para simular notas e calcular a média necessária

def calcular_media():
    print("== Simulador de Média Final ==")
    
    # Entrada de notas já obtidas
    P1 = 4.7
    P2 = float(input("Digite a nota da P2: "))
    P3 = float(input("Digite a nota da P3: "))

    Q1 = 10.0
    Q2 = 2.5

    Q3 = float(input("Digite a nota do Q3 (Quiz 3): "))
    
    # Pesos
    peso_provas = 0.8
    peso_quizzes = 0.2
    
    # Meta de média final
    media_alvo = 6.0
    
    # Contribuição dos quizzes
    media_quizzes = (Q1 + Q2 + Q3) / 3
    contrib_quizzes = media_quizzes * peso_quizzes
    
    # Contribuição necessária das provas
    media_provas = (P1 + P2 + P3) / 3
    contrib_provas = media_provas * peso_provas
    
    # Calcular média final
    media_final = contrib_provas + contrib_quizzes 
    print(f"Média final: {media_final:.2f}")
# Executar o simulador
calcular_media()