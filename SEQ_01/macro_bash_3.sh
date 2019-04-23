#!/usr/bin/env bash

declare -i imax=10
declare -i i=0

# Nom du fichier cible pour stocker des
# octets aléatoires :
random_seed="./random.seed"

# Copies de 4 octets aléatoires dans le fichier
# cible à partir de la source d'entropie du noyau
# Linux (périphérique virtuel '/dev/urandom'
# accumulant du bruit en provenance de l'environnement
# de la machine) :
dd if=/dev/urandom of=${random_seed} \
  count=1 bs=4 > /dev/null 2>&1

# Extraction d'une amorce aléatoire (variable
# entière non-signée sur 32 bits) construite à
# partir des 4 octets aléatoires :
seed=$(od --format=u4 --skip-bytes=0 --read-bytes=4 \
  ${random_seed} | head -1 | awk '{print $2}')

# Utilisation de l'amorce pour initialiser la
# variable RANDOM du shell :
echo "NOTICE: Seed = ${seed}" >&2
declare -i mask=32767
RANDOM=$(( seed & mask ))
echo "NOTICE: RANDOM = ${RANDOM}" >&2
while [ ${i} -lt ${imax} ]; do
	declare -i r=${RANDOM}
	echo ${r}
	let i=i+1
done

exit 0