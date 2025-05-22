from meu_modulo import*



def menu():
    while True:
        print("\n========== CALCULADORA CIVIL ==========")
        print("Escolha uma operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Raiz Quadrada")
        print("6 - Potência")
        print("7 - Seno")
        print("8 - Cosseno")
        print("9 - Tangente")
        print("0 - Sair")
        print("========================================")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            resultado = somar()
            print(f"Resultado da Soma: {resultado}")

        elif opcao == '2':
            resultado = subtrair()
            print(f"Resultado da Subtração: {resultado}")

        elif opcao == '3':
            resultado = multiplicacao()
            print(f"Resultado da Multiplicação: {resultado}")

        elif opcao == '4':
            resultado = divisao()
            print(f"Resultado da Divisão: {resultado}")

        elif opcao == '5':
            resultado = raiz_quadrada()
            print(f"Resultado da Raiz Quadrada: {resultado}")

        elif opcao == '6':
            resultado = potencia()
            print(f"Resultado da Potência: {resultado}")

        elif opcao == '7':
            resultado = seno()
            print(f"Resultado do Seno: {resultado}")

        elif opcao == '8':
            resultado = cosseno()
            print(f"Resultado do Cosseno: {resultado}")

        elif opcao == '9':
            resultado = tangente()
            print(f"Resultado da Tangente: {resultado}")

        elif opcao == '0':
            print("Calculadora encerrada. Até a próxima, Engenheiro!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
