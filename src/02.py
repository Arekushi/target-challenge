# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
# próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de
# Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua
# preferência ou pode ser previamente definido no código;

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
