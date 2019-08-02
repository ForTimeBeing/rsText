import math
import src.woodcuttinginfo as wcinfo
#Checks for save game, Get's data from save game
def checkForSaveGame():
    return

#Generates XP level list 1-99
def generateXPlevelList():
    xp = 0
    xp_list = []
    for level in range(1, 99):
        diff = int(level + 300 * math.pow(2, float(level) / 7))
        xp += diff
        xp_list.append(xp / 4)
    return(xp_list)


def game():
    checkForSaveGame()
    xp_list = generateXPlevelList()
    print(wcinfo.axes)
    print(wcinfo.trees)

if __name__ == "__main__":
    game()
