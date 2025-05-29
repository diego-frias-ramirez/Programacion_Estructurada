
print("Tablas de Multiplicacion")
def tablaMultiplicacion(num,multi):
 num = int(input("Ingresa el número para calcular su tabla de multiplicar: "))
 for i in range(1,11):
    multi=num*i
    return num, i, multi
 
 tablaMultiplicacion()