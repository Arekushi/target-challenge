# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

# RESPOSTA
# No final o valor de soma deve ser [91]
# Abaixo também deixei outras implementações

from sys import stdout


index = 13
k = 0
sum_while = 0
sum_func = 0
sum_without_loop = 0

while(k < index):
    k += 1
    sum_while += k

sum_without_loop = (index * (index + 1)) // 2

sum_func = sum(i for i in range(0, index + 1))

stdout.write(f'{sum_while}\n') # 91
stdout.write(f'{sum_without_loop}\n') # 91
stdout.write(f'{sum_func}\n') # 91
