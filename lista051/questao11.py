'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um expoente qualquer (Variável e), ou seja, de be. (Sem usar Math.pow();)
'''

b = float(input("Informe um valor para ser a base da potência: "))
e = float(input("Informe um valor para ser o expoente: "))

cont = 1
acumulador = 1
while ( cont <= e ):
    acumulador = acumulador * b
    cont = cont + 1

print(f"{b:.0f} elevado à {e:.0f} = {acumulador:.0f}")


'''
c = b ** e
d = 0

print(f"{b} elevado à {e} = {c}")
'''
