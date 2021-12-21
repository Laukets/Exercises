def para_segundos(hora, minuto, segundo):
    resultado = int(hora*3600 + minuto*60 + segundo)
    return resultado

para_segundos(1.5,23,54)

def horas_em(segundos):
    result = int(segundos/3600)
    return result

horas_em(10976)

import math

def minutos_em(segundos):
    horas = segundos/3600
    inteiro = math.trunc(horas)
    segundos_restantes = (horas - inteiro)*3600
    result = int(segundos_restantes/60)
    return result

minutos_em(10976)

def segundos_em(segundos):
    minutos = segundos/60
    inteiro = math.trunc(minutos)
    restante = int((minutos - inteiro)*60)
    return restante

segundos_em(10976)

