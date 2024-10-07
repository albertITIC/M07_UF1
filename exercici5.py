# Author: Albert Penadés Casajús
# Demanar a l’usuari una frase. 
# El programa eliminarà els espais i s'afegirà a una tupla. 
# Mostrar per pantalla el contingut de la tupla. 
# I mostrar també la frase sense caràcters repetits. 
# Exemple: Usuari indica la paraula caracteristica dels animals. 
# Es mostra per pantalla ==> carteisdnml.

frase = input("Introdueix una frase: ")
fSenseEspais= frase.replace(" ", "") # Per eliminar els espais

print("Cadena sense espais: ", fSenseEspais)

# Afegir els caràcters de la frase a una tupla
# tupla_caracters = tuple(frase_sense_espais)

# # Mostrar el contingut de la tupla
# print("Tupla de caràcters:", tupla_caracters)

# # Eliminar els caràcters repetits mantenint l'ordre
# frase_sense_repetits = "".join(sorted(set(frase_sense_espais), key=frase_sense_espais.index))

# # Mostrar la frase sense caràcters repetits
# print("Frase sense caràcters repetits:", frase_sense_repetits)
