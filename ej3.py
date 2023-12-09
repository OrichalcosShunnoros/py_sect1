"""
Programa que calcula intereses.
Autor: CZ
Fecha: 20 Octubre 2023
"""
#Cree un programa que lea el monto de un préstamo y el plazo en meses, 
#y muestre al usuario el valor de las cuotas mensuales pagando un interés fijo de 2.7% mensual.

pres = float(input("Ingrese el monto del préstamo solicitado: "))
plzm = int(input("Ingrese el plazo en meses: "))

intrs = float(0.027)

ctam = ((pres + (pres * intrs)) / plzm)

print(f"Las cuotas mensuales pagando un interés fijo del 2.7% mensual es ${ctam:.2f}")