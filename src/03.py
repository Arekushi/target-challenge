# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
# faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
# Estes dias devem ser ignorados no cálculo da média;

# DÚVIDA
# Aparentemente não foi incluido um JSON ou XML para fonte de dados, então criei um

from sys import stdout

data = {
    '2023-03-01': {'faturamento': 1000.0, 'feriado': False},
    '2023-03-02': {'faturamento': 1200.0, 'feriado': False},
    '2023-03-03': {'faturamento': 1500.0, 'feriado': False},
    '2023-03-04': {'faturamento': 0.0, 'feriado': True},
    '2023-03-05': {'faturamento': 1800.0, 'feriado': False},
    '2023-03-06': {'faturamento': 2000.0, 'feriado': False},
    '2023-03-07': {'faturamento': 0.0, 'feriado': True},
    '2023-03-08': {'faturamento': 0.0, 'feriado': True},
    '2023-03-09': {'faturamento': 2200.0, 'feriado': False},
    '2023-03-10': {'faturamento': 2500.0, 'feriado': False},
    '2023-04-01': {'faturamento': 1200.0, 'feriado': False},
    '2023-04-02': {'faturamento': 1500.0, 'feriado': False},
    '2023-04-03': {'faturamento': 1800.0, 'feriado': False},
    '2023-04-04': {'faturamento': 0.0, 'feriado': True},
    '2023-04-05': {'faturamento': 2000.0, 'feriado': False},
    '2023-04-06': {'faturamento': 2200.0, 'feriado': False},
    '2023-04-07': {'faturamento': 0.0, 'feriado': True},
    '2023-04-08': {'faturamento': 0.0, 'feriado': True},
    '2023-04-09': {'faturamento': 2500.0, 'feriado': False},
    '2023-04-10': {'faturamento': 2800.0, 'feriado': False},
    '2023-04-11': {'faturamento': 3000.0, 'feriado': False},
    '2023-04-12': {'faturamento': 0.0, 'feriado': True},
    '2023-04-13': {'faturamento': 3200.0, 'feriado': False},
    '2023-04-14': {'faturamento': 3500.0, 'feriado': False},
    '2023-04-15': {'faturamento': 0.0, 'feriado': True},
}

def remove_holidays(data):
    return {date: values for date, values in data.items() if not values['feriado']}

def calc_avg(data):
    avg_billing = {}

    for date, values in data.items():
        month = date.split('-')[1]

        if month not in avg_billing:
            avg_billing[month] = []

        avg_billing[month].append(values['faturamento'])

    for month, faturamentos in avg_billing.items():
        avg = round(sum(faturamentos) / len(faturamentos), 4)
        avg_billing[month] = avg

    return avg_billing


def calc_min_max(data):
    min_max = {}

    for date, values in data.items():
        month = date.split('-')[1]

        if month not in min_max:
            min_max[month] = {'min': float('inf'), 'max': float('-inf')}

        if values['faturamento'] < min_max[month]['min']:
            min_max[month]['min'] = values['faturamento']
        
        if values['faturamento'] > min_max[month]['max']:
            min_max[month]['max'] = values['faturamento']

    return min_max


def days_above_average(data):
    days = {}
    avg_billing = calc_avg(data)

    for date, values in data.items():
        month = date.split('-')[1]

        if month not in days:
            days[month] = 0

        if values['faturamento'] > avg_billing[month]:
            days[month] += 1

    return days


data = remove_holidays(data)
avg_billing = calc_avg(data)
min_max = calc_min_max(data)
days = days_above_average(data)

stdout.write(f'Média do faturamento por mês: {avg_billing}\n')
stdout.write(f'Maior e menor valor de faturamento por mês: {avg_billing}\n')
stdout.write(f'Dias em que o faturamento foi maior que a média: {days}\n')
