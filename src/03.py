# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
# faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
# Estes dias devem ser ignorados no cálculo da média;

# UPDATE
# Os dados agora vem do arquivo data.json, que foi disponibilizado pela empresa

# RESULTADO
# Média do faturamento por mês. AVG: 20865.3702
# Maior e menor valor de faturamento por mês. MAX: 373.7838 | MIN: 48924.2448
# Dias em que o faturamento foi maior que a média. DAYS: [1, 2, 3, 6, 8, 9, 16, 20, 21, 27] | TOTAL: 10 dias

from sys import stdout
import functools
import json
from typing import List


with open('./data/data.json', 'r') as f:
    data = json.load(f)


# Remove os dias em que o faturamento foi diferente de 0, ou seja, dias úteis
def transform_data(data) -> dict:
    return {values['dia']: values['valor'] for values in data if values['valor'] != 0}


# Solução em usar SUM, mas usando um REDUCE
# Arredondamento com precisão de 4 casas decimais
def calc_avg(data) -> float:
    sum_values = functools.reduce(lambda x, y: x + y, data.values())
    return round(sum_values / len(data), 4)


# Solução sem usar MIN e MAX
def calc_min_max(data) -> tuple[float, float]:
    min_value = float('inf')
    max_value = float('-inf')
    
    for value in data.values():
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    
    return min_value, max_value


# Solução usando For Comprehension
def days_above_avg(data) -> List[int]:
    avg = calc_avg(data)
    return [day for day, value in data.items() if value > avg]


data = transform_data(data)
avg_billing = calc_avg(data)
min, max = calc_min_max(data)
days = days_above_avg(data)

stdout.write(f'Média do faturamento por mês. AVG: {avg_billing}\n')
stdout.write(f'Maior e menor valor de faturamento por mês. MAX: {min} | MIN: {max}\n')
stdout.write(f'Dias em que o faturamento foi maior que a média. DAYS: {days} | TOTAL: {len(days)} dias\n')
