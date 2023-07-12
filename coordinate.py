class Coordinate:
    def __init__(self, xPos, yPos, zPos):
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos

    def getCoords(self):
        print(" x:",self.xPos," y:",self.yPos," z:", self.zPos)

    def moveX(self, x1):
        self.xPos += x1
        
    def moveY(self, y1):
        self.yPos += y1
    def moveZ(self, z1):
        self.zPos += z1

c1 = Coordinate (25, 27, 29)
c1.getCoords()
c1.moveX(-14)
c1.moveY(10)
c1.moveZ(45)
c1.getCoords()    