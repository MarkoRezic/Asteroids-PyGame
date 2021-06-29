from gameSettings import *

class Star(object):

    def __init__(self):
        self.img = pygame.image.load('images/star.png')
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < sw//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < sh//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2

    def move(self):
        self.x += self.xv
        self.y += self.yv

    def checkOffScreen(self):
        return self.x > sw + 100 or self.x + self.w < -100 or self.y > sh + 100 or self.y + self.h < -100

    def checkCollision(self, x, y, w, h):
        return ((self.x >= x and self.x <= x + w) or (self.x + self.w >= x and self.x + self.w <= x + w)) and ((self.y >= y and self.y <= y + h) or (self.y + self.h >= y and self.y + self.h <= y + h))

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


