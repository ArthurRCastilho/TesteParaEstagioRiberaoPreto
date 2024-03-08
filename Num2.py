# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será 
# a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um 
# programa na linguagem que desejar onde, informado um número, ele calcule a sequência de 
# Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# ===================

# 01 Cria uma função para Verficação
def verificaFibonacci(valor):

    # 02 Inicia o a fibonnacci com 0 no primeiro valor
    fibonacci = [0 , 1]
    
    #03 Cria um while para adicionar valores a sequencia do Fibonacci
    while fibonacci[-1] <= valor:

        # 04 Faz-se a soma entre o primeiro e o segundo valor
        proximo_valor = fibonacci[-1] + fibonacci[-2]

        # 05 Adiciona a lista o valor a lista do fibonacci
        fibonacci.append(proximo_valor)

    # 06 Verifica se o valor está dentro da sequencia Fibonacci
    if valor in fibonacci:
        print(f'{valor} pertence á sequencia de Fibonacci')
        return
    else: 
        print(f'{valor} não pertence à sequencia de Fibonacci')
        return

# 07 Recebe o valor desejado
valor = int(input("Digite um valor e veja se está dentro da sequencia do Fibonnacci: "))

# 08 Executa a função
verificaFibonacci(valor)