**PARSEUR**

<ins> **Prérequis :** <ins>

Vous devez avoir installé sur votre machine _Python 3_ et dialog pour que le parseur fonctionne.

<ins> **Fonctionnement :** <ins>

Notre parseur a besoin d'un argument, le dossier contenant les .pdf.

Le script Bash va:
  
  - Afficher un menu de selection avec tout les fichier pdf du dossier donné
  - Supprimer le répertoire "_txt" dans le dossier donné en argument puis le re-créer. Ce qui permet de supprimer tout le contenue du dossier "_txt"
  - Parcourir tout les pdf dans le dossier, et créer le .txt avec le même nom que le fichier pdf dans le sous-dossier "_txt"
  - Appelle le script Python, avec en argument le dossier contenant les .pdf, le nom du pdf actuel et le fichier txt dans lequel il doit écrire
  
A la suite le Python va :

- Appeller la fonction bash "pdftotext", et ainsi convertir les .pdf en .txt
- Parcourir les documents convertis en .txt, afin de trouver les "abstract" (ou résumé de l'auteur) présents dans les documents
- Les écrires (si trouvés) dans un fichier .txt précédemment initialisé dans un sous-dossier

<ins> **Commande pour lancer le programme :** <ins>

./analyseur.sh [nom du dossier contenant les fichiers .pdf]
