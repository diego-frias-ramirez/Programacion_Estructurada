"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en
    lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido 
    como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("cls")

pais1={
      "nombre":"México",
      "capital":"CDMX",
      "poblacion":12000000,
      "idioma":"español",
      "status":True
       }

pais2={
      "nombre":"Brasil",
      "capital":"Brasilia",
      "poblacion":14000000,
      "idioma":"portuges",
      "status":True
       }

pais3={
      "nombre":"Canada",
      "capital":"Otawua",
      "poblacion":10000000,
      "idioma":["ingles","frances"],
      "status":True
       }

#Funciones u operaciones con los dict u objetos

print(pais1)

for i in pais1:
    print(f"{i}={pais1[i]}")

#agregar un atributo a un dict

pais1["altitud"]=3000

print(pais1)

for i in pais1:
    print(f"{i}={pais1[i]}")

#quitar un atributo en particular 

pais1.pop("status")
for i in pais1:
    print(f"{i}={pais1[i]}")