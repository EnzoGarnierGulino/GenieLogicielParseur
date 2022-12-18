#!/usr/bin/python3

# python3 XMLReaderRapide.py ../CORPUS_TRAIN/ Torres ../CORPUS_TRAIN/_txt/Torres.xml -x
# ./createfile.sh ../CORPUS_TRAIN/


import sys

path = sys.argv[1]
filename = sys.argv[2]
fileToWrite = sys.argv[3]
file = path + filename


f = open(file + ".html", "r")
lines = f.readlines()

strTitle = ""
strAuthor = ""
strAbstract = ""
strBiblio = ""
isTitle = False
isAuthor = False
endAuthor = False
isAbstract = False

yBlockBefore = 999999999

i = 0
while i < len(lines)-1:
    if not isTitle:
        if lines[i].find("<block") != -1 and float(lines[i].split('"')[3]) >= 60:
            isTitle = True
            i += 1
            while (lines[i].find("</block") == -1):
                if lines[i].find("<line") == -1 and lines[i].find("</line>") == -1:
                    lineSplit = lines[i].split(">")
                    lineSplitSplit = lineSplit[1].split("</")
                    content = lineSplitSplit[0] + " "
                    strTitle += content
                i += 1
    
    elif not isAuthor:
        isAuthor = True
        while not endAuthor:
            while lines[i].find("<block") == -1:
                i += 1
            if float(lines[i].split('"')[3]) - yBlockBefore < 20:
                yBlockBefore = float(lines[i].split('"')[7])
                i += 1
                while (lines[i].find("</block") == -1):
                    if lines[i].find("<line") == -1 and lines[i].find("</line>") == -1:
                        lineSplit = lines[i].split(">")
                        lineSplitSplit = lineSplit[1].split("</")
                        content = lineSplitSplit[0] + " "
                        strAuthor += content
                    i += 1
            else:
                endAuthor = True

    if isTitle and isAuthor and not isAbstract:
        if lines[i].find("<word") != -1 and lines[i].find("</word>") != -1:
            lineSplit = lines[i].split(">")
            lineSplitSplit = lineSplit[1].split("</")
            content = lineSplitSplit[0] + " "

            if lineSplitSplit[0].lower() == "abstract" or lineSplitSplit[0].lower() == "bstract":
                strAbstract = ""
            elif lines[i].lower().find("introduction") != -1 or lines[i].lower().find("ntroduction") != -1:
                isAbstract = True
            else:
                strAbstract += content
    
    if isAbstract:
        if lines[i].find("<word") != -1 and lines[i].find("</word>") != -1:
            lineSplit = lines[i].split(">")
            lineSplitSplit = lineSplit[1].split("</")
            content = lineSplitSplit[0] + " "
            if lines[i].find("References") != -1 or lines[i].find("REFERENCES") != -1 or content.lower() == "eferences" or content.lower() == "eferences.":
                strBiblio = ""
            else:
                strBiblio += content
            
    i += 1



if sys.argv[4] == "-t":
    e = open(fileToWrite, 'w')
    e.write(filename + ".pdf" +"\n"+ strTitle +"\n"+ strAuthor +"\n"+ strAbstract +"\n"+ strBiblio)
    e.close()
else:
    e = open(fileToWrite, 'w')
    e.write("<article> \n\t<preamble> "+ filename + ".pdf" +" </preamble> \n\t<titre> "+ strTitle +" </titre> \n\t<auteur> "+ strAuthor +" </auteur> \n\t<abstract> "+ strAbstract +" </abstract> \n\t<biblio> "+ strBiblio +" </biblio> \n</article>")
    e.close()

f.close()


