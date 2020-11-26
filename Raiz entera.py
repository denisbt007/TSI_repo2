num= int(input("Ingrese el numero al que quiere sacar raiz"))
import math 

def RaízEntera(num):
    raiz = str(math.sqrt(num))
    punto = False
    entero = True

    for i in raiz:
        print(i)
        if(punto == True):
            print("Opciones para luego del punto:")
            if i == "0":
                entero = True
                print("i entero")
            elif i != "0":
                entero = False
                print("i no entero")

        if i == ".":
            print("Se detectó un punto.")
            punto = True
        

    if(entero == True):
        print(num,"tiene raíz entera que es:",raiz)
    else:
        print("la raíz es",raiz,"Por lo tanto no es entera.")

n = int(input("Ingrese el número que quiere averiguar si su raíz es entera: "))
RaízEntera(n)