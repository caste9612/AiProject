import os
import string
import pickle



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
        for line in lines:
            thisline = line.split(" ")

            # Per ogni parola
            for i in range(len(thisline)):

                # Filtro per parole vuote  e troppo lunghe e con caratteri speciali(set velocizzano)
                thisline[i] = thisline[i].translate(None, '\t\n ')

                invalidChars = set(string.punctuation.replace("-", ""))
                if any(char in invalidChars for char in thisline[i]):
                    break
                if len(thisline[i]) > 18 or len(thisline) < 3:
                    break
                if not thisline[i]:
                    break
                if thisline[i] == "\n":
                    break

                # Controllo che non sia gia presente nel vocabolario
                for j in range(len(array)):
                    if thisline[i] == array[j]:
                        break
                    if j == len(array) - 1:
                        array.append((thisline[i]))
                if len(array) <= 2:
                    array.append(thisline[i])

def documentAnalyseToken(array, document):
    with open(document) as f:
        # Per ogni riga
        lines = f.readlines()
        for line in lines:
            thisline = line.split(" ")

            # Per ogni parola
            for i in range(len(thisline)):

                # Filtro per parole vuote  e troppo lunghe e con caratteri speciali(set velocizzano)
                thisline[i] = thisline[i].translate(None, '\t\n ')

                invalidChars = set(string.punctuation.replace("-", ""))
                if any(char in invalidChars for char in thisline[i]):
                    break
                if len(thisline[i]) > 18 or len(thisline) < 3:
                    break
                if not thisline[i]:
                    break
                if thisline[i] == "\n":
                    break

                array.append(thisline[i])

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




