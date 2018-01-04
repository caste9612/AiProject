import os
import string
import pickle
import re




def createVocoabulary(r):

    vocabulary = []
    count = 0

    # Per ogni file
    for fle in r:
        count += 1
        print count
        documentAnalyse(vocabulary ,fle)

    return vocabulary

def documentAnalyse(array, document):
    with open(document) as f:
        # Per ogni riga
        lines = f.readlines()
        check = False
        for line in lines:
            if line == "\n" and check is False:
                check = True
            if check is True:
                thisline = line.split(" ")

                if len(thisline) > 1:
                    thisline = re.findall(r"[\w']+", line)

                    # Per ogni parola
                    for i in range(len(thisline)):

                        # Filtro per parole vuote  e troppo lunghe e con caratteri speciali(set velocizzano)
                        tmp = thisline[i].lower()

                        invalidChars = set(string.punctuation.replace("", "", ))
                        if any(char in invalidChars for char in tmp):
                            tmp = ""

                        if tmp.isdigit() or len(tmp)>20 or len(tmp) < 3:
                            tmp = ""


                        # Controllo che non sia gia presente nel vocabolario
                        if tmp!= "":
                            for j in range(len(array)):
                                if tmp == array[j]:
                                    break
                                if j == len(array) - 1:
                                    array.append(tmp)
                            if len(array) <= 1:
                                array.append(tmp)

def documentAnalyseToken(array, document):
    with open(document) as f:
        # Per ogni riga
        lines = f.readlines()
        check = False
        for line in lines:
            if line == "\n" and check is False:
                check = True
            if check is True:
                thisline = line.split(" ")

                if len(thisline) > 1:
                    thisline = re.findall(r"[\w']+", line)

                    # Per ogni parola
                    for i in range(len(thisline)):

                        # Filtro per parole vuote  e troppo lunghe e con caratteri speciali(set velocizzano)
                        tmp = thisline[i].lower()

                        invalidChars = set(string.punctuation.replace("", "", ))
                        if any(char in invalidChars for char in tmp):
                            tmp = ""

                        if tmp.isdigit() or len(tmp)>20 or len(tmp) < 3:
                            tmp = ""
                        if tmp != "":
                            array.append(tmp)

def write(data, outfile):
    f = open(outfile, "w+b")
    for i in range(len(data)):
        f.writelines(data[i])
        f.write("\n")
    f.close()

def createList(path):
    # Creo la lista dei file
        r = []
        subdirs = [x[0] for x in os.walk(path)]
        for subdir in subdirs:
            files = os.walk(subdir).next()[2]
            if (len(files) > 0):
                for file in files:
                    r.append(subdir + "/" + file)
        return r


