soma = 0
contador = 0

while True:
    numero= int(input("digite um número para inteiro (0 para sair): "))

    if numero == 0:
        break

    soma += numero
    contador += 1


if contador > 0:
    media = soma / contador

    print(f"quantidade de números digitados: {contador}")
    print(f"soma: {soma}")
    print(f"média aritmética: {media:.2f}")
else:
    print("nenhum número foi digitado.")

