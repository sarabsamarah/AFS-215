class Oils:
    def __init__(self):
        self.oilList = []

    def printOils(self):
        print(self.oilList)

    def addOils(self, newOilString):
        self.oilList.append(newOilString)

    def changeList(self):
        self.oilList = tuple(self.oilList)

print('o')

o = Oils()

o.printOils()

o.addOils('Copaiba')
o.printOils()
o.addOils(("Frankensence", "Sage", "Lavendar"))
o.printOils()
o.addOils({'oilName':'Orange','type':'sweet'})
o.printOils()
o.addOils(1)
o.printOils()

o.changeList()
o.printOils()