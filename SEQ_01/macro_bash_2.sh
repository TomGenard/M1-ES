!/usr/bin/env bash

# Déclaration d'une variable pour le nombre
# de tirages :
declare -i imax=10

# Déclaration d'une variable pour l'indice
# de boucle du tirage :
declare -i i=0

# Extraction d'une amorce aléatoire (variable
# entière non-signée sur 32 bits) construite à
# partir de la date (exprimée en secondes écoulées
# depuis Epoch, cf. man date) :
declare -i seed=$(date +%s)

# Affichage (dans le flot standard des erreurs) :
echo "NOTICE: Seed = ${seed}" >&2

# Utilisation de l'amorce pour initialiser la
# variable RANDOM (16 bits) du shell :
declare -i mask=32767
RANDOM=$(( seed & mask ))
echo "NOTICE: RANDOM = ${RANDOM}" >&2
while [ ${i} -lt ${imax} ]; do
	declare -i r=${RANDOM}
	echo ${r}
	let i=i+1
done

exit 0