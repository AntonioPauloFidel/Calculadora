import math


def somar():
    soma = 0
    while True:
        num = input("Digite um número para somar (ou 'sair' para encerrar): ")
        if num.lower() == 'sair':
            break
        soma += float(num)
    return soma


def subtrair():
    resultado = float(input("Digite o valor inicial: "))
    while True:
        num = input("Digite o valor para subtrair (ou 'sair' para encerrar): ")
        if num.lower() == 'sair':
            break
        resultado -= float(num)
    return resultado


def multiplicacao():
    resultado = float(input("Digite o valor inicial: "))
    while True:
        num = input("Digite um valor para multiplicar (ou 'sair' para encerrar): ")
        if num.lower() == 'sair':
            break
        resultado *= float(num)
    return resultado


def divisao():
    resultado = float(input("Digite o valor inicial: "))
    while True:
        num = input("Digite o divisor (ou 'sair' para encerrar): ")
        if num.lower() == 'sair':
            break
        if num == '0':
            print("divisão por zero não é permitida.")
            continue
        resultado /= float(num)
    return resultado


def raiz_quadrada():
    num = input("Digite o número para calcular a raiz quadrada: ")
    if float(num) < 0:
        print("Não existe raiz de número negativo.")
        return None
    return math.sqrt(float(num))


def potencia():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    return math.pow(base, expoente)


def seno():
    angulo = float(input("Digite o ângulo em graus: "))
    return math.sin(math.radians(angulo))


def cosseno():
    angulo = float(input("Digite o ângulo em graus: "))
    return math.cos(math.radians(angulo))


def tangente():
    angulo = float(input("Digite o ângulo em graus: "))
    return math.tan(math.radians(angulo))
