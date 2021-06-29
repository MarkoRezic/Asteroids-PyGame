from gameSettings import *
from Player import Player
from Bullet import Bullet
from Asteroid import Asteroid
from Explosion import Explosion
from Star import Star
from SuperNova import SuperNova
from Alien import Alien
from AlienBullet import AlienBullet


def drawBackground():
    global bgx
    global bgy
    global bgvx
    global bgvy
    if bgx > 0: win.blit(bg, (bgx - sw, bgy))
    if bgy > 0: win.blit(bg, (bgx, bgy - sh))
    if bgx > 0 and bgy > 0: win.blit(bg, (bgx - sw, bgy - sh))
    win.blit(bg, (bgx, bgy))
    bgx = (bgx + bgvx) % sw
    bgy = (bgy + bgvy) % sh


def redrawGameWindow():

    # postavi pozadinu, font, broj života, rezultat itd.

    drawBackground()
    font = pygame.font.SysFont('arial',30)
    livesText = font.render('Lives: ' + str(lives), 1, (255, 255, 255))
    playAgainText = font.render('Press Tab to Play Again', 1, (255,255,255))
    scoreText = font.render('Score: ' + str(score), 1, (255,255,255))
    highScoreText = font.render('High Score: ' + str(highScore), 1, (255, 255, 255))

    # crtanje objekata
    
    player.draw(win)
    for a in asteroids:
        a.draw(win)
    for b in playerBullets:
        b.draw(win)
    for s in stars:
        s.draw(win)
    for a in aliens:
        a.draw(win)
    for b in alienBullets:
        b.draw(win)
    for e in explosions:
        e.draw(win)
    for s in supernovas:
        s.draw(win)

    # prikaži preostalo vrijeme za rapidFire

    if rapidFire:
        pygame.draw.rect(win, (255, 255, 255), [sw//2 - 54, 16, 108, 28])
        pygame.draw.rect(win, (0, 0, 0), [sw//2 - 52, 18, 104, 24])
        pygame.draw.rect(win, (100, 180, 255), [sw//2 - 50, 20, 100 - 100*(count - rfStart)/500, 20])

    # prikaži ekran za kraj igre

    if gameover:
        win.blit(playAgainText, (sw//2-playAgainText.get_width()//2, sh//2 - playAgainText.get_height()//2))

    # prikaži rezultat, živote i najveći rezultat

    win.blit(scoreText, (sw- scoreText.get_width() - 25, 25))
    win.blit(livesText, (25, 25))
    win.blit(highScoreText, (sw - highScoreText.get_width() -25, 35 + scoreText.get_height()))
    pygame.display.update()


# inicijalizacija objekata

player = Player()
playerBullets = []
asteroids = []
explosions = []
count = 0
stars = []
supernovas = []
aliens = []
alienBullets = []

pygame.mixer.music.play(-1, 0.0)

loadingCounter = 0

while loadingCounter < 1500:
    fontTitle = pygame.font.SysFont('arialblack',60)
    font = pygame.font.SysFont('arial',25)
    titleText = fontTitle.render('Asteroids', 1, (255, 255, 255))
    loadingDots = ((loadingCounter % 400) // 100) * '.'
    loadingText = font.render('Loading' + loadingDots, 1, (255, 255, 255))
    loadingPercent = font.render(str(round(100 * (loadingCounter/1500))) + '%', 1, (255, 255, 255))
    pygame.draw.rect(win, (0, 0, 0), [0, 0, sw, sh])
    win.blit(titleText, (sw//2 - 150, 200))
    win.blit(loadingText, (sw//2 - 45, sh//2 - 36))
    win.blit(loadingPercent, (sw//2 + 90, sh//2 - 2))
    pygame.draw.rect(win, (255, 255, 255), [sw//2 - 54, sh//2 - 4, 128, 28])
    pygame.draw.rect(win, (0, 0, 0), [sw//2 - 52, sh//2 - 2, 124, 24])
    pygame.draw.rect(win, (30, 230, 70), [sw//2 - 50, sh//2, 120*(loadingCounter/1500), 20])
    pygame.display.update()
    loadingCounter += 1
        
run = True

while run:

    # 60 FPS

    clock.tick(60)
    count += 1

    if not gameover:
        # stvori asteroid svaki sekund (60 frame-ova)
        if count % 60 == 0:
            # izaberi nasumičnu veličinu od 1-3
            ran = random.choice([1,1,1,2,2,3])
            asteroids.append(Asteroid(ran))
        # stvori zvijezdu svakih 25 sekundi
        if count % 1500 == 0:
            stars.append(Star())
        # stvori vanzemaljca svakih 12 sekundi
        if count % 720 == 0:
            aliens.append(Alien())
        for i, a in enumerate(aliens):
            a.move()
            if a.checkOffScreen():
                aliens.pop(i)
            if count % 80 == 0:
                alienBullets.append(AlienBullet(a.x + a.w//2, a.y + a.h//2, player))
                if isSoundOn:
                    enemyShoot.play()

            for b in playerBullets:
                if b.checkCollision(a.x, a.y, a.w, a.h):
                    explosions.append(Explosion(a.x, a.y, a.w, a.h, 4))
                    aliens.pop(i)
                    playerBullets.pop(playerBullets.index(b))
                    if isSoundOn:
                        bangLargeSound.play()
                    score += 50
                    break

        for i, b in enumerate(alienBullets):
            b.move()
            if b.checkCollision(player.x - player.w//2, player.y-player.h//2, player.w, player.h):
                lives -= 1
                explosions.append(Explosion(b.x, b.y, b.w, b.h, 1))
                if isSoundOn:
                    bangLargeSound.play()
                alienBullets.pop(i)
                break

        player.updateLocation()
        for b in playerBullets:
            b.move()
            if b.checkOffScreen():
                playerBullets.pop(playerBullets.index(b))


        for a in asteroids:
            a.move()

            if a.checkCollision(player.x - player.w//2, player.y-player.h//2, player.w, player.h):
                lives -= 1
                explosions.append(Explosion(a.x, a.y, a.w, a.h, a.rank))
                asteroids.pop(asteroids.index(a))
                if isSoundOn:
                    bangLargeSound.play()
                break

            # bullet collision
            for b in playerBullets:
                if b.checkCollision(a.x, a.y, a.w, a.h):
                    if a.rank == 3:
                        if isSoundOn:
                            bangLargeSound.play()
                        score += 10
                        na1 = Asteroid(2)
                        na2 = Asteroid(2)
                        na1.x = a.x
                        na2.x = a.x
                        na1.y = a.y
                        na2.y = a.y
                        asteroids.append(na1)
                        asteroids.append(na2)
                    elif a.rank == 2:
                        if isSoundOn:
                            bangSmallSound.play()
                        score += 20
                        na1 = Asteroid(1)
                        na2 = Asteroid(1)
                        na1.x = a.x
                        na2.x = a.x
                        na1.y = a.y
                        na2.y = a.y
                        asteroids.append(na1)
                        asteroids.append(na2)
                    else:
                        score += 30
                        if isSoundOn:
                            bangSmallSound.play()
                    explosions.append(Explosion(a.x, a.y, a.w, a.h, a.rank))
                    asteroids.pop(asteroids.index(a))
                    playerBullets.pop(playerBullets.index(b))
                    break

        for s in stars:
            s.move()
            if s.checkOffScreen():
                stars.pop(stars.index(s))
                break
            if s.checkCollision(player.x - player.w//2, player.y-player.h//2, player.w, player.h):
                lives += 1
                rapidFire = True
                rfStart = count
                supernovas.append(SuperNova(player.x, player.y))
                if isSoundOn:
                    supernova.play()
                stars.pop(stars.index(s))
            for b in playerBullets:
                if b.checkCollision(s.x, s.y, s.w, s.h):
                    lives += 1
                    rapidFire = True
                    rfStart = count
                    stars.pop(stars.index(s))
                    supernovas.append(SuperNova(b.x, b.y))
                    if isSoundOn:
                        supernova.play()
                    playerBullets.pop(playerBullets.index(b))
                    break

        for e in explosions:
            if e.isDone:
                explosions.pop(explosions.index(e))
        for s in supernovas:
            if s.isDone:
                supernovas.pop(supernovas.index(s))
            for a in asteroids:
                if s.checkCollision(a.x + a.w//2, a.y + a.h//2):
                    if a.rank == 3:
                        if isSoundOn:
                            bangLargeSound.play()
                        score += 10
                        na1 = Asteroid(2)
                        na2 = Asteroid(2)
                        na1.x = a.x
                        na2.x = a.x
                        na1.y = a.y
                        na2.y = a.y
                        asteroids.append(na1)
                        asteroids.append(na2)
                    elif a.rank == 2:
                        if isSoundOn:
                            bangSmallSound.play()
                        score += 20
                        na1 = Asteroid(1)
                        na2 = Asteroid(1)
                        na1.x = a.x
                        na2.x = a.x
                        na1.y = a.y
                        na2.y = a.y
                        asteroids.append(na1)
                        asteroids.append(na2)
                    else:
                        score += 30
                        if isSoundOn:
                            bangSmallSound.play()
                    explosions.append(Explosion(a.x, a.y, a.w, a.h, a.rank))
                    asteroids.pop(asteroids.index(a))
            for i, a in enumerate(aliens):
                if s.checkCollision(a.x + a.w//2, a.y + a.h//2):
                    explosions.append(Explosion(a.x, a.y, a.w, a.h, 4))
                    aliens.pop(i)
                    if isSoundOn:
                        bangLargeSound.play()
                    score += 50

            for i, b in enumerate(alienBullets):
                if s.checkCollision(b.x + b.w//2, b.y + b.h//2):
                    explosions.append(Explosion(b.x, b.y, b.w, b.h, 1))
                    alienBullets.pop(i)


        if lives <= 0:
            gameover = True

        if rfStart != -1:
            if count - rfStart > 500:
                rapidFire = False
                rfStart = -1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.turnLeft()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.turnRight()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.moveForward()
        else:
            player.momentumMove()
        if keys[pygame.K_SPACE]:
            if rapidFire and count % 2 == 0:
                playerBullets.append(Bullet(player))
                if isSoundOn:
                    shoot.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not gameover:
                    if not rapidFire:
                        playerBullets.append(Bullet(player))
                        if isSoundOn:
                            shoot.play()
            if event.key == pygame.K_m:
                isSoundOn = not isSoundOn
                if isSoundOn: pygame.mixer.music.unpause()
                else: pygame.mixer.music.pause()
            if event.key == pygame.K_TAB:
                if gameover:
                    gameover = False
                    lives = 3
                    playerBullets.clear()
                    asteroids.clear()
                    aliens.clear()
                    alienBullets.clear()
                    stars.clear()
                    if score > highScore:
                        highScore = score
                    score = 0
                    player.resetLocation(sw/2, sh/2)

    redrawGameWindow()


pygame.quit()
