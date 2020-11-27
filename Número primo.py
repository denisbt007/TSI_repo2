
import math
n = int(input("Ingrese el número que quiere revisar si es primo: "))
def DefNúmeroPrimo(num):
    primo = True
    print("El número a evaluar es",num)
    print("")

    for d in range(2, num):
        if(num%d == 0):
            print(d,"es divisor de",num)
            primo = False
        else:
            print("No es divisor, siguiente.")
        print("********")
        print("")

    if(primo==True):
        print(num,"es primo.")
    else:
        print(num,"no es primo.")
DefNúmeroPrimo(n)

#test1