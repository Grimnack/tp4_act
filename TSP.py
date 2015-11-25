import random as r

r.seed

def monRemove(liste, element):
    res = []
    for item in liste :
        if item != element:
            res.append(item)
    return res 

class TSP(object):
    """Travelling Salesman Problem"""
    def __init__(self, nVilles, matrice):
        super(TSP, self).__init__()
        self.nVilles = nVilles
        self.matrice = matrice[:]

    def certificatAlea(self) :
        certificat = range(self.nVilles)
        for i in reversed(xrange(1,self.nVilles)) :
            index = r.randint(0,i-1)
            tmp = certificat[i]
            certificat[i] = certificat[index]
            certificat[index] = tmp
        return certificat

    def certificatCorrecte(self, certificat, longueurMax) :
        somme = 0
        for i in range(self.nVilles - 1) :
            somme = somme + self.matrice[certificat[i]][certificat[i+1]]
        somme = somme + self.matrice[certificat[self.nVilles-1]][certificat[0]]
        return somme <= longueurMax


    def enumerateCertificat(self, listeVilles) :
        if len(listeVilles) <= 1 :
            return listeVilles
        listeCertificats = []
        for ville in listeVilles :
            sousListe = monRemove(listeVilles,ville)
            listeCertificats.append(sousListe.insert(0,ville))
        return listeCertificats
                

tsp = TSP(4,[[0,2,5,7],[7,0,8,1],[2,1,0,9],[2,2,8,0]]) 


# test certificat correcte
# A C B D = 0 2 1 3
# WORKS

# print tsp.certificatCorrecte([0,2,1 ,3],9)
# print tsp.certificatCorrecte([0,2,1,3],8)

# test de certificatAlea
# WORKS
# for x in range(10) :
#     print tsp.certificatAlea()


shortTSP = TSP(3,[[0,2,5,7],[7,0,8,1],[2,1,0,9],[2,2,8,0]])
# test de enumerateCertificat

print shortTSP.enumerateCertificat([0,1])
