**Prérequis :**

Vous devez avoir installé sur votre machine Python 3 pour que celui-ci fonctionne.

**Fonctionnement :**

Notre parseur a besoin d'un argument, le dossier contenant les .pdf.
// ange explique ici //
Ensuite, le programme appelle un script Python.
Celui-ci va :

- Appeller la fonction bash "pdftotext", et ainsi convertir les .pdf en .txt
- Parcourir les documents convertis en .txt, afin de trouver les "abstract" (ou résumé de l'auteur) présents dans les documents
- Les écrires (si trouvés) dans un fichier .txt précédemment initialisé dans un sous-dossier

**Commande pour lancer le programme :**

./analyseur.sh [nom du dossier contenant les fichiers .pdf]
