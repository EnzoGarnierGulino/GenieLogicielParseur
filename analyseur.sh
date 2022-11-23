#!/bin/bash

type_sortie=$1
dossier_origine=$2

if [[ ! -z $dossier_origine && $type_sortie == "-t" || $type_sortie == "-x" ]]
then
    rm -rf "$dossier_origine/_txt"
    mkdir "$dossier_origine/_txt"
    for f in $dossier_origine*.pdf
    do
        nom_origin=$(echo "$f" | grep -o "[^/]*$" | cut -d'.' -f1)
        if [ $type_sortie == "-t" ]
        then
            nom_dest="$dossier_origine/_txt/$nom_origin.txt"
        else
            nom_dest="$dossier_origine/_txt/$nom_origin.xml"
        fi
        touch $nom_dest
        python3 analyseur.py $dossier_origine $nom_origin $nom_dest $type_sortie
    done
else
    echo "Erreur au niveau des arguments veillez entre -t ou -x en premier argument et le dossier en deuxieme argument"
fi