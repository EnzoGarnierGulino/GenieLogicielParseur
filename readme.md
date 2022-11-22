<ins> **PARSEUR** <ins>

<ins> **Prérequis :** <ins>

Vous devez avoir installé sur votre machine _Python 3_ pour que le parseur fonctionne.

<ins> **Fonctionnement :** <ins>

Notre parseur a besoin d'un argument, le dossier contenant les .pdf.
// ange explique ici //
Ensuite, le programme appelle un script Python.
Celui-ci va :

- Appeller la fonction bash "pdftotext", et ainsi convertir les .pdf en .txt
- Parcourir les documents convertis en .txt, afin de trouver les "abstract" (ou résumé de l'auteur) présents dans les documents
- Les écrires (si trouvés) dans un fichier .txt précédemment initialisé dans un sous-dossier

<ins> **Commande pour lancer le programme :** <ins>

./analyseur.sh [nom du dossier contenant les fichiers .pdf]
