import pygame
import math
import random

pygame.init()

global sw
global sh
global bg
global bgx
global bgy
global bgvx
global bgvy

global masterVolume
global musicVolume
global sfxVolume
global shoot
global enemyShoot
global bangLargeSound
global bangSmallSound
global supernova

global win
global clock

global gameover
global lives
global score
global rapidFire
global rfStart
global isSoundOn
global highScore

sw = 800
sh = 800
bg = pygame.image.load('images/starbg.png')
bgx = 0
bgy = 0
bgvx = 1
bgvy = 0.5

masterVolume = 0.25
musicVolume = 0.8
sfxVolume = 1.0
pygame.mixer.init()
pygame.mixer.music.load("sounds/bg_music.mp3")
pygame.mixer.music.set_volume(masterVolume * musicVolume)
shoot = pygame.mixer.Sound('sounds/shoot.wav')
enemyShoot = pygame.mixer.Sound('sounds/enemyShoot.wav')
bangLargeSound = pygame.mixer.Sound('sounds/bangLarge.wav')
bangSmallSound = pygame.mixer.Sound('sounds/bangSmall.wav')
supernova = pygame.mixer.Sound('sounds/supernova.wav')
shoot.set_volume(masterVolume * sfxVolume)
bangLargeSound.set_volume(masterVolume * sfxVolume)
bangSmallSound.set_volume(masterVolume * sfxVolume)
supernova.set_volume(masterVolume * sfxVolume * 2)

pygame.display.set_caption('Asteroids')
win = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()

gameover = False
lives = 3
score = 0
rapidFire = False
rfStart = -1
isSoundOn = True
highScore = 0


