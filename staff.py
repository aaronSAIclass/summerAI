
import random

class Player:
    def __init__(self, xPos, yPos):
        self.room = 0
        self.xPos = xPos
        self.yPos = yPos
        self.isAlive = True
    def moveRooms(self, room2):
        self.room = room2
    def moveX(self, x1):
        self.xPos += x1    
    def moveY(self, y1):
        self.yPos += y1
    def setPos(self, x2, y2):
        self.xPos = x2
        self.yPos = y2
    def getX(self):
        return self.xPos
    def getY(self):
        return self.yPos
    def getPos(self):
        return self.xPos, self.yPos
    def kill(self):
        self.isAlive = False
    def setX(self, num):
        self.xPos = num
    def setY(self, num):
        self.yPos = num
    
class Exit:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
      
    def setPos(self, x2, y2):
        self.xPos = x2
        self.yPos = y2
       
    def getPos(self):
        return self.xPos, self.yPos
    def getX(self):
        return self.xPos
    def getY(self):
        return self.yPos
    


class Staff:
    def __init__(self, position, xPos, yPos, isActive, room):
        self.position = position
        self.xPos = xPos
        self.yPos = yPos
       
        self.isActive = isActive
        self.room = room
    
    def activate(self):
        self.isActive = True
    def deactivate(self):
        self.isActive = False
    def moveRooms(self, room2):
        self.room = room2
    def changeJob(self, job):
        self.position = job
    def moveX(self, x1):
        self.xPos += x1    
    def moveY(self, y1):
        self.yPos += y1
    def setPos(self, x2, y2):
        self.xPos = x2
        self.yPos = y2
    def getX(self):
        return self.xPos
    def getY(self):
        return self.yPos
    def getPos(self):
        return self.xPos, self.yPos
    def chooseDirection(self):
        p = random.randint(0, 1)
        match p:
            case 1:
                return 1
            case 2:
                return 2
            case _:
                return 1
    def isOn(self):
        return self.isActive
    def getPosition(self):
        return self.position
    def setX(self, num):
        self.xPos = num
    def setY(self, num):
        self.yPos = num
              
    
def randomRoomPosInt():
    return random.randint(0, 3)  
def randomLarge():
    return random.randint(0, 7) 
def compareTeacherPos(player, lst):
    
    for i in range(len(lst)):
        if(lst[i].isActive ==  True):
            
            if(player.getX() == lst[i].getX() and player.getY() == lst[i].getY()):
                player.setPos(randomRoomPosInt(), randomRoomPosInt())
                return False
    return True
def playerIsCaught(player, lst):
    q = compareTeacherPos(player, lst)
    if(q == False):
        return True
    else:
        return False

def playerIsAtExit(player, exit):
    if(player.getX() == exit.getX() and player.getY() == exit.getY()):
        return True
    return False

def placeInRoom(player, lst):
    q = compareTeacherPos(player, lst)
                
              
    if(q == False):
        player.setPos(randomRoomPosInt(), randomRoomPosInt())
        placeInRoom(player, lst)    
    else:
        print("Player Pos")    
        print(player.getPos())
        for i in range(len(lst)):
            if(lst[i].isActive ==  True):
                print("The", lst[i].getPosition(), "is at", lst[i].getPos())
def bounds(num):
    if(num < 0):
        num = 0
    if(num > 3):
        num = 3
    return num

def move(player):
    typo = input("Choose move direction. 1 for x and 2 for y")
    crap = ""
    match typo:
        case "1":
            print("X chosen")
            crap = input("Choose to go positive or negative. Bounds are 0 and 3. 1 for positive, 2 for negative.")
            moveX(player, crap)
        case "2":
            print("Y chosen")
            crap = input("Choose to go positive or negative. Bounds are 0 and 3. 1 for positive, 2 for negative.")
            moveY(player, crap)
        case _:
            print("X chosen")
            crap = input("Choose to go positive or negative. Bounds are 0 and 3. 1 for positive, 2 for negative.")
            moveX(player, crap)

def moveX(player, direction):
    match direction:
        case "1":
            number = bounds(player.getX()+1)
            player.setX(number)
        case "2":
            number = bounds(player.getX()-1)
            player.setX(number)
        case _:
            number = bounds(player.getX()+1)
            player.setX(number)
    print("New Pos", player.getPos())

def moveY(player, direction):
    match direction:
        case "1":
            number = bounds(player.getY()+1)
            player.setY(number)
        case "2":
            number = bounds(player.getY()-1)
            player.setY(number)
        case _:
            number = bounds(player.getY()+1)
            player.setY(number)
    print("New Pos", player.getPos())

def teacherMove(teacher):
    pt = random.randint(0,1)
    numba = 0
    match pt:
        case 0:
            numba = 1
        case 1:
            numba = -1
        case _:
            numba  = 1
    pt2 = random.randint(0,1)
    
    match pt2:
        case 0:
            teacherMoveX(teacher, numba)
        case 1:
            teacherMoveY(teacher, numba)
        case _:
            teacherMoveX(teacher, numba)
def teacherMoveX(teacher, num):
    number = bounds(teacher.getX()+num)
    teacher.setX(number)
    print("The", teacher.getPosition(), "is at", teacher.getPos())
def teacherMoveY(teacher, num):
    number = bounds(teacher.getY()+num)
    teacher.setY(number)
    print("The", teacher.getPosition(), "is at", teacher.getPos())



   

s1 = Staff("Math Teacher", randomRoomPosInt(), randomRoomPosInt(), True, 0)
s2 = Staff("English Teacher", randomRoomPosInt(),randomRoomPosInt(), False, 1)
s3 = Staff("History Teacher", randomRoomPosInt(), randomRoomPosInt(),  False, 2)
s4 = Staff("Biology Teacher", randomRoomPosInt(), randomRoomPosInt(),  False, 4)
s5 = Staff("Janitor", randomRoomPosInt(),randomRoomPosInt(), False, 5)
s6 = Staff("Headmaster", randomRoomPosInt(), randomRoomPosInt(),  False, 7)
s7 = Staff("Art Teacher", randomRoomPosInt(), randomRoomPosInt(), False, 6)
e1 = Exit(randomRoomPosInt(), randomRoomPosInt())
lst = [s1, s2, s3, s4, s5, s6, s7]

name = input("Welcome to the game! Please enter your name!")
print("Hello ", name,"!")
p1 = Player(randomRoomPosInt(), randomRoomPosInt())

placeInRoom(p1, lst)
print("Exit at", e1.getPos())
win = False
while(p1.isAlive == True and win == False):
    move(p1)
    for i in range(len(lst)):
           if(lst[i].isActive ==  True):
               teacherMove(lst[i])
    if(playerIsAtExit(p1, e1) == True):
        print("exit")
        win = True
    else:
        if(playerIsCaught(p1, lst) == True):
            p1.kill()
            print("Game Over")         







