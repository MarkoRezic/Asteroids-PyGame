from gameSettings import *

class AlienBullet(object):
    def __init__(self, x, y, player):
        self.images = [pygame.image.load('images/enemy/laser/enemyLaser' + str(i+1) + '.png') for i in range(5)]
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (int(self.images[i].get_width() * 1.5), int(self.images[i].get_height() * 2.5)))
        self.imgcur = 0
        self.animation = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,4,4,3,3,3,2,2,2,1,1,1,0,0]
        self.x = x
        self.y = y
        # self.w = 4
        # self.h = 4
        self.w = self.images[self.imgcur].get_width()
        self.h = self.images[self.imgcur].get_height()
        self.dx, self.dy = player.x - self.x, player.y - self.y
        self.angle = math.degrees(math.atan2(self.dx, self.dy))
        self.dist = math.hypot(self.dx, self.dy)
        self.dx, self.dy = self.dx / self.dist, self.dy / self.dist
        self.rotatedSurf = pygame.transform.rotate(self.images[self.imgcur], self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x + self.w//2, self.y + self.h//2)
        self.xv = self.dx * 5
        self.yv = self.dy * 5

    def animate(self):
        self.imgcur = (self.imgcur + 1) % len(self.animation)
        self.rotatedSurf = pygame.transform.rotate(self.images[self.animation[self.imgcur]], self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x + self.w//2, self.y + self.h//2)

    def move(self):
        self.x += self.xv
        self.y += self.yv

    def checkCollision(self, x, y, w, h):
        return ((self.x >= x and self.x <= x + w) or (self.x + self.w >= x and self.x + self.w <= x + w)) and ((self.y >= y and self.y <= y + h) or (self.y + self.h >= y and self.y + self.h <= y + h))

    def draw(self, win):
        # pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])
        self.animate()
        win.blit(self.rotatedSurf, self.rotatedRect)


