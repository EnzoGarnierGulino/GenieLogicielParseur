#!/bin/bash

rm -rf "$1_txt"
mkdir "$1_txt"
for f in $1*.pdf
do
    nom_origin=$(echo "$f" | grep -o "[^/]*$" | cut -d'.' -f1)
    nom_dest="$1_txt/$nom_origin.txt"
    touch $nom_dest
    python3 analyseur.py $1 $nom_origin $nom_dest
done