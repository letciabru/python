dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
km = float(input("Digite a quantidade de quilômetros percorridos: "))

preco_dia = 60
preco_km = 0.15

preco_total = (dias * preco_dia) + (km * preco_km)

print("O preço total a pagar é: R$", preco_total)