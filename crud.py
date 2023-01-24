class Crud:
    def __init__(self):
        self.elementList = []

    def create(self, element):
        self.elementList.append(element)
    
    def read(self):
        return self.elementList
    
    def update(self, oldElement, newElement):
        for item in self.elementList:
            if item == oldElement:
                self.elementList.remove(item)
                self.elementList.append(newElement)
    
    def delete(self, element):
        self.elementList.remove(element)