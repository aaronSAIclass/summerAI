class Staff:
    def __init__(self, position, xPos, yPos, zPos, isActive, room):
        self.position = position
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
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
    def moveZ(self, z1):
        self.zPos += z1

s1 = Staff("Math Teacher", 1, 3, 1, True, 0)
s2 = Staff("English Teacher", 0, 2, 4, False, 1)
s3 = Staff("History Teacher", 3, 3, 1, False, 2)
s4 = Staff("Biology Teacher", 4, 3, 4, False, 4)
s5 = Staff("Janitor", 1, 2, 2, False, 5)
s6 = Staff("Headmaster", 0, 0, 1, False, 7)
s7 = Staff("Art Teacher", 1, 2, 4, False, 6)
