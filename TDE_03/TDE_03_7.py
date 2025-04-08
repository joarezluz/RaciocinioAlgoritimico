#Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabela
#de conversão de metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10
#quilômetros.  milha=1609,344m

milha = round(1609.344/1000)
km = 120
while km <= 160:
    print(f'{km}Km = {km*milha}milha')
    km += 10
