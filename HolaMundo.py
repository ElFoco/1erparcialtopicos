#!/usr/bin/env python

texto1, texto2="Hola Mundo","jaja saludos"

texto12=12

print(texto12)

textoMultilinea="""Esto es un texto
multilinea
y puedo manejar un texto largo, en parrafos
sin necesidad de usar saltos de linea"""

print(textoMultilinea)

nombre="Luis"
apellido="Ley"
edad=22

print("Hola: {0} {1} y tienes {2}".format(nombre,apellido,edad))

nombreCompleto=f"Hola: {nombre} {apellido} tienes {edad} años"

contador=0

while(contador <=3):
    print(contador)
    contador+=1

for numero in range(3):
    print(numero+1)
    if numero==2:
        print("Fin del ciclo")



print(nombreCompleto)