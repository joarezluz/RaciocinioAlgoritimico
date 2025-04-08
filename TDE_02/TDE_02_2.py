#Exercício 02
# A partir do ano de nascimento informado pelo usuário, elabore um algoritmo que informe
# a idade que completará (ou já completou) em 2023. Verifique se ele já pode fazer a carteira
# de motorista ou não, informando sua situação.

anoNascimento = int(input("Ano de nascimento: "))
idade = 2023 - anoNascimento

print(f"Você possui {idade} anos.")
if idade >= 18:
    print("Está apto para fazer a carteira de motorista.")
else:
    print("Ainda não pode fazer a carteira de motorista")
