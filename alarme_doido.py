atual = input("entre com a hora atual: ")
alarme = input("entre com o numero de horas que faltam para o alarme tocar: ")
hr_atual = int(atual)
alarm = int(alarme)
dias = alarm // 24
horas = alarm % 24
hr_alarme = hr_atual + horas
print(f"O alarme irá tocar daqui {dias} às {hr_alarme}.")