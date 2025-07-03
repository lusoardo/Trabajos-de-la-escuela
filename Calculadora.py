union=0
Num = []
resultado=[]
n1 = input("Ingrese el nombre que desea calcular: ").lower()
n2 = input("Ingrese el nombre que desea calcular: ").lower()

if len(n1) > len(n2):
    union = n1 + n2
else:
    union = n2 + n1

# Contar las letras
while len(union) > 0:
    letra = union[0]
    Num.append(union.count(letra))
    union = union.replace(letra, "")

# Proceso de reducción
while len(Num) > 2:
    nuevo_Num = []
    i = 0
    j = len(Num) - 1
    while i <= j:
        if i == j:
            nuevo_Num.append(Num[i])
        else:
            nuevo_Num.append(Num[i] + Num[j])
        i += 1
        j -= 1
    Num = nuevo_Num

if len (Num) ==0:
    Num=resultado
    resultado=[]

if Num[0]==10:
        Num[0]=5
        Num[1]=0
print (Num)
print(resultado)


porcentaje_final = int(f"{Num[0]}{Num[1]}")
print(f"Compatibilidad final: {porcentaje_final}%")
