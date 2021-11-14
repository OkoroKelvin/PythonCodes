class Fruit:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr

    def details(self):
        print("My" + self.name +
              "is"
              + self.colour)


voice = Fruit("Tobi", "Red")
voice.details()
