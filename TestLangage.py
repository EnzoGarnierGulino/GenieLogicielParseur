#!/usr/bin/python3
import subprocess

filename = "ACL2004-HEADLINE.pdf"
path = "../Corpus/"
fileToWrite = "SD/texte.txt"

def initializeTxt(fileToCreate):
    f = open(fileToCreate, 'w').close()

def writeInTxt(fileToWrite, whatToWrite):
    with open(fileToWrite, 'a') as f:
        f.write(whatToWrite)
        f.write("\n")

def convertPdfFileToTxt(filename):
    filenameWithoutExtensionArray = filename.split(".")
    filenameWithoutExtension = filenameWithoutExtensionArray[0]

    # filenameWithoutExtension = nom du fichier avec _ à la place des espaces
    filenameWithoutExtension = filenameWithoutExtension.replace(" ", "_")

    # On exécute la commande bash pour convertir
    subprocess.run(["pdftotext", path + filename, path + filenameWithoutExtension + ".txt"])

def readTxtFile(filename):
    f = open(path + filename,"r")
    lines = f.readlines()

    # On affiche la 1ère ligne
    print(lines[0])

def getAbstract(filename):
    f = open(path + filename,"r")
    lines = f.readlines()
    content = ""
    vide = False
    
    ## lines est un tableau qui contient tout le texte
    for i in range(0, len(lines)):
        
        
        linesTable = lines[i].split(" ")
        if (linesTable[0] == "Abstract") or (linesTable[0] == "Abstract\n") or (linesTable[0] == "ABSTRACT") or (linesTable[0] == "ABSTRACT\n"):
            content = ""

        if vide == True:
            if (linesTable[0] == "Introduction") or (linesTable[0] == "Introduction\n") or (linesTable[0] == "INTRODUCTION") or (linesTable[0] == "INTRODUCTION\n") or (linesTable[0] == "1") or (linesTable[0] == "1\n") or (linesTable[0] == "I."):
                return content
            if (len(linesTable) > 1):
                if (linesTable[1] == "Introduction") or (linesTable[1] == "Introduction\n") or (linesTable[1] == "INTRODUCTION\n") or (linesTable[1] == "INTRODUCTION\n") or (linesTable[1] == "1") or (linesTable[1] == "1\n") or (linesTable[1] == "I."):
                    return content
            else:
                content = ""
                vide = False

        # Si la ligne est vide
        if lines[i] == "\n":
            vide = True
        else:
            content = content + lines[i]

# Main 
def launch(filename):

    # On vide le .txt
    initializeTxt(fileToWrite)

    filenameTxtArray = filename.split(".pdf")
    filenameTxt = filenameTxtArray[0] + ".txt"

    # filenameTxt = nom du fichier avec _ à la place des espaces
    filenameTxt = filenameTxt.replace(" ", "_")

    # Appel des fonctions :
    # Conversion du pdf en txt
    convertPdfFileToTxt(filename)

    # Écriture du nom du fichier pdf
    writeInTxt(fileToWrite, filenameTxt)

    # Écriture de l'abstract
    abstract = getAbstract(filenameTxt)

    if abstract:
        print(abstract)
        writeInTxt(fileToWrite, abstract)
    else:
        print("Il n'y a pas d'abstract dans ce document")

# Main
launch(filename)