# Author: Albert Penadés Casajús
# Demanar a l’usuari que introdueixi un valor en €, seguidament demanar que introdueixi el IVA a aplicar-hi (4%, 10% o 21%) i 
# finalment mostrar, per pantalla, el resultat del valor indicat per l’usuari, el % d’IVA demanat per l’usuari i el valor final amb l’IVA afegit.
# Si no afageix el IVA correcte, tornar a demanar el IVA fins que posi un dels 3 vàlids.
print("Apartat 2: IVA")
preu = float(input("Entra una quantitat en €: " ))
# Comprovo que el preu sigui real
while preu > 0:
    iva = input("Introdueix una quantitat d'IVA (4, 10 o 21): ")
    # Paso la conversió del número amb el IVA relacionat
    if iva == 4:
        iva == 1.04
    elif iva == 10:
        iva == 1.1
    elif iva == 21:
        iva = 1.21
    # Si no coincideix amb el que es demana, error
    else:
        print("ERROR: IVA invàlid!")
        continue

    # Fer la operació (aplicar l'IVA):
    preuTotal = preu * iva
    
    # Donar resultat per pantalla
    print("Preu final (amb IVA aplicat): " + str(preuTotal))
    break 