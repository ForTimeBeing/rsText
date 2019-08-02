import src.woodcuttinginfo as wcinfo


class Player:
    def __init__(self, name):
        self.name = name
        self.woodcuttingXP = 0
        self.axe = wcinfo.axes['bronzeaxe']

    def setAxe(self, x):
        self.axe = x

    def getAxe(self):
        return self.axe

    def setWoodcutting(self, x):
        self.woodcuttingXP = self.woodcuttingXP + x

    def getWoodcutting(self):
        return self.woodcuttingXP
