#Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de
#1 a 20 polegadas. A conversão entre estas duas unidades é dada por: polegada =
#centímetro × 2,54

cm = 1

while cm <= 20:
    print(f'{cm}cm = {cm * 2.54}pol')
    cm += 1
