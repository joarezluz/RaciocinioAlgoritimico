import getpass

try:
    texto_oculto = getpass.getpass("Digite o texto secreto: ")
    print("\nTexto revelado:", texto_oculto)
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário")
except Exception as erro:
    print(f"\nOcorreu um erro: {erro}")
    