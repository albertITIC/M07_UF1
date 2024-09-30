# Author: Albert Penadés Casajús

# Demanar a l’usuari un número. Indicar si el número inserit per l’usuari és parell o senar.
print("Activitat 5: ")

# Demano el número per pantalla
num = int(input("Introdueix un número: "))
# Faig el módul del número, i si aquest obté un residu de 0 significa que és parell
if num %2 == 0:
    print("Número parell :)")
# Si no, significa que és senar
else:
    print("Número senar :)")