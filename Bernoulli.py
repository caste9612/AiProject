from __future__ import division
from Utility import documentAnalyse
from Utility import createList
import os
from math import log10


# def bernoulliTrain (dir, vocabulary, percentage):
#
#     tab = []
#     tab.append(vocabulary)
#     tab.append([])
#
#     subdirs = [x[0] for x in os.walk(dir)]
#     partial = 0
#     for subdir in subdirs:
#         if subdir != "/home/antonio/Scrivania/AI/newsgroups/":
#             partial += 1
#             #1 sta per laplace smoothing
#             tabTmp = [1] * len(vocabulary)
#             tab[1].append(subdir)
#             print subdir
#             files = createList(subdir)
#             for i in range((len(vocabulary))):
#                 count = 0
#                 print str(partial) + "/" + str(len(subdirs)-1) + " :" + str((int)((i * 100)/len(vocabulary))) + " %"
#                 for file in files:
#                     if count > (len(files) / 100) * percentage:
#                         break
#                     count += 1
#                     tmp = []
#                     documentAnalyse(tmp, file)
#                     for j in range(len(tmp)):
#                         if vocabulary[i] == tmp[j] and vocabulary[i] != "\n":
#                             tabTmp[i] = tabTmp[i]+1
#                             break
#                     # + 2 per Laplace?
#                     tabTmp[i] = tabTmp[i] / count + len(vocabulary)
#             tab.append(tabTmp)
#
#
#     return tab



# def bernoulliCompute(document, dir, tab, percentage):
#     # Creo l'array con le parole del documento
#     doc = []
#     documentAnalyse(doc, document)
#
#     # Creo il vettore che segnala per ogni parola del vocabolario se e presente o meno nel documento
#     b = [0] * len(tab[0])
#     for i in range(len(tab[0])):
#         for j in range(len(doc)):
#             if doc[j] == tab[0][i]:
#                 b[i] = 1
#                 break
#
#
#     cond1 = []
#     subdirs = [x[0] for x in os.walk(dir)]
#     for subdir in subdirs:
#         if subdir != "/home/antonio/Scrivania/AI/newsgroups/":
#
#             #Inizializzo la probabilita e cerco la ctaegoria per sapere quale riga di tab controllare
#             for i in range(len(tab[1])):
#                 if subdir == tab[1][i]:
#                     k = i + 2
#                     break
#             #Per ogni parola del dizionario
#             tmp = 1
#             i = 0
#             for p in tab[k]:
#                 if b[i] == 0:
#                     tmp = tmp * (1-p)
#                 else:
#                     tmp = tmp * p
#                 i += 1
#             prova1 = (tab[1][k-2]).split("/")
#             cond1.append(prova1[len(prova1)-1])
#             cond1.append(tmp)
#     print cond1
#     cond2 = []
#
#     #Per ogni categoria
#     iterator = 0
#     for cat in tab[1]:
#         files = createList(cat)
#         totalFiles = createList(dir)
#         print (((len(files)/len(totalFiles))*percentage)/100)
#         tmp1 = cond1[iterator+1] * (((len(files)/len(totalFiles))*percentage)/100)
#         tmp2 = 0
#         for i in range(1,len(cond1),2):
#             tmp2 = tmp2 + (cond1[i] * (((len(files)/len(totalFiles))*percentage)/100))
#         cond2.append(cond1[iterator])
#         #Per evitare il problema della divisione per 0 dovrei usare laplace smoothing,per ora:
#         if tmp2 != 0:
#             cond2.append(tmp1 / tmp2)
#         else:
#             cond2.append(tmp2)
#         iterator += 2
#
#     print cond2
#     max = 1
#     for i in range(3,len(cond2),2):
#         if cond2[i] > cond2[max]:
#             max = i
#     print "Classe predetta per il documento " + document + " : " + cond2[max-1]


def bernoulliTrain (dir, vocabulary, percentage):

    tab = []
    tab.append(vocabulary)
    tab.append([])
    partial = 0
    totalFiles = createList(dir)
    prior = []

    subdirs = [x[0] for x in os.walk(dir)]
    partial = 0
    for subdir in subdirs:
        if subdir != "/home/antonio/Scrivania/AI/newsgroups/":
            partial += 1
            #1 sta per laplace smoothing
            tabTmp = [0] * len(vocabulary)
            tab[1].append(subdir)
            print subdir
            files = createList(subdir)
            prior.append(len(files)/len(totalFiles))
            for i in range((len(vocabulary))):
                count = 0
                print str(partial) + "/" + str(len(subdirs)-1) + " :" + str((int)((i * 100)/len(vocabulary))) + " %"
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
        if subdir != "/home/antonio/Scrivania/AI/newsgroups/":

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
                print score
                i += 1
            prova1 = (tab[1][k-2]).split("/")
            cond.append(prova1[len(prova1)-1])
            cond.append(score)
    print cond


    max = 1
    for i in range(3,len(cond),2):
        if cond[i] > cond[max]:
            max = i
    print "Credo che il documento " + document + " parli di : " + cond[max - 1]


