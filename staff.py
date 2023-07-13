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



