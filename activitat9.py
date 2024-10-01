# Author: Albert Penadés Casajús

# Demanar a l’usuari que posi dues paraules.
# Al executar el programa, mostrarà per pantalla les dues paraules amb els dos primers caràcters de cada paraula intercanviats.
# Exemple: Quatre Camins passaria a Caatre Qumins.

print("Activitat 9: ")

nParaules = input("Introdueix dues paraules: ")

# Separar les paraules
paraules = nParaules.split()

# Validar que s'han introduït exactament dues paraules
if len(paraules) != 2:
    print("ERROR, introdueix 2 paraules.")
else:
    p1 = paraules[0]  # Primera paraula
    p2 = paraules[1]  # Segona paraula

    # Comprovar que ambdues paraules tinguin almenys 2 caràcters
    if len(p1) < 2 or len(p2) < 2:
        print("ERROR, ambdues paraules han de tenir almenys 2 caràcters.")
    else:
        # Intercanviar els dos primers caràcters
        nova_p1 = p2[:2] + p1[2:]  # Els dos primers caràcters de p2 + la resta de p1
        nova_p2 = p1[:2] + p2[2:]  # Els dos primers caràcters de p1 + la resta de p2

        # Mostrar el resultat
        print(f"Resultat: {nova_p1} {nova_p2}")
