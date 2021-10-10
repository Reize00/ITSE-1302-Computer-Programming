# Wesslee Whatley 9/19/2021 Robot Vacuum
from random import randint
import time

def resetLevels(robot):
    print("Returning to station...")
    time.sleep(.5)
    print("Resetting levels...")
    time.sleep(.5)
    print("Returning to previous location...")
    time.sleep(.5)
    print("Resuming cleaning operations.")
    return [0, 100, 0, 100] # dust bin, clean water, dirty water, battery


def checkDustBin(robot):
    if robot[0] > 75:
        print("Dust bin full, returning to station to empty.")
        robot = resetLevels(robot)
    return robot
def checkCleanWater(robot):
    if robot[1] < 25:
        print("Clean Water empty, returning to station to fill.")
        robot = resetLevels(robot)
    return robot
def checkDirtyWater(robot):
    if robot[2] > 75:
        print(f"Dirty Water full, returning to station to empty.")
        robot = resetLevels(robot)
    return robot
def checkBattery(robot):
    if robot[3] < 25:
        print(f"Battery low, returning to station to charge.")
        robot = resetLevels(robot)
    return robot

def systemChecks(robot):
    robot = checkDustBin(robot)
    robot = checkCleanWater(robot)
    robot = checkDirtyWater(robot)
    robot = checkBattery(robot)
    print("System Checks Cleared.")
    return (robot)

def generateHard():
    tiles = []
    possibleTiles = ("sweep","mop","obstacle")
    tileNumber = randint(5, 20)
    for tile in range(0, tileNumber):
        tiles.append(possibleTiles[randint(0,2)])
    return tiles

def generateCarpet():
    tiles = []
    possibleTiles = ("vacuum","steam","obstacle")
    tileNumber = randint(5, 20)
    for tile in range(0, tileNumber):
        tiles.append(possibleTiles[randint(0,2)])
    return tiles
        

def cleanRoom(room, robot):
    if room[0] == "stairs":
        for x in range (1, randint(8, 13)):
            print("Vacuuming stair.")
            robot[0] += randint(1, 5) # dust bin
            robot[3] -= 1 # battery
            time.sleep(.1)
            print("Initiating power jump.")
            print("Jumping.")
        return
    elif(room[1] == 'hard'):
        tileList = generateHard()
    else:
        tileList = generateCarpet()

    print(f"Cleaning {room[0]}")
    for tile in tileList:
        if tile == "sweep":
            print("Sweeping.") # vacuuming with spinning sweepers
            time.sleep(.1)
            robot[0] += randint(1, 5) # dust bin
            robot[3] -= 1 # battery
        elif tile == "mop":
            print("Mopping.") # spray clean water, vacuum with wet vac
            time.sleep(.1)
            robot[1] -= randint(1, 5) # clean water
            robot[2] += randint(1, 5) # dirty water
            robot[3] -= 1 # battery
        elif tile == "vacuum":
            print("Vacuuming") # suck up dirt
            time.sleep(.1)
            robot[0] += randint(1, 5) # dust bin
            robot[3] -= 1 # battery
        elif tile == "steam":
            print("Steaming") # spray heated clean water, vacuum with wet vac
            time.sleep(.1)
            robot[1] -= randint(1, 5) # clean water
            robot[2] += randint(1, 5) # dirty water
            robot[3] -= 1 # battery
        elif tile == "obstacle": # cleans room via circling counter-clockwise from the door, obstacles are noted and circled around
            print("Circling around obstacle.")
            time.sleep(.1)
    robot = systemChecks(robot)

def cleanHouse():
    rooms = [
        ('foyer','hard'),
        ('kitchen','hard'),
        ('bathroom','hard'),
        ('office','hard'),
        ('hallway','hard'),
        ('closet','hard'),
        ('stairs','carpet'),
        ('hallway','hard'),
        ('bedroom','carpet'),
        ('bathroom','hard'),
        ('closet','carpet'),
        ('bedroom','carpet'),
        ('closet','carpet')
    ]
    print("Initializing RobotCleaner! Please avoid using stairs while jump jets are in use.")
    robot = [0, 100, 0, 100]
    robot = systemChecks(robot)
    time.sleep(1)
    print("Initialization complete. Beginning cleaning process.\n")
    for room in rooms:
        cleanRoom(room, robot)
        print(f"{room[0]} cleaned, moving to next room.\n")
        time.sleep(.2)
    print("House clean, thank you for using RobotCleaner!")

cleanHouse()