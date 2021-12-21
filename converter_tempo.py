
sec_str = input("entre com o numero de segundos que deseja converter: ")
total_sec = int(sec_str)

horas = total_sec // 3600 
sec_restantes = total_sec % 3600
minutos = sec_restantes // 60
sec_rest_final = sec_restantes % 60

print('Horas = ', horas, ", Minutos = ", minutos, " e Segundos = ", sec_rest_final)
