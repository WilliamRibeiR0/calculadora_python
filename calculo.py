def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return " Invalido pois não é possível dividir por zero!"
    return a / b

def calculadora():
    print("""
============================================
                CALCULADORA
============================================
    Selecione a operação:
    [1] - Soma
    [2] - Subtração
    [3] - Multiplicação
    [4] - Divisão
============================================
""")

    operacao = int(input("Insira a opção:"))

    if operacao in [1, 2, 3, 4]:
        
        num1 = float(input("Digite o primeiro:"))
        num2 = float(input("Digite o segundo:"))

        if operacao == 1:
            print(f"A soma entre {num1} + {num2} é = {soma(num1, num2)}")
        elif operacao == 2:
            print(f"A Subtração entre {num1} - {num2} é = {subtracao(num1, num2)}")
        elif operacao == 3:
            print(f"A Multiplicação entre {num1} x {num2} é = {multiplicacao(num1, num2)}")
        elif operacao == 4:
            print(f"A Divisão entre {num1} / {num2} é = {divisao(num1, num2)}")
    else:
        print("Valor invalido!")

calculadora()