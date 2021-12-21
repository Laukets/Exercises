dia_m = input("qual é o dia do mês: ")
dia_semana = input("qual é o dia da semana: ")
ferias_ini = input("o total de dia de férias: ")
dia_mes = int(dia_m)
ferias_inicio = int(ferias_ini)

if dia_semana == "domingo":
    dia_semana = 1
elif dia_semana == "segunda":
    dia_semana = 2
elif dia_semana == "terça":
    dia_semana = 3
elif dia_semana == "quarta":
    dia_semana = 4
elif dia_semana == "quinta":
    dia_semana = 5
elif dia_semana == "sexta":
    dia_semana = 6
elif dia_semana == "sabado":
    dia_semana = 7
else:
    print("resposta inválida!")

dia = dia_mes + ferias_inicio
semanas = ferias_inicio // 7
dias = ferias_inicio % 7
ferias_fim = dia_semana + dias

if ferias_fim == 1 or ferias_fim == 8:
    ferias_fim = "domingo"
elif ferias_fim == 2 or ferias_fim == 9:
    ferias_fim = "segunda"
elif ferias_fim == 3 or ferias_fim == 10:
    ferias_fim = "terça"
elif ferias_fim == 4 or ferias_fim == 11:
    ferias_fim = "quarta"
elif ferias_fim == 5 or ferias_fim == 12:
    ferias_fim = "quinta"
elif ferias_fim == 6 or ferias_fim == 13:
    ferias_fim = "sexta"
elif ferias_fim == 7 or ferias_fim == 14:
    ferias_fim = "sabado"
else:
    print("erro de contagem")

print(f"suas férias terminarão dia {dia}, {ferias_fim}.")