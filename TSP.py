import random as r
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--tsp', help = 'importer fichier TSP.py',default = 'probleme.py',type=str)
parser.add_argument('--verification', help = 'saisir un certificat',type = int,  dest='collection', nargs = '+')
parser.add_argument('--exhaustif', help = 'verification exhaustive', action = 'store_true')
parser.add_argument('--nd', help = 'non deterministe verification', action = 'store_true')
r.seed

def monRemove(liste, element):
    res = []
    for item in liste :
        if item != element:
            res.append(item)
    return res 

def ajoutEnTete(liste,element):
    res = [element]
    for item in liste :
        res.append(item)
    return res

class TSP(object):
    """Travelling Salesman Problem"""
    def __init__(self, nVilles, matrice, longueurMax):
        super(TSP, self).__init__()
        self.nVilles = nVilles
        self.matrice = matrice[:]
        self.longueurMax = longueurMax

    def certificatAlea(self) :
        certificat = range(self.nVilles)
        for i in reversed(xrange(1,self.nVilles)) :
            index = r.randint(0,i-1)
            tmp = certificat[i]
            certificat[i] = certificat[index]
            certificat[index] = tmp
        return certificat

    def certificatCorrecte(self, certificat) :
        somme = 0
        for i in range(self.nVilles - 1) :
            somme = somme + self.matrice[certificat[i]][certificat[i+1]]
        somme = somme + self.matrice[certificat[self.nVilles-1]][certificat[0]]
        return somme <= self.longueurMax


    def enumerateCertificat(self, listeVilles) :
        if len(listeVilles) <= 1 :
            return [listeVilles]
        listeCertificats = []
        for ville in listeVilles :
            sousListes = self.enumerateCertificat(monRemove(listeVilles,ville)) 
            for sousListe in sousListes :
                listeCertificats.append(ajoutEnTete(sousListe,ville)) 
        return listeCertificats

    def verification(self, listeCertificats) :
        for certificat in listeCertificats :
            if self.certificatCorrecte(certificat) :
                return (True,certificat)
        return (False,None)

def creeDepuisFichier(f) :
    space = {}
    execfile(f, space)
    data = space['data']
    return TSP(data['nVilles'],data['matrice'],data['longueurMax'])

class HamiltonCycle(object):
    """classe HamiltonCycle un peu bidon juste pour montrer la transformation
    en TSP avec en attributs une matrice de bool et un int le nombre de sommets"""
    def __init__(self, nbSommets, arcs):
        super(HamiltonCycle, self).__init__()
        self.nbSommets = nbSommets
        self.matricebool = arcs

    def matriceInt(self) :
        matriceInt = []
        for ligne in self.matricebool :
            ligneInt = []
            for element in ligne:
                if element :
                    ligneInt.append(1) 
                else :
                    ligneInt.append(nbSommets+1)
            matriceInt.append(ligneInt)
        return matriceInt

    def fileToHamiltonCycle(f) :
        pass

    def reductToTSP() :
        return TSP(self.nbSommets, self.matriceInt(), self.nbSommets)








if __name__ == '__main__':
    result = parser.parse_args()
    tsp = creeDepuisFichier(result.tsp)
    if result.collection != None :
        print 'voici le certificat : ', result.collection
        print 'voici le resultat : ', tsp.certificatCorrecte(result.collection) 
    elif result.exhaustif :
        listeCertificats = tsp.enumerateCertificat(range(tsp.nVilles))
        resultat,certificat = tsp.verification(listeCertificats)
        if resultat :
            print 'il existe bien un certificat :' , certificat
        else :
            print 'il n existe pas de certificat'
    elif result.nd :
        certificat = tsp.certificatAlea()
        print 'voici le certificat Aleatoire : ', certificat
        print 'voici le resultat : ' , tsp.certificatCorrecte(certificat)



# tsp = TSP(4,[[0,2,5,7],[7,0,8,1],[2,1,0,9],[2,2,8,0]],9) 
# tspFaux = TSP(4,[[0,2,5,7],[7,0,8,1],[2,1,0,9],[2,2,8,0]],8)

# test certificat correcte
# A C B D = 0 2 1 3
# WORKS

# print tsp.certificatCorrecte([0,2,1,3])
# print tspFaux.certificatCorrecte([0,2,1,3])

# test de certificatAlea
# WORKS
# for x in range(10) :
#     print tsp.certificatAlea()


# test de enumerateCertificat

# print tsp.enumerateCertificat([0,1,2,3])

    