from __future__ import division
from Utility import documentAnalyse
#from Utility import createList
import os
from math import log10

def bernoulliTrain (dir, vocabulary, percentage, trainSet):

    print "BernoulliTrain start..."

    tab = []
    tab.append(vocabulary)
    tab.append([])
    totalFiles = trainSet
    prior = []


    subdirs = [x[0] for x in os.walk(dir)]
    partial = 0
    for subdir in subdirs:
        if subdir != dir:
            counter = 0
            partial += 1
            #1 sta per laplace smoothing
            tabTmp = [0] * len(vocabulary)
            tab[1].append(subdir)
            files = []
            for i in (totalFiles):
                a = subdir.split("/")
                b = i.split("/")
                if a[len(a)-1] == b[len(b)-2]:
                    files.append(i)
            prior.append(len(files)/len(totalFiles))
            for i in range((len(vocabulary))):
                count = 0
                t = int((i * 100)/len(vocabulary))
                if t != counter:
                    counter = t
                    print str(partial) + "/" + str(len(subdirs)-1) + " :" + str(counter) + " %"
                for file in files:
                    if count > (len(files) / 100) * percentage:
                        break
                    count += 1
                    tmp = []
                    documentAnalyse(tmp, file)
                    for j in range(len(tmp)):
                        if vocabulary[i] == tmp[j] and vocabulary[i] != "\n":
                            tabTmp[i] = tabTmp[i]+1
                            break
                    # + 2 per Laplace?
                tabTmp[i] = (tabTmp[i] + 1) / (len(files) + 2)
            print tabTmp
            tab.append(tabTmp)
    tab.append(prior)
    return tab

def bernoulliCompute(document, dir, tab):


    # Creo l'array con le parole del documento (solo se gia presenti nel vocabolario)
    doc = []
    documentAnalyse(doc, document)

    # Creo il vettore che segnala per ogni parola del vocabolario se e presente o meno nel documento
    b = [0] * len(tab[0])
    for i in range(len(tab[0])):
        for j in range(len(doc)):
            if doc[j] == tab[0][i]:
                b[i] = 1
                break


    cond = []
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:
        if subdir != dir:

            #Inizializzo la probabilita e cerco la ctaegoria per sapere quale riga di tab controllare
            for i in range(len(tab[1])):
                if subdir == tab[1][i]:
                    k = i + 2
                    break
            #Per ogni parola del dizionario
            score = log10((tab[len(tab)-1][k-2]))
            i = 0
            for p in tab[k]:
                if b[i] == 0:
                    score += log10(1-p)
                else:
                    score += log10(p)
                i += 1
            prova1 = (tab[1][k-2]).split("/")
            cond.append(prova1[len(prova1)-1])
            cond.append(score)


    max = 1
    for i in range(3,len(cond),2):
        if cond[i] > cond[max]:
            max = i
    prov = document.split("/")
    prov1 = cond[max - 1].split("/")
    #print "Credo che il documento " + prov[len(prov) - 1] + "(" + prov[len(prov) - 2] + ")" + " parli di : " + prov1[len(prov1) - 1]
    return prov1[len(prov1) - 1]

