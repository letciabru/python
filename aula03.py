# tipos de dados primitivos: 
# - inteiro(int): numeros inteiros
# - float (float): numeros reais, decimais
# - string (str): cadeias de caracteres, utilizando aspas
# - boolean (bool): tipo logico True ou False
# - complex (complex): numeros complexos, com parte real e imaginaria
# - list (list): lista de elementos, ordenados e imutaveis
# - tuple (tuple): tuple de elementos, ordenados e imutaveis
# - dictionary (dict): dicionario de elementos, não ordenados e indexados

# atribuição de variavel por captura
nome = input("digite seu nome mano!: ")
print(type(nome))
idade = input("digite sua idade vei!: ")
print(type(idade))
altura = input("digite sua altura: ")
print(type(altura))

# exibir na tela
print(f"nome: {nome} idade: {idade} altura: {altura}")

# exemplo de conversão de string para inteiro
valorA = int(input("digite o valor de A: "))
valorB = int(input("digite o valor de B: "))
resultado = valorA + valorB
print(f"a soma = {resultado}")

#exemplo de conversão de string para float
valorA = float(input("digite o valor de A: "))
valorB = float(input("digite o valor de B: "))
resultado = valorA + valorB
print(f"a soma = {resultado}")



