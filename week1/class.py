class Oils:
    def __init__(self):
        self.oilList = []

    def printOils(self):
        print(self.oilList)

    def addOils(self, newOilString):
        self.oilList.append(newOilString)

    def changeList(self):
        self.oilList = tuple(self.oilList)

print('x')

x = Oils()

x.printOils()

x.addOils('Copaiba')
x.printOils()
x.addOils(("Frankensence", "Sage", "Lavendar"))
x.printOils()
x.addOils({'oilName':'Orange','type':'sweet'})
x.printOils()
x.addOils(1)
x.printOils()

x.changeList()
x.printOils()