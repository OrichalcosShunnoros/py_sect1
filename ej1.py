"""
Programa que calcula qué edad tendrá un individuo pasado un tiempo x.
Autor: CZ
Fecha: 20 de Octubre 2023
"""
#Cree un programa que lea la edad de un usuario y muestre cuántos años tentrá
#el usuario dentro de tantos años como el usuario indique.

ed = int(input("Ingrese edad: "))
t = int(input("Ingrese el número de años con el que hacer el cálculo: "))

edf = ed + t

print(f"La edad que tendrá dentro de {t} años son {edf} años.")