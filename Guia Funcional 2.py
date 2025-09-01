# Dada una lista de números, duplicar cada uno.
# Entrada: [1, 2, 3]
# Salida: [2, 4, 6]
def multiplicar(x):
    return x*2
print(list(map(multiplicar,[1,2,3])))

# Entrada: [1, -3, 5, -2]
# Salida: [-1, -3, -5, -2]

def neg(x):
    if x>0:
        return -x
    else:
        return x
print(list(map(neg,[1,2,3])))

# f = c * 9/5 + 32
# Entrada: [0, 25, 100]
# Salida: [32.0, 77.0, 212.0]

def grado(c):
    return c * 9/5 + 32
print(list(map(grado,[0,25,100])))

# Entrada: ["hola", "mundo", "python"]
# Salida: [4, 5, 6]

def tam(x):
    return len(x)
print(list(map(tam,["hola", "mundo", "python"])))


def tam(x):
    return (x)
print(list(map(len,["hola", "mundo", "python"])))

# Entrada: ["hola", "mundo"]
# Salida: ["HOLA", "MUNDO"]

def min(x):
    return x.upper()
print(list(map(min,["hola", "mundo"])))

# Entrada: ["bien", "hecho"]
# Salida: ["¡bien!", "¡hecho!"]

def sig(x):
       return "¡" + x + "!"
print(list(map(sig,["hola", "mundo"])))

# Entrada: ["manzana", "banana", "pera"] 
# Salida: ["m", "b", "p"] 
def quitar(x):
      return x[:1]
print(list(map(quitar,["hola", "mundo"])))

# Entrada: [2, 3, 4] 
# Salida: [8, 27, 64] 
def cubo(x):
    return x*x*x
print(list(map(cubo,[1,2,3])))

# Entrada: [3.6, 4.2, 5.9]
# Salida: [4, 4, 6]
print(list(map(round, [3.6, 4.2, 5.9])))


def par(x):
    return x % 2 == 0

print(list(map(par, [1, 2, 3, 4])))
