# cedulas disponíveis
cedulas = [50, 20, 10, 5, 1]

valor = int(input("digite o valor total a ser pago (ou 0 para sair): "))

valor_original = valor
print(f"\npara pagar o valor de R$ {valor_original}, serão necessárias:")

for cedula in cedulas:
        if valor >= cedula:
            quantidade = valor // cedula
            print(f"R$ {cedula}: {quantidade} cédula(s)")
            valor %= cedula
        else:
            print(f"R$ {cedula}: 0 cédula(s)")

print("\npagamento concluído.\n")