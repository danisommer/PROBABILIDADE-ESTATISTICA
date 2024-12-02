def sacarDinheiro(JsonValor):
    notas = [100, 50, 20, 10, 5, 2]
    resultado = {}
    valor = JsonValor["valor"]

    for nota in notas:
        quantidade = valor // nota
        valor -= quantidade * nota
        resultado[str(nota)] = quantidade
    
    return resultado

def main():

    json = {
        "valor": 380
    }

    resultado = sacarDinheiro(json)
    
    print(resultado)

if __name__ == "__main__":
    main()
