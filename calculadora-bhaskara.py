a= float(input("valor de a:"))
b= float(input("valor de b:"))
c = float(input("valor de c:"))

delta = b**2 -4*a*c

if delta <0:
    print("A equação não possui raízes reais")
elif delta == 0:
    print("Faça a equação de baskara: x1-b + delta**0,5 / 2*a")
    x1 = -b/2*a
    print("valor de x1:")
else:
    x1= -b + delta**0,5 / 2*a 
    x2= -b - delta**0,5 / 2*a

print(f"valor de x1: {x1}")
print(f"valor de x2: {x2}")


