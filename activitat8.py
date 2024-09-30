# Author: Albert Penadés Casajús

# Demanar a l’usuari que posi entre 1 i 3 paraules. Al executar el programa, mostrarà la/es paraula/es indicada/es per l’usuari, 
# indicar quants caràcters té i indicar el primer, i l’últim caràcter. (mirar split())
# GUIA pas a pas de mostra:
# Demanar a l’usuari les paraules.
# Utilitzar split().
# Validar el número de paraules insertat
# Imprimir resposta per pantalla

print("Activitat 8: ")

# Demanar a l’usuari que posi entre 1 i 3 paraules
nParaules = input("Introdueix entre 1 i 3 paraules: ") # Número de paraules que introdueix l'usuari

# Utilitzar split() per separar les paraules
paraules = nParaules.split()

# Validar el número de paraules insertat
if len(paraules) < 1 or len(paraules) > 3:
    print("ERROR, has d'introdueir entre 1 i 3 paraules.")
else:
    # Imprimim la resposta per pantalla
    for paraula in paraules:
        num_car = len(paraula)
        primer_car = paraula[0]
        ultim_car = paraula[-1]
        
        print(f"Paraula: '{paraula}'")
        print(f"Número de caràcters: {num_car}")
        print(f"Primer caràcter: '{primer_car}'")
        print(f"Últim caràcter: '{ultim_car}'")
        print("--------------------")
