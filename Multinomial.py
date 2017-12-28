from Utility import createList
from Utility import documentAnalyse
import os

def multinomialTrain(dir, vocabulary, percentage):

    tab = []
    tab.append(vocabulary)
    tab.append([])

    totalWords = 0

    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:
        if subdir != "/home/antonio/Scrivania/AI/newsgroups/":
            #1 sta per laplace smoothing
            tabTmp = [1] * len(vocabulary)
            tab[1].append(subdir)
            print subdir
            files = createList(subdir)
            for i in range((len(vocabulary))):
                count = 0
                print str((i * 100)/len(vocabulary)) + " %"
                for file in files:
                    if count > (len(files) / 100) * percentage:
                        break
                    count += 1
                    tmp = []
                    documentAnalyse(tmp, file)
                    totalWords += len(tmp)
                    for j in range(len(tmp)):
                        if vocabulary[i] == tmp[j] and vocabulary[i] != "\n":
                            tabTmp[i] = tabTmp[i]+1
            tab.append(tabTmp)

    for i in range(2,len(tab)):
        for j in range(len(tab[i])):
            #+1000 per laplace,diviso 1000 o 20 000?
            tab[i][j] = tab[i][j] / (totalWords + len(vocabulary))


    return tab

def multinomialCompute(document, dir, tab):
