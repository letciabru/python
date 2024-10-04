# NESSE CÓGIGO CALCULA E MOSTRA QUANTO UMA EMPRESA DE CINEMA LUCROU EM UM DIA, 
# E QUANTO FOI DE INGRESSO DE VALOR INTEIRO OU MEIA (ESTUDANTE OU NÃO). 
# ONDE NO SISTEMA LINEAR SERIA CALCULADO X E Y.

total_pagantes = 60
valor_total = 1000
valor_inteira = 20
valor_meia = 10

total_pagantes = int(input("Digite a quantidade total de pagantes: "))
valor_total = float(input("Informe o valor total do dia: "))
valor_inteira = float(input("Informa o valor da inteira: "))
valor_meia = float(input("Informe o valor da meia: "))

x = (valor_total-valor_meia * total_pagantes) / (valor_inteira - valor_meia)
y = total_pagantes - x

print(f"Pagantes Inteira: {x}")
print(f"Pagantes meia: {y}")
print(f"Total Inteira: {x*valor_inteira}")
print(f"Total meia: {y*valor_meia}")