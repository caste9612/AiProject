from __future__ import division
from Utility import documentAnalyseToken
import os
from math import log

def multinomialTrain(dir, vocabulary, percentage,trainSet):

    print "MultinomialTrain start..."


    tab = []
    tab.append(vocabulary)
    tab.append([])
    totalFiles = trainSet
    prior = []

    subdirs = [x[0] for x in os.walk(dir)]
    partial = 0
    for subdir in subdirs:
        if subdir != dir:
            total = 0
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
                        if vocabulary[i] == words[j]:
                            tabTmp[i] += 1
                            total += 1
            for i in range(len(tabTmp)):
                tabTmp[i] = tabTmp[i]/(total + len(vocabulary))
            tab.append(tabTmp)

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

            score = log(tab[len(tab)-1][k-2])

            for i in range(len(doc)):
                for j in range(len(tab[0])):
                    if doc[i] == tab[0][j]:
                        score += log(tab[k][j])
                        break

            cond.append(subdir)
            cond.append(score)

    max = 1
    for i in range(3, len(cond), 2):
        if cond[i] > cond[max]:
            max = i
    #uncomment per stampare le predizioni file per file
    #prov = document.split("/")
    prov1 = cond[max - 1].split("/")
    #print "Credo che il documento " + prov[len(prov)-1] + "(" + prov[len(prov)-2] + ")" + " parli di : " + prov1[len(prov1)-1]
    return prov1[len(prov1) - 1]



