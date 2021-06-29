from gameSettings import *

class Alien(object):
    def __init__(self):
        self.images = [pygame.image.load('images/enemy/alienShip' + str(i+1) + '.png') for i in range(4)]
        self.imgcur = 0
        frames = range(len(self.images))
        n = 7
        self.animation = [item for item in frames for i in range(n)] + [item for item in frames[::-1] for i in range(n)]
        self.w = self.images[self.imgcur].get_width()
        self.h = self.images[self.imgcur].get_height()
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

    def animate(self):
        self.imgcur = (self.imgcur + 1) % len(self.animation)

    def checkOffScreen(self):
        return self.x > sw + 100 or self.x + self.w < -100 or self.y > sh + 100 or self.y + self.h < -100

    def draw(self, win):
        self.animate()
        win.blit(self.images[self.animation[self.imgcur]], (self.x, self.y))


