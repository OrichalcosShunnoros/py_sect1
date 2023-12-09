"""
Programa que  lea y muestre diferentes resultados dependiendo de la operación.
Autor: CZ
Fecha: 05 de Diciembre 2023
"""
#Cree un programa que lea dos números y muestre su producto, su cociente, su módulo, su suma y su resta.

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

prod = n1 * n2
coci = n1 / n2
mod = n1 % n2
sum = n1 + n2
res = n1 - n2
#--------------------------------------Resultados------------------------------
print(f"Producto: {prod}")
print(f"Cociente: {coci}")
print(f"Módulo: {mod}")
print(f"Suma: {sum}")
print(f"Resta: {res}")
