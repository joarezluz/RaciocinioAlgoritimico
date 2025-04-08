# Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um
# algoritmo que leia o código da moeda que o cliente quer comprar e qual o montante
# que ele quer adquirir nessa moeda. Mostre então quanto ele deverá pagar em reais
# para concretizar a operação. Além da cotação, a empresa cobra uma comissão de 5%
# (quando o valor for menor que R$ 1.000), ou de 3% (quando maior ou igual a
# R$1.000). Considere o câmbio do dia.

# $1 = R$5,6741  libra= R$7.3423 eur= R$6,1368
cambio = 0
cambDol = 5.6741
cambLib = 7.3423
cambEur = 6.1368

moeda = int(input('Qual moeda deseja?\n[1] Dólar [2] Libra [3] Euro \n:> '))
valor = float(input('Insira o valor desejado:'))

if moeda == 1: cambio =cambDol
if moeda == 2: cambio =cambLib
if moeda == 3: cambio =cambEur
if valor <= 1000: tx = 0.005
if valor > 1000: tx = 0.003

print(f'R${cambio * (valor + (valor* tx)):.2f}')
