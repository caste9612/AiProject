from Utility import createVocoabulary
from Bernoulli import bernoulliTrain
from Bernoulli import bernoulliCompute
import pickle





path = '/home/antonio/Scrivania/AI/newsgroups/'


#voc = createVocoabulary(path)
#with open("Vocabulary", "wb") as fp:
    #pickle.dump(voc, fp)

with open("Vocabulary", "rb") as fp:
    voc = pickle.load(fp)

#tab = bernoulliTrain(path,voc,60)
#with open("Tabella", "wb") as fp:
    #pickle.dump(tab, fp)



with open ("Tabella", "rb") as fp:
    tab = pickle.load(fp)

print tab
print tab



bernoulliCompute("/home/antonio/Scrivania/AI/newsgroups/sci.space/60155", path, tab)



