# Author: Albert Penadés Casajús

# Demanar a l’usuari que introdueixi 2 valors i mostrar, per pantalla, quin és el més gran. (Utilitzar operador correcte)
print("Activitat 3: ")
# Demano per pantalla els valors (v) que fiqui l'usuari per pantalla
v1 = input("Introdueix un valor: ")
v2 = input("Introdueix un segon valor: ")

#Si v1 és més gran que v2...
if v1 > v2:
    print(v1 + " és més gran que " + v2)
#Si v2 és més gran que v1...
elif v1 < v2:
    print(v2 + " és més gran que " + v1)
#Si v1 i v2 són iguals...
else:
    print("Els valors introduïts són iguals.")
