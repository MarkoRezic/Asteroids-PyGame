from gameSettings import *

class Flame(object):
    def __init__(self, player):
        self.images = [pygame.image.load('images/player/flame/flame' + str(i+1) + '.png') for i in range(5)]
        self.imgcur = 0
        self.animation = [0,0,0,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,3,3,2,2,2,3,3,4,4,4,3,3,3,2,2,2,2,1,1,1,1,0,0]
        self.player = player
        self.point = player.thrust
        self.x, self.y = self.point
        # self.w = 4
        # self.h = 4
        self.w = self.images[self.imgcur].get_width()
        self.h = self.images[self.imgcur].get_height()
        self.angle = player.angle
        self.rotatedSurf = pygame.transform.rotate(self.images[self.imgcur], self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.c = player.cosine
        self.s = player.sine

    def animate(self):
        self.imgcur = (self.imgcur + 1) % len(self.animation)
        self.angle = self.player.angle
        self.rotatedSurf = pygame.transform.rotate(self.images[self.animation[self.imgcur]], self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)

    def move(self):
        self.x, self.y = self.player.thrust

    def draw(self, win):
        # pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])
        self.animate()
        win.blit(self.rotatedSurf, self.rotatedRect)

class Player(object):
    def __init__(self):
        self.img = pygame.image.load('images/player/spaceRocket.png')
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw//2
        self.y = sh//2
        self.angle = 0
        self.momentum = 0
        self.momentumLoss = 1.03
        self.isMoving = False
        self.thrustConst = 1
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)
        self.thrust = (self.x - (self.cosine * self.w//2)*self.thrustConst, self.y + (self.sine * self.h//2)*self.thrustConst)
        self.flame = Flame(self)

    def draw(self, win):
        #win.blit(self.img, [self.x, self.y, self.w, self.h])
        if not self.isMoving: self.momentumMove()
        self.thrust = (self.x - (self.cosine * self.w//2)*self.thrustConst, self.y + (self.sine * self.h//2)*self.thrustConst)
        self.flame.move()
        self.flame.draw(win)
        win.blit(self.rotatedSurf, self.rotatedRect)
        self.isMoving = False
        self.thrustConst = 1

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)
        self.thrust = (self.x - (self.cosine * self.w//2)*self.thrustConst, self.y + (self.sine * self.h//2)*self.thrustConst)

    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)
        self.thrust = (self.x - (self.cosine * self.w//2)*self.thrustConst, self.y + (self.sine * self.h//2)*self.thrustConst)

    def moveForward(self):
        self.isMoving = True;
        self.thrustConst = 1.2
        self.momentum = 3
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)
        self.thrust = (self.x - (self.cosine * self.w//2)*self.thrustConst, self.y + (self.sine * self.h//2)*self.thrustConst)

    def momentumMove(self):
        self.x += self.cosine * self.momentum
        self.y -= self.sine * self.momentum
        self.momentum /= self.momentumLoss
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)
        self.thrust = (self.x - (self.cosine * self.w//2)*self.thrustConst, self.y + (self.sine * self.h//2)*self.thrustConst)

    def updateLocation(self):
        if self.x > sw + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = sw
        elif self.y < -50:
            self.y = sh
        elif self.y > sh + 50:
            self.y = 0

    def resetLocation(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2)
        self.thrust = (self.x - (self.cosine * self.w//2)*self.thrustConst, self.y + (self.sine * self.h//2)*self.thrustConst)


