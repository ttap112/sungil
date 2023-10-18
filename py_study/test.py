class nameSet:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


petSet = str(input("이름 : "))
pet = nameSet(petSet)

print(pet)
