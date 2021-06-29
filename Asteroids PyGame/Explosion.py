from gameSettings import *

class Explosion(object):
    def __init__(self, x, y, w, h, size):
        self.images = [pygame.image.load('images/explosion/explosion0' + str(i) + '.png') for i in range(10)]
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (int(self.images[i].get_width() * (size/2)), int(self.images[i].get_height() * (size/2))))
        self.imgcur = 0
        frames = range(len(self.images))
        n = size + 1
        self.animation = [item for item in frames for i in range(n)]
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.angle = random.randint(0, 360)
        self.rotatedSurf = pygame.transform.rotate(self.images[self.imgcur], self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x + self.w//2, self.y + self.h//2)
        self.isDone = False

    def animate(self):
        if self.imgcur >= len(self.animation) - 1:
            self.isDone = True
            return
        self.imgcur = self.imgcur + 1
        self.rotatedSurf = pygame.transform.rotate(self.images[self.animation[self.imgcur]], self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x + self.w//2, self.y + self.h//2)

    def draw(self, win):
        self.animate()
        win.blit(self.rotatedSurf, self.rotatedRect)


