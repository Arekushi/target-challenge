# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
# próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de
# Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua
# preferência ou pode ser previamente definido no código;

# EXEMPLOS DE ENTRADA E SAÍDA
# 35
# Fibbonaci: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# o número 35 não pertence a sequência

# 55
# Fibbonaci: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# o número 55 pertence a sequência

# 789152
# Fibbonaci: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
# o número 789152 não pertence a sequência

from sys import stdout, stdin


def fibonnaci(n):    
    def fib(a, b, n):
        if a >= n:
            return [a]
        else:
            return [a] + fib(b, a + b, n)

    return fib(0, 1, n)


n = int(stdin.readline())
fib_sequence = fibonnaci(n)
message = f'o número {n} não pertence a sequência'
message = message.replace(' não ', ' ') if n in fib_sequence else message

stdout.write(f'Fibbonaci: {fib_sequence}\n')
stdout.write(f'{message}\n')
