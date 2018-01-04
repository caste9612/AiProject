from __future__ import division
from Utility import createList
from Utility import documentAnalyseToken
import os
from math import log10

def multinomialTrain(dir, vocabulary, percentage,trainSet):

    print "MultinomialTrain start..."


    tab = []
    tab.append(vocabulary)
    tab.append([])
    totalFiles = trainSet
    prior = []
    total = 0


    subdirs = [x[0] for x in os.walk(dir)]
    partial = 0
    for subdir in subdirs:
        if subdir != dir:
            partial += 1
            counter3 = 0
            #1 sta per laplace smoothing
            tabTmp = [1] * len(vocabulary)
            tab[1].append(subdir)
            files = []
            for i in (totalFiles):
                a = subdir.split("/")
                b = i.split("/")
                if a[len(a) - 1] == b[len(b) - 2]:
                    files.append(i)
            prior.append(len(files)/len(totalFiles))

            words = []
            for file in files:
                documentAnalyseToken(words, file)

            for i in range((len(vocabulary))):
                    for j in range(len(words)):
                        tmp = int((i * 100)/len(vocabulary))
                        if tmp != counter3:
                            counter3 = tmp
                            print str(partial) + "/" + str(len(subdirs)-1) + " :" + str(counter3) + " %"
                        if vocabulary[i] == words[j] and vocabulary[i] != "\n":
                            tabTmp[i] += 1
                            total += 1
            tab.append(tabTmp)

    for i in range(2,len(tab)):
        for j in range(len(tab[i])):
            #+1000 per laplace,diviso 1000 o 20 000?
            tab[i][j] = tab[i][j] / (total + len(vocabulary))

    tab.append(prior)
    return tab

def multinomialCompute(document, dir, tab):


    doc = []
    documentAnalyseToken(doc,document)

    cond = []

    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:
        if subdir != dir:

            # Inizializzo la probabilita e cerco la ctaegoria per sapere quale riga di tab controllare
            for i in range(len(tab[1])):
                if subdir == tab[1][i]:
                    k = i + 2
                    break

            score = log10(tab[len(tab)-1][k-2])

            for i in range(len(doc)):
                for j in range(len(tab[0])):
                    if doc[i] == tab[0][j]:
                        score += log10(tab[k][j])

            cond.append(subdir)
            cond.append(score)

    max = 1
    for i in range(3, len(cond), 2):
        if cond[i] > cond[max]:
            max = i
    prov = document.split("/")
    prov1 = cond[max - 1].split("/")
    #print "Credo che il documento " + prov[len(prov)-1] + "(" + prov[len(prov)-2] + ")" + " parli di : " + prov1[len(prov1)-1]
    return prov1[len(prov1) - 1]



