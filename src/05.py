# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua
# preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

from sys import stdout, stdin


def invert_string(value: str) -> str:
    inversed_str = ''
    
    for char in value:
        inversed_str = char + inversed_str
    
    return inversed_str


def invert_string_rec(value):
    if len(value) <= 1:
        return value
    else:
        return invert_string_rec(value[1:]) + value[0]


str_input = stdin.readline() # abc
inversed_inputs = []

inversed_inputs.append(str_input[::-1]) # cba
inversed_inputs.append(invert_string(str_input)) # cba
inversed_inputs.append(invert_string_rec(str_input)) # cba

stdout.write(f'{inversed_inputs}\n')
