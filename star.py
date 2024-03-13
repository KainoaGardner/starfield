import random
from settings import *

class Star:
    def __init__(self):
        self.x = random.randint(0,WIDTH)
        self.y = random.randint(0,HEIGHT)
        self.startX = self.x
        self.startY = self.y

        self.speed = 5

        self.size = random.randint(0,100)/100
        self.moveAmount = 100

    def update(self):
        self.x += ((self.x - (WIDTH / 2)) / self.moveAmount) * self.speed
        self.y += ((self.y - (HEIGHT / 2)) / self.moveAmount) * self.speed
        self.startX += ((self.x - (WIDTH / 2)) / self.moveAmount) * self.speed / 2
        self.startY += ((self.y - (HEIGHT / 2)) / self.moveAmount) * self.speed / 2

        self.size += max(abs(((self.x - (WIDTH / 2)) / self.moveAmount) * self.speed / 50),abs(((self.y - (WIDTH / 2)) / self.moveAmount) * self.speed / 50))

        if self.startX < 0 or self.startX > WIDTH or self.startY < 0 or self.startY > HEIGHT:
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(0, HEIGHT)
            self.startX = self.x
            self.startY = self.y
            self.size = random.randint(0,100)/100

    def getSpeed(self):
        mos = pygame.mouse.get_pos()
        self.speed = mos[0] / 50
        # self.speed = (mos[0] - WIDTH / 2) / 100
        pass
    def drawLines(self):
        pygame.draw.line(screen,"#f1f2f6",(self.startX,self.startY),(self.x,self.y))

    def draw(self):
        self.getSpeed()
        self.drawLines()
        pygame.draw.circle(screen,"#f1f2f6",(self.x,self.y),self.size)


stars = []

for i in range(STARAMOUNT):
    stars.append(Star())