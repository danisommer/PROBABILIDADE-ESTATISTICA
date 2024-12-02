# Script para simular notas e calcular a média necessária

def calcular_media():
    print("== Simulador de Média Final ==")
    
    # Entrada de notas já obtidas
    P1 = 4.7
    Q1 = 10.0
    
    # Entrada das notas máximas para quizzes restantes
    Q2 = float(input("Digite a nota do Q2 (Quiz 2): "))
    Q3 = float(input("Digite a nota do Q3 (Quiz 3): "))
    
    # Pesos
    peso_provas = 0.8
    peso_quizzes = 0.2
    
    # Meta de média final
    media_alvo = 7.0
    
    # Contribuição dos quizzes
    media_quizzes = (Q1 + Q2 + Q3) / 3
    contrib_quizzes = media_quizzes * peso_quizzes
    
    # Contribuição necessária das provas
    contrib_provas_necessaria = (media_alvo - contrib_quizzes) / peso_provas
    P2_P3_soma_necessaria = contrib_provas_necessaria * 3 - P1
    
    # Média necessária por prova (caso sejam iguais)
    P2_P3_individual_necessaria = P2_P3_soma_necessaria / 2
    
    # Exibir resultados
    print("\n== Resultados ==")
    print(f"Contribuição atual dos quizzes: {contrib_quizzes:.2f}")
    print(f"Soma necessária das notas P2 e P3: {P2_P3_soma_necessaria:.2f}")
    print(f"Média necessária por prova (se iguais): {P2_P3_individual_necessaria:.2f}")
    
    # Verificar se a média é viável
    if P2_P3_individual_necessaria > 10:
        print("Alerta: Não é possível alcançar a média com as notas informadas.")
    else:
        print("É possível alcançar a média com um bom desempenho nas próximas provas.")

# Executar o simulador
calcular_media()