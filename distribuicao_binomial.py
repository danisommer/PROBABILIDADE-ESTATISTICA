import math

def calcular_probabilidade(x, n_pos, chance_a, chance_b):
    y = n_pos - x
    z = (chance_a**x) * (chance_b**y) * (math.factorial(n_pos) / (math.factorial(x) * math.factorial(n_pos - x)))
    return z

def probabilidade_acumulada(x, n_pos, chance_a, chance_b):
    z = 0
    for i in range(x, n_pos + 1):
        z += calcular_probabilidade(i, n_pos, chance_a, chance_b)
    return z

def probabilidade_intervalo(x_start, x_end, n_pos, chance_a, chance_b):
    z = 0
    for x in range(x_start, x_end + 1):
        z += calcular_probabilidade(x, n_pos, chance_a, chance_b)
    return z

def main():
    n_pos = int(input("Insira a quantidade de itens da amostra: "))
    chance_a = float(input("Insira a chance de sucesso: "))
    chance_b = 1 - chance_a
    print(f"Esperança: {round(n_pos * chance_a, 4)}")
    print(f"Desvio Padrão: {round(math.sqrt(n_pos * chance_a * chance_b), 4) }")
    print(f"Variância: {round(n_pos * chance_a * chance_b, 4)}")

    while True:
        escolha = input("Deseja calcular a probabilidade para um número exato de itens (E) ou em um intervalo (I)? ").strip().upper()
        match escolha:
            case 'E':
                x = int(input("Insira a quantidade de itens desejados: "))
                if x > n_pos or x < 0:
                    print("Número de itens fora do intervalo permitido. Encerrando...")
                    break
                z = calcular_probabilidade(x, n_pos, chance_a, chance_b)
                z_ac = probabilidade_acumulada(x, n_pos, chance_a, chance_b)
                print(f"A chance de exatamente {x} acontecer é de {round(z,4)}")
                print(f"A chance de pelo menos {x} acontecer é de {round(z_ac,4)}")
        
            case 'I':
                x_start = int(input("Insira o início do intervalo: "))
                x_end = int(input("Insira o fim do intervalo: "))
                if x_start > x_end or x_start < 0 or x_end > n_pos:
                    print("Intervalo inválido. Encerrando...")
                    break
                z_intervalo = probabilidade_intervalo(x_start, x_end, n_pos, chance_a, chance_b)
                print(f"A chance de que a quantidade de itens esteja no intervalo de {x_start} a {x_end} é de {round(z_intervalo, 4)}")
            
            case _:
                print("Opção inválida. Encerrando...")
                break

if __name__ == "__main__":
    main()
