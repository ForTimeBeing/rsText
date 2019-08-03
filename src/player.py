import src.woodcuttinginfo as wcinfo


class Player:
    def __init__(self, name):
        self.name = name
        self.woodcuttingXP = 0
        self.handslot = wcinfo.axes['bronzeaxe']
        self.offhandslot = None

    def setHandSlot(self, x):
        self.handslot = x

    def setHandSlot(self):
        return self.handslot

    def setOffHandSlot(self,x):
        self.offhandslot = x

    def getOffHandSlot(self):
        return self.offhandslot

    def setWoodcutting(self, x):
        self.woodcuttingXP = self.woodcuttingXP + x

    def getWoodcutting(self):
        return self.woodcuttingXP
