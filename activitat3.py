# Author: Albert Penadés Casajús
# Demanar a l’usuari que introdueixi 2 valors i mostrar, per pantalla, quin és el més gran. (Utilitzar operador correcte)
v1 = input("Introdueix un valor: ")
v2 = input("Introdueix un valor: ")

if v1 > v2:
    print(v1 + " és més gran que " + v2)
elif v1 < v2:
    print(v2 + " és més gran que " + v1)
else:
    print("Els valors introduïts són iguals.")