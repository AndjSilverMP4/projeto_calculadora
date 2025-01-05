import math


def adicionar(numeros):
    return sum(numeros)


def subtrair(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado


def multiplicar(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado


def dividir(numeros):
    resultado = numeros[0]
    try:
        for num in numeros[1:]:
            resultado /= num
    except ZeroDivisionError:
        return "Erro: divisão por zero!"
    return resultado


def exponenciar(numeros):
    base = numeros[0]
    for num in numeros[1:]:
        base **= num
    return base


def raiz_quadrada(numero):
    return math.sqrt(numero)


def logaritmo(numero, base=10):
    return math.log(numero, base)


def seno(numero):
    return math.sin(math.radians(numero))


def cosseno(numero):
    return math.cos(math.radians(numero))


def tangente(numero):
    return math.tan(math.radians(numero))


def fatorial(numero):
    if numero < 0:
        return "Erro: fatorial de número negativo!"
    return math.factorial(numero)


def radianos_para_graus(numero):
    return math.degrees(numero)


def graus_para_radianos(numero):
    return math.radians(numero)


def modulo(x, y):
    return x % y


print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Exponenciação")
print("6. Raiz Quadrada")
print("7. Logaritmo")
print("8. Seno")
print("9. Cosseno")
print("10. Tangente")
print("11. Fatorial")
print("12. Radianos para Graus")
print("13. Graus para Radianos")
print("14. Módulo")

while True:
    escolha = input("Digite sua escolha (1/2/3/4/5/6/7/8/9/10/11/12/13/14): ")

    if escolha in ["1", "2", "3", "4", "5"]:
        numeros = list(
            map(float, input("Digite os números separados por espaço: ").split())
        )

        if escolha == "1":
            print("Resultado:", adicionar(numeros))

        elif escolha == "2":
            print("Resultado:", subtrair(numeros))

        elif escolha == "3":
            print("Resultado:", multiplicar(numeros))

        elif escolha == "4":
            print("Resultado:", dividir(numeros))

        elif escolha == "5":
            print("Resultado:", exponenciar(numeros))

    elif escolha in ["6", "7", "8", "9", "10", "11", "12", "13"]:
        numero = float(input("Digite o número: "))

        if escolha == "6":
            print("Resultado:", raiz_quadrada(numero))

        elif escolha == "7":
            base = float(input("Digite a base do logaritmo (padrão é 10): ") or 10)
            print("Resultado:", logaritmo(numero, base))

        elif escolha == "8":
            print("Resultado:", seno(numero))

        elif escolha == "9":
            print("Resultado:", cosseno(numero))

        elif escolha == "10":
            print("Resultado:", tangente(numero))

        elif escolha == "11":
            print("Resultado:", fatorial(numero))

        elif escolha == "12":
            print("Resultado:", radianos_para_graus(numero))

        elif escolha == "13":
            print("Resultado:", graus_para_radianos(numero))

    elif escolha == "14":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado:", modulo(num1, num2))

    else:
        print("Opção inválida. Tente novamente.")
