num = input("Ingrese el número que quiere averiguar si es capicúa: ")
capi = True
izq = []
der = []
for i in str(num):
    der.append(i)
izq.extend(der)
der.reverse()
print(izq)
print(der)

pos = 0
for i in izq:
    if i != der[pos]:
        capi = False
    pos += 1
    
if capi == True:
    print(num,"es capicúa.")
else:
    print(num,"no es capicúa.")
    #codigo capicua