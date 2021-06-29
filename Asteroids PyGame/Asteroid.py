from gameSettings import *

class Asteroid(object):

    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = pygame.image.load('images/asteroid1.png')
        elif self.rank == 2:
            self.image = pygame.image.load('images/asteroid2.png')
        else:
            self.image = pygame.image.load('images/asteroid3.png')
        self.w = 50 * rank
        self.h = 50 * rank
        self.ranPoint = random.choice([(random.randrange(0, sw-self.w), random.choice([-1*self.h - 5, sh + 5])), (random.choice([-1*self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint
        self.angle = 0
        self.rotation = round(random.uniform(-5, 5), 2)
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x + self.w//2, self.y + self.h//2)
        if self.x < sw//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < sh//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * round(random.uniform(0.4, 4), 2)
        self.yv = self.ydir * round(random.uniform(0.4, 4), 2)

    def move(self):
        self.x += self.xv
        self.y += self.yv
        self.angle -= self.rotation
        if self.angle <= -360: self.angle += 360
        if self.angle >= 360: self.angle -= 360
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x + self.w//2, self.y + self.h//2)

    def checkCollision(self, x, y, w, h):
        return ((self.x >= x and self.x <= x + w) or (self.x + self.w >= x and self.x + self.w <= x + w)) and ((self.y >= y and self.y <= y + h) or (self.y + self.h >= y and self.y + self.h <= y + h))

    def draw(self, win):
        # win.blit(self.image, (self.x, self.y))
        win.blit(self.rotatedSurf, self.rotatedRect)


