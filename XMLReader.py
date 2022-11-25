#!/usr/bin/python3

path = "../Corpus/"
filename = "mikheev.txt"
fileToWrite = "resultat.txt"
file = path + filename

## Variables à déclarer

startOfBlock = 0
endOfBlock = 0
titleValue = 60
differenceMax = 25

## Fonctions

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
        
def getNumberOfBlockWithStart(startLine):
    f = open(path + filename, "r")
    lines = f.readlines()
    compteur = 0

    for i in range(0, startLine):
        linesTable = lines[i].split(" ")

        for j in range(0, len(linesTable)):
            if linesTable[j] == "<block":
                compteur = compteur + 1

    return compteur

def getNumberOfLinesWhereBlockStarts():
    f = open(path + filename, "r")
    lines = f.readlines()
    compteur = 0
    blockStarts = []

    for i in range(0, len(lines)):
        linesTable = lines[i].split(" ")

        for j in range(0, len(linesTable)):
            if linesTable[j] == "<block":
                blockStarts.append(i + 1)
                compteur = compteur + 1

    return blockStarts
  
def getEndOfBlockWithLineNumber(lineNumber):
    f = open(path + filename, "r")
    lines = f.readlines()
    nbLigneArr = lineNumber

    for i in range(lineNumber, len(lines)):
        linesTable = lines[i].split(" ")
        nbLigneArr = nbLigneArr + 1

        ## Si on entre dans un block
        for j in range(0, len(linesTable)):
            if linesTable[j] == "</block>\n":
                return nbLigneArr

def getContentOfBlockWithStartAndEndOfBlock(startOfBlock, endOfBlock):
    content = ""
    for i in range(startOfBlock, endOfBlock):
        content = content + getContentFromLine(i)
    return content

def getAuteurs(titreNum):
    content = ""
    blocksLineNumbers = getNumberOfLinesWhereBlockStarts()
    coordinates = []
    yMin = []
    yMax = []
    
    for i in range(titreNum, len(blocksLineNumbers)):
        coordinates = getCoordinatesFromLine(blocksLineNumbers[i])
        yMin.append(coordinates[1])
        yMax.append(coordinates[3])

    for j in range(titreNum, len(blocksLineNumbers)):
        blocNum = getNumberOfBlockWithStart(blocksLineNumbers[j])
        endBlock = getEndOfBlock(blocNum)
        content = content + getContentOfBlockWithStartAndEndOfBlock(blocksLineNumbers[j], endBlock)
        if not abs(float(yMin[j]) - float(yMax[j-1])) < differenceMax:
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

def getCoordinatesFromLine(lineNumber):
    f = open(path + filename, "r")
    lines = f.readlines()
    coordinates = []

    ## On supprime les lignes vides
    lineTable = lines[lineNumber - 1].split(" ")

    for i in range(0, len(lineTable)):
        if lineTable[i].startswith("xMin") or lineTable[i].startswith("yMin") or lineTable[i].startswith("xMax") or lineTable[i].startswith("yMax"):
            lineSplit = lineTable[i].split("=")
            lineSplitSplit = lineSplit[1].split('"')
            coordinates.append(lineSplitSplit[1])

    return coordinates

def getStartOfBlockWithYMin():   
    f = open(path + filename, "r")
    lines = f.readlines()
    table = []

    for i in range (0, len(lines)):
        table = getCoordinatesFromLine(i)
        if len(table):
            if (float(table[1]) > titleValue):
                return i

def launch():
    initializeTxt(fileToWrite)

    # Titre
    titleFirstLine = getStartOfBlockWithYMin()
    titleLastLine = getEndOfBlockWithLineNumber(titleFirstLine)
    titrePapier = getContentOfBlockWithStartAndEndOfBlock(titleFirstLine, titleLastLine)
    titreNum = getNumberOfBlockWithStart(titleFirstLine)

    # Auteurs
    auteurs = getAuteurs(titreNum)
    
    # Écriture + Mise en forme
    writeInTxt(fileToWrite, " TITRE : ")
    writeInTxt(fileToWrite, titrePapier)
    writeInTxt(fileToWrite, "\n")
    writeInTxt(fileToWrite, " AUTEURS : ")
    writeInTxt(fileToWrite, auteurs)
    writeInTxt(fileToWrite, "\n")

# Lancer le programme
launch()