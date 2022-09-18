class Player:
    name = ''
    brain = 0
    shots = 0
    tempBrains = 0

    def __init__(self, name):
        self.name = name

    def points(self):
        print("Brains: ", self.brain, "\n")

    def newRound(self):
        print("U Have ", self.brain, " brains")
        self.shots = 0
        print("Reset Shots: ", self.shots)

    def addTempBrain(self):
        self.tempBrains = self.tempBrains + 1
        print("Add Brain")

    def addShot(self):
        self.shots = self.shots + 1
        print("Add Shot")

    def validRound(self):
        print("Brains: ", self.tempBrains, "\n")
        print("Shots: ", self.shots, "\n")
