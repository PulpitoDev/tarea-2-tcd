import math
from functools import reduce

print("Multiplexación en tiempo y frecuencia \n\n")

print("1. Concentrador\n")

f_inf = 430*1000
f_sup = 432*1000
Bt = f_sup - f_inf
b = 10

# Concentrador

fs = [4,4,12,20] #kHz
Ftr = reduce(math.gcd,fs)

Ri = [b*num for num in fs]
for i in range(len(Ri)):
    print(f"R{i+1} = {Ri[i]} kHz")



print("\nPara poder obtener la frecuencia de trama se requiere el máximo común divisor")
print("de las frecuencias de los sensores, esto para poder enviarlos en slots.")
print("Frecuencia de trama = MCD(4,4,12,20) =",Ftr,"kHz")
print("\nDuración de la trama: Ttr =",int(1000/Ftr),"us\n")

ni = [int(frec/Ftr) for frec in fs]
N_slots = sum(ni) + 1

for i in range(len(ni)):
    print(f"n{i+1} = {ni[i]} slots")

print("\nCantidad estimada de slots: N slots =",N_slots,"\n")
print("Una posible estructura para la trama: ")
print("| S | 4 | 1 | 2 | 3 | 4 | 3 | 4 | 3 | 4 | 4 |\n")

bpt = b*N_slots
R = bpt*Ftr
print("Bits por trama = b * N slots =",bpt,"bits")
print("R = 110 bits * Ftr =", R, "kbps")
print("Tiempo de slot: T slot =",int(1000/(Ftr*N_slots)),"us")
print("Tiempo de bit: T bit \u2248", round(1000/R,3),"us")
print("\u03b7 = Bits de información / Bits totales \u2248",round((N_slots-1)/N_slots,3))

# Enlace de radio
print("\n\n2. Enlace de radio\n")
canales = [R,330,200]
BW_canales = [2*Rci for Rci in canales]

Bg = int((Bt - sum(BW_canales))/(len(BW_canales) - 1))

print("Bi = 2*Rci")
for i in range(len(BW_canales)):
    print(f"Rc{i} = {BW_canales[i]} kHz")

print("\nBanda de guarda: Bg = (Bt-sum(Bi))/(N-1) =",Bg,"kHz\n")

contador = 0
cont_bw = 0
cotas_frecuencias = []
print(f"{'Canal':<15}{'BW'+'[kHz]':<15}{'f inf'+'[kHz]':<15}{'f sup'+'[kHz]':<15}{'fi'+'[kHz]':<15}")
print("-"*68)

while contador < (2*len(BW_canales) -1):
    if contador%2 == 0:
        f_sup = f_inf + BW_canales[cont_bw]
        print(f"{'C'+str(cont_bw+1)+' ':<15}{str(BW_canales[cont_bw]):<15}{str(f_inf):<15}{str(f_sup):<15}{str(f_inf+canales[cont_bw]):<15}")
        f_inf = f_sup
        cotas_frecuencias.append([f_inf,f_sup])
        cont_bw += 1
        
    else:
        f_sup += Bg
        print(f"{'Guarda':<15}{str(Bg):<15}{str(f_inf):<15}{str(f_sup):<15}{'-':<15}")
        f_inf = f_sup

    contador += 1

contador = cont_bw = 0

print("")
print("+" + "+".join(["-"*13 if i%2 == 0 else "-"*10 for i in range(2*len(cotas_frecuencias)-1)]) + "+")

while contador < (2*len(cotas_frecuencias)-1):
    if contador%2 == 0:
        print(f"|{'C'+str(cont_bw+1):^13}", end="")
        cont_bw += 1
    else:
        print(f"|{'Guarda':^10}", end="")
    contador += 1

print("|")
print("+" + "+".join(["-"*13 if i%2 == 0 else "-"*10 for i in range(2*len(cotas_frecuencias)-1)]) + "+")

contador = cont_bw = 0

while contador < (2*len(cotas_frecuencias)-1):
    if contador%2 == 0:
        print(f"|{str(cotas_frecuencias[cont_bw][0])+'–'+str(cotas_frecuencias[cont_bw][1]):^13}", end="")
        cont_bw += 1
    else:
        print(f"|{Bg:^10}", end="")
    contador += 1

print("|")
print("+" + "+".join(["-"*13 if i%2 == 0 else "-"*10 for i in range(2*len(cotas_frecuencias)-1)]) + "+")

print("\n\n3. Un sensor más\n")

f_inf = 430*1000
f_sup = 432*1000
Bt = f_sup - f_inf

fs = [4,4,12,20,5] #kHz
Ftr = reduce(math.gcd,fs)
print("La nueva f tr es de",Ftr,"kHz\n")
ni = [int(frec/Ftr) for frec in fs]

for i in range(len(ni)):
    print(f"n{i} = {ni[i]} slots")

N_slots = sum(ni) + 1
bpt = b*N_slots
R = bpt*Ftr
print(f"\nTasa nueva: R' = {R} kHz")

canales = [R,330,200]
BW_canales = [2*Rci for Rci in canales]
Bg = int((Bt - sum(BW_canales))/(len(BW_canales) - 1))
print(f"Bg' = {Bg} kHz\n\n")

contador = cont_bw = 0
cotas_frecuencias = []
print(f"{'Canal':<15}{'BW'+'[kHz]':<15}{'f inf'+'[kHz]':<15}{'f sup'+'[kHz]':<15}{'fi'+'[kHz]':<15}")
print("-"*68)

while contador < (2*len(BW_canales) -1):
    if contador%2 == 0:
        f_sup = f_inf + BW_canales[cont_bw]
        print(f"{'C'+str(cont_bw+1)+' ':<15}{str(BW_canales[cont_bw]):<15}{str(f_inf):<15}{str(f_sup):<15}{str(f_inf+canales[cont_bw]):<15}")
        f_inf = f_sup
        cotas_frecuencias.append([f_inf,f_sup])
        cont_bw += 1
        
    else:
        f_sup += Bg
        print(f"{'Guarda':<15}{str(Bg):<15}{str(f_inf):<15}{str(f_sup):<15}{'-':<15}")
        f_inf = f_sup

    contador += 1