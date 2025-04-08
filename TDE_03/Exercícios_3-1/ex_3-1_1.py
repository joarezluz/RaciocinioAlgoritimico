# Ler do teclado uma quantidade de números inteiros a serem lidos e calcular:
# a) a soma total entre eles
# b) a soma dos que forem pares
# c) a soma dos que forem ímpares
# d) a amplitude amostral considerando todos os números lidos (diferença entre o maior e o menor)

# Solicita a quantidade de números a serem lidos
quantidade = int(input("Digite a quantidade de números que deseja inserir: "))

# Inicializa as variáveis necessárias
numeros = []
soma_total = 0
soma_pares = 0
soma_impares = 0

# Lê os números do usuário e realiza os cálculos
for _ in range(quantidade):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)
    soma_total += num
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num

# Calcula a amplitude amostral
amplitude = max(numeros) - min(numeros)

# Exibe os resultados
print(f"Soma total: {soma_total}")
print(f"Soma dos pares: {soma_pares}")
print(f"Soma dos ímpares: {soma_impares}")
print(f"Amplitude amostral: {amplitude}")
