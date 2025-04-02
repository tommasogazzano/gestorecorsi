from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPDwithIscritti(self, pd):
        return DAO.getCorsiPDwithIscritti(pd)

    def getStudentiCorso(self, codins):
        studenti =  DAO.getStudentiCorso(codins)
        studenti.sort(key=lambda s: s.nome)
        return studenti

    def getCDSofCorso(self, codins):
        return DAO.getCDSofCorso(codins)
