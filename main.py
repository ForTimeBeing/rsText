import math
from src.gui.gui import createGUI

# TODO Create pygame GUI
# Checks for save game, Get's data from save game
# TODO Create/Return saved game
def checkForSaveGame():
    return


# Generates XP level list 1-99
def generateXPlevelList():
    xp = 0
    xp_list = []
    for level in range(1, 99):
        diff = int(level + 300 * math.pow(2, float(level) / 7))
        xp += diff
        xp_list.append(xp / 4)
    return xp_list


def game():
    checkForSaveGame()
    xp_list = generateXPlevelList()
    createGUI()

if __name__ == "__main__":
    game()
