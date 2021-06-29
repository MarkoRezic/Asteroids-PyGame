from gameSettings import *

class SuperNova(object):
    def __init__(self, x, y):
        self.initImage = pygame.image.load('images/explosion/superNova.png')
        self.img = pygame.image.load('images/explosion/superNova.png')
        self.size = 1
        self.growth = 1.07
        self.x, self.y = x, y
        self.w, self.h = 0, 0
        self.isDone = False

    def animate(self):
        if self.size > 6:
            self.isDone = True
            return
        self.size *= self.growth
        self.w = int(self.initImage.get_width() * (self.size - 1))
        self.h = int(self.initImage.get_height() * (self.size - 1))
        self.img = pygame.transform.scale(self.initImage, (self.w, self.h))

    def checkCollision(self, x, y):
        return abs((self.x - self.w // 2) - x) <= (self.w * 0.7) or abs((self.y - self.h // 2) - x) <= (self.h * 0.7)

    def draw(self, win):
        self.animate()
        win.blit(self.img, (self.x - self.w // 2, self.y - self.h // 2))


