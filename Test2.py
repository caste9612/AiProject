from Utility import createVocoabulary
import pickle
from Multinomial import multinomialTrain
from Multinomial import multinomialCompute





path = '/home/antonio/Scrivania/AI/newsgroupsM/'


#voc = createVocoabulary(path)
#with open("Vocabulary1", "wb") as fp:
    #pickle.dump(voc, fp)

with open("Vocabulary1", "rb") as fp:
    voc = pickle.load(fp)

#tab = multinomialTrain(path,voc,100)
#with open("Tabella2", "wb") as fp:
    #pickle.dump(tab, fp)


with open ("Tabella2", "rb") as fp:
    tab = pickle.load(fp)

multinomialCompute("/home/antonio/Scrivania/AI/testM/comp.graphics/39636", path, tab)
multinomialCompute("/home/antonio/Scrivania/AI/testM/comp.graphics/39637", path, tab)
multinomialCompute("/home/antonio/Scrivania/AI/testM/comp.graphics/39638", path, tab)
multinomialCompute("/home/antonio/Scrivania/AI/testM/comp.graphics/39639", path, tab)
multinomialCompute("/home/antonio/Scrivania/AI/testM/comp.graphics/39640", path, tab)

multinomialCompute("/home/antonio/Scrivania/AI/testM/comp.sys.mac.hardware/52321", path, tab)
multinomialCompute("/home/antonio/Scrivania/AI/testM/comp.sys.mac.hardware/52322", path, tab)
multinomialCompute("/home/antonio/Scrivania/AI/testM/comp.sys.mac.hardware/52323", path, tab)
multinomialCompute("/home/antonio/Scrivania/AI/testM/comp.sys.mac.hardware/52324", path, tab)
multinomialCompute("/home/antonio/Scrivania/AI/testM/comp.sys.mac.hardware/52325", path, tab)



