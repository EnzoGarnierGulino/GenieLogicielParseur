#!/usr/bin/python3

path = "../Corpus/"
filename = "Torres.txt"
fileToWrite = "resultat.txt"
file = path + filename

## Variables à déclarer

startOfBlock = 0
endOfBlock = 0
titleValue = 60

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
    titleFirstLine = getStartOfBlockWithYMin()
    titleLastLine = getEndOfBlockWithLineNumber(titleFirstLine)
    content = getContentOfBlockWithStartAndEndOfBlock(titleFirstLine, titleLastLine)
    writeInTxt(fileToWrite, content)

launch()