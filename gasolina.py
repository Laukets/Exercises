km_perc = input("entre com o numero de km percorridos: ")
gas_l = input("entre com o numero de litros consumidos: ")
km = int(km_perc)
gas = int(gas_l)

consumo = gas / km

print(f"O consumo de gasolina por km é de {consumo} litros.")