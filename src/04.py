# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada
# estado teve dentro do valor total mensal da distribuidora.

# RESPOSTA
# SP      67836.43        37.53%
# RJ      36678.66        20.29%
# MG      29229.88        16.17%
# ES      27165.48        15.03%
# OUTROS  19849.53        10.98%
from sys import stdout


data = {
    'sp': 67836.43,
    'rj': 36678.66,
    'mg': 29229.88 ,
    'es': 27165.48,
    'outros': 19849.53
}

total_value = sum(data.values())

for state, values in data.items():
    percentage = (values / total_value) * 100
    stdout.write(f"{state.upper()}\t{values:.2f}\t{percentage:.2f}%\n")
