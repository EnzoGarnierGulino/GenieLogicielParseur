#!/bin/bash

type_sortie=$1
dossier_origine=$2


if [[ ! -z "$dossier_origine" && -d "$dossier_origine" && $type_sortie == "-t" || $type_sortie == "-x" ]]
then
    rm -rf "$dossier_origine""_txt"
    mkdir "$dossier_origine""_txt"

    options=()
    for t in "$dossier_origine"*.pdf
    do
        options+=("$t")
        options+=("")
        options+=(off)
    done
    choices=$(dialog --separate-output --checklist "Selection des pdf de $dossier_origine" 22 90 16 "${options[@]}" 2>&1 >/dev/tty)
    for f in $choices
    do
        clear
        echo "En Cours" $f
        nom_origin=$(echo "$f" | grep -o "[^/]*$" | cut -d'.' -f1)
        if [ $type_sortie == "-t" ]
        then
            nom_dest="$dossier_origine""_txt/$nom_origin.txt"
        else
            nom_dest="$dossier_origine""_txt/$nom_origin.xml"
        fi
        touch "$nom_dest"
        pdftotext -bbox-layout "$f"
        python3 XMLReader.py "$dossier_origine" "$nom_origin" "$nom_dest" "$type_sortie"
        rm "$dossier_origine""$nom_origin"".html"
    done
    clear
    echo "Success"
else
    echo "Erreur au niveau des arguments veillez entre -t ou -x en premier argument et le dossier en deuxieme argument"
fi