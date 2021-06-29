from gameSettings import *

class Bullet(object):
    def __init__(self, player):
        self.images = [pygame.image.load('images/laser' + str(i+1) + '.png') for i in range(3)]
        self.imgcur = 0
        self.animation = [0,0,0,1,1,1,2,2,2,2,2,1,1,1,0,0]
        self.point = player.head
        self.x, self.y = self.point
        # self.w = 4
        # self.h = 4
        self.w = self.images[self.imgcur].get_width()
        self.h = self.images[self.imgcur].get_height()
        self.angle = player.angle
        self.rotatedSurf = pygame.transform.rotate(self.images[self.imgcur], self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x + self.w//2, self.y + self.h//2)
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    def animate(self):
        self.imgcur = (self.imgcur + 1) % len(self.animation)
        self.rotatedSurf = pygame.transform.rotate(self.images[self.animation[self.imgcur]], self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x + self.w//2, self.y + self.h//2)

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def checkOffScreen(self):
        if self.x < -50 or self.x > sw or self.y > sh or self.y < -50:
            return True

    def checkCollision(self, x, y, w, h):
        return ((self.x >= x and self.x <= x + w) or (self.x + self.w >= x and self.x + self.w <= x + w)) and ((self.y >= y and self.y <= y + h) or (self.y + self.h >= y and self.y + self.h <= y + h))

    def draw(self, win):
        # pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])
        self.animate()
        win.blit(self.rotatedSurf, self.rotatedRect)


