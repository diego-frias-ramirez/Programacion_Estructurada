"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("cls")

paises={"México", "Brasil", "España","Canada","Canada"}
print(paises)
  
varios={True,"Cadena",23,23.1416}
print(varios)

paises.add("Mexico")
print(paises)

varios.pop()
print(varios)

varios.remove("Cadena")
print(varios)


#ejemplo crear un programa que soicte los email de los alumnos de la utd alamcenar en una lista y
#  posterioremnete mostrar en pantalla los email sin duplicados 

"""
emails = []

# Pedimos al usuario que ingrese los emails (por ejemplo 5)
for i in range(5):
    email = input(f"Ingresa el email del alumno {i+1}: ")
    emails.append(email)

# Convertimos la lista en un set para eliminar duplicados
emails_sin_duplicados = set(emails)

print("\nEmails sin duplicados:")
for email in emails_sin_duplicados:
    print(email)
    """

os.system("cls")
# 2da en clase

emails = []
resp="si"

while resp=="si":
    emails.append(input("Escribe un email: "))
    resp=input("¿Deseas agregar otro email").lower
  
emails_set=set(emails)
emails=list(emails_set)
print(emails)
