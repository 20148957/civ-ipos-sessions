class Student():
    def __init__(self, name, id, units, address):
        self.name = name
        self.id = id
        self.units = units
        self.address = address

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getUnits(self):
        for _ in self.units:
            print(_)

    def setUnits(self, newUnits):
        self.units = newUnits