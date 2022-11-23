#!/usr/bin/python3

path = "../Corpus/"
filename = "compression.txt"
fileToCreate = "resultat.txt"
file = path + filename

## Variables à déclarer

startOfBlock = 0
endOfBlock = 0

## Numéro du bloc qu'on veut afficher

blocNumber = 6

def initializeTxt(fileToCreate):
    f = open(fileToCreate, 'w').close()

def writeInTxt(fileToWrite, whatToWrite):
    with open(fileToWrite, 'a') as f:
        f.write(whatToWrite)

def getStartOfBlock(blockNumber):
    f = open(path + filename, "r")
    lines = f.readlines()
    compteur = 1
    nbLigneDep = 0

    for i in range(0, len(lines)):
        linesTable = lines[i].split(" ")

        ## Si on entre dans un block
        for j in range(0, len(linesTable)):
            if linesTable[j] == "<block" and compteur == blockNumber:
                nbLigneDep = i + 1
                return nbLigneDep

            if linesTable[j] == "<block":
                compteur = compteur + 1

def getEndOfBlock(blockNumber):
    f = open(path + filename, "r")
    lines = f.readlines()
    compteur = 1
    nbLigneArr = 0

    for i in range(0, len(lines)):
        linesTable = lines[i].split(" ")

        ## Si on entre dans un block
        for j in range(0, len(linesTable)):
            if linesTable[j] == "</block>\n" and compteur == blockNumber:
                nbLigneArr = i + 1
                return nbLigneArr

            if linesTable[j] == "</block>\n":
                compteur = compteur + 1
  
def getContentOfBlockWithStartAndEndOfBlock(startOfBlock, endOfBlock):
    content = ""
    for i in range(startOfBlock, endOfBlock):
        content = content + getContentFromLine(i)
    return content

def getContentFromLine(lineNumber):
    f = open(path + filename, "r")
    lines = f.readlines()
    content = ""

    ## On supprime les lignes vides
    lineTable = lines[lineNumber - 1].split(" ")

    for i in range(0, len(lineTable)):
        if lineTable[i] == "<word":
            lineSplit = lines[lineNumber - 1].split(">")
            lineSplitSplit = lineSplit[1].split("</")
            content = lineSplitSplit[0] + " "

    return content

def launch():   
    initializeTxt(fileToCreate)
    startOfBlock = getStartOfBlock(blocNumber)
    endOfBlock = getEndOfBlock(blocNumber)
    content = getContentOfBlockWithStartAndEndOfBlock(startOfBlock, endOfBlock)
    writeInTxt(fileToCreate, content)
    
launch()