#!/usr/bin/python3
import subprocess

filename = "ACL2004 HEADLINE.pdf"
fileToWrite = "SD/texte.txt"

def writeFilenameInTxt(fileToWrite, filename):
    with open(fileToWrite, 'w') as f:
        f.write(filename)

def convertPdfFileToTxt(filename):
    filenameWithoutExtensionArray = filename.split(".")
    filenameWithoutExtension = filenameWithoutExtensionArray[0]

    # filenameWithoutExtension = nom du fichier avec _ à la place des espaces
    filenameWithoutExtension = filenameWithoutExtension.replace(" ", "_")

    # On exécute la commande bash pour convertir
    subprocess.run(["pdftotext", filename, filenameWithoutExtension + ".txt"])

def readTxtFile(filename):
    file = open(filename,"r")
    lines = file.readlines()

    # On affiche la 1ère ligne
    print(lines[0])

# Main 
def launch(filename):
    filenameTxtArray = filename.split(".")
    filenameTxt = filenameTxtArray[0] + ".txt"

    # filenameTxt = nom du fichier avec _ à la place des espaces
    filenameTxt = filenameTxt.replace(" ", "_")

    # Appel des fonctions
    convertPdfFileToTxt(filename)
    readTxtFile(filenameTxt)
    writeFilenameInTxt(fileToWrite, filenameTxt)

# Main
launch(filename)