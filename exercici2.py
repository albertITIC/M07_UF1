# Author: Albert Penadés Casajús
# Crear una tupla amb els mesos de l’any. 
# Demanar a l’usuari que posi un número entre 0 i 12 i mostrar per 
# pantalla el mes corresponent al número indicat per l’usuari. 
# El programa finalitza només quan l’usuari posa 0.

mesos = int(input("Introdueix un número entre 0 i 12: "))

# Rang per saber si el número de mesos es troba dins
if mesos > 0 and mesos < 13:
    # Crearé una nova tupla amb els mesos de l'any
    la_meva_tupla = ["Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Septembre", "Octubre", "Novembre", "Decembre"]
    
    # Imprimiré desde el mes 0 fins el que m'indiqui
    print(la_meva_tupla[0:mesos])
# Si posa 0, s'acaba el programa i no imprimeix cap mes del any
elif mesos == 0:
    print("Finalitzat.")
# Error perquè no es troba el número dins del rang establert
else:
    print("Error. Número fora de rang.")
