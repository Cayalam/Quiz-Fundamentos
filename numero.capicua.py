# QUIZ: Leer un numero entero de cinco digitos y determinar si es capicua

print("-----------------------------------------------------------")
print("----Numero entero de 5 digitos y determinar si es capicua--")
print("-----------------------------------------------------------")

# input
n=int(input("digite un numero entero : "))

# processing

if 10000<=n<=99999:

    y= n%100
    d= n//1000
    f= d%10
    a=d//10
    b=y%10
    x=y//10
if x==f and b==a:
    print("Es un numero capicua")
else:
    print("No es un numero capicua")
   



print("--------------------------------")
print("---------RESULTADOS-------------")


