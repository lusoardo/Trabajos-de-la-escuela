#7- Números mayores que 10 al cuadrado
cuadrado = [5, 12, 3, 20]
mayor = [x**2 for x in cuadrado if x > 10]
print(mayor)
#9. Tablas de multiplicar del 5 (como strings)
tabla= [f"{i}x5={i*5}" for i in range(1, 10)]
print(tabla)
