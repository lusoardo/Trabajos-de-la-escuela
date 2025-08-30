# Juego del Ahorcado en Python

# Función para pedir la palabra secreta y transformarla en lista
def ingresar_palabra():
    palabra = input("Ingrese la palabra secreta: ").lower()
    return list(map(str, palabra))

# Función que dibuja guiones bajos según la cantidad de letras
def dibujar_lineas(palabra):
    return ["_" for _ in palabra]

# Función para mostrar el estado del tablero de manera clara
def mostrar_lineas(lineas):
    print(" ".join(lineas))

# Función recursiva que verifica si una letra está en una lista
def pertenece(letra, lista):
    if not lista:
        return False
    if lista[0] == letra:
        return True
    return pertenece(letra, lista[1:])

# Función recursiva para insertar letra en todas las posiciones donde aparezca
def insertarEnPosicion(letra, palabra, tablero, i=0):
    if i == len(palabra):   # caso base: fin de la lista
        return tablero
    if palabra[i] == letra:  # si coincide, reemplaza en tablero
        tablero[i] = letra
    return insertarEnPosicion(letra, palabra, tablero, i + 1)

# ------------------- Programa principal -------------------

palabra = ingresar_palabra()         # palabra secreta en lista
tablero = dibujar_lineas(palabra)    # tablero con guiones bajos
letrasJugadas = []                   # letras ya usadas
errores = 0                          # contador de errores
max_errores = 6

print("\nComienza el juego del Ahorcado!")
mostrar_lineas(tablero)

while errores < max_errores and "_" in tablero:
    letra = input("Ingrese una letra: ").lower()

    # Si ya jugó esa letra
    if pertenece(letra, letrasJugadas):
        print("Esa letra ya fue ingresada, pruebe con otra.")
        continue

    # Guardamos la letra jugada
    letrasJugadas.append(letra)

    # Caso: la letra está en la palabra
    if pertenece(letra, palabra):
        tablero = insertarEnPosicion(letra, palabra, tablero)
        print("¡Bien! La letra pertenece a la palabra.")
    else:
        errores += 1
        print(f"Letra incorrecta. Errores: {errores}/{max_errores}")

    mostrar_lineas(tablero)

# Resultado final
if "_" not in tablero:
    print("\n¡Felicidades! Adivinaste la palabra secreta.")
else:
    print("\nHas perdido. La palabra era:", "".join(palabra))
