#!/usr/bin/env bash

# Déclaration d'une variable pour le nombre
# de tirages :
declare -i imax=10

# Déclaration d'une variable pour l'indice
# de boucle du tirage :
declare -i i=0

# Amorce la variable d'environnement RANDOM
# (entre 0 et 32767, cf. man bash)
RANDOM=3126

# Boucle :
while [ ${i} -lt ${imax} ]; do
	# Extraction d'un entier aléatoire à
	# partir de RANDOM :
	declare -i r=${RANDOM}
	# Affichage (dans le flot standard de sortie) :
	echo ${r}
	# Increment de l'indice de boucle :
	let i=i+1
done

exit 0