def CalcFactorial(num):
    acumulado = 1
    for i in range(1,num+1):
        print(acumulado,"x",i,"=",acumulado*i)
        acumulado *= i
    print(acumulado)

n = int(input("Ingrese el número que quiere calcular su factorial: "))
CalcFactorial(n)
#somos Grupo 2