#imports
import pygame
import random
import math
from pygame import mixer


#Iniatialize the pygame
pygame.init()

#Create the screen
screen=pygame.display.set_mode((900 , 600))

#Backgroud
background=pygame.image.load('1876.jpg')

#Background sound
mixer.music.load('easy.mp3')
mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#Player
PlayerImg=pygame.image.load('spaceship.png')
playerX=290
playerY=500
playerX_change=0

#Enemy
enemyImg= []
enemyX= []
enemyY = []
enemyX_change=[]
enemyY_change=[]
num_of_enemies = 6

for i in range (num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint (50 , 830))
    enemyY.append(random.randint (50,200))
    enemyX_change.append(0.5)
    enemyY_change.append(40)

#Bullet
#1. Ready state - You cant see the bullet on the screen
#2. Fire - The bullet is currently moving
bulletImg=pygame.transform.scale(pygame.image.load('bullet.png') , (24,24))
bulletX=0
bulletY=500
bulletX_change=0
bulletY_change=3
bullet_state= 'ready'

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf' , 32)
textX= 20
textY=30

#Game Over
over_text_font = pygame.font.Font('freesansbold.ttf' , 64)
gameoverX=290
gameoverY=300

def game_over_text(x , y):
    g_over = over_text_font.render('GAME OVER' , True , (255 , 255 , 255))
    screen.blit(g_over , (x , y))
    

def show_score(x ,y):
    score=font.render('Score : ' + str(score_value) , True , (255 , 255 , 255))
    screen.blit(score , (x,y))

def player(x , y):
    screen.blit(PlayerImg , (x,y))

def enemy(x , y , i):
    screen.blit(enemyImg[i] , (x,y))

def fire_bullet(x , y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg , (x + 19 , y + 10))

def isCollision(enemyX , enemyY , bulletX , bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX , 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
counter = 0
# Game loop      
running= True
while running:
         
     #RGB - Red , Green , Blue
     screen.fill((0 , 0 , 0))
     # image background
     screen.blit(background , (0,0))
     
     playerX+=0
    
     for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False 

#if keystroke is pressed , lets check if it rightarrow or left 
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.9
            if event.key==pygame.K_RIGHT:
                playerX_change=0.9
            if event.key==pygame.K_SPACE:
                if bullet_state is 'ready':
                    # bullet_sound=mixer.Sound('')
                    # bullet_sound.play()
                    # Get the current x cordinate of the spaceship.
                    bulletX = playerX
                    fire_bullet(bulletX ,bulletY)

        if event.type==pygame.KEYUP:
          if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0

    #5 = 5 + -0.1 is 5 - 0.1
    #5 = 5 + 0.1

   
     playerX += playerX_change 
     if playerX <= 9:
            playerX=9
     elif playerX >= 830:
            playerX=830

    #  enemyX += enemyX_change
     
     for i in range (num_of_enemies):
         #Game over
         if enemyY[i] >= 500:
             for j in range (num_of_enemies):
                 enemyY[j] = 2000
             game_over_text(gameoverX , gameoverY)
             break
         enemyX[i] += enemyX_change[i]
         if enemyX[i] <= 20:
              enemyX_change[i] = 0.7
              enemyY[i]+=enemyY_change[i]
           
         elif enemyX[i] >= 830:
              enemyX_change[i] = -0.7
              enemyY[i]+=enemyY_change[i]
       

    
         collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
         if collision:
            #  explotion_sound=mixer.Sound('')
            #  explotion_sound.play()
             bulletY = 500
             bulletX_state='ready'
             score_value += 1 
             enemyX[i]=random.randint (50 , 830)
             enemyY[i]=random.randint (50, 200)        
     
         enemy(enemyX[i] , enemyY[i] , i) 

     if  bulletY <= 0:
         bulletY = 500
         bullet_state ='ready'

       # Bullet state      
     if bullet_state is 'fire':
         fire_bullet(bulletX , bulletY)
         bulletY -= bulletY_change  
    #  enemy(enemyX[i] , enemyY[i] , i)
     show_score(textX , textY) 
     player(playerX , playerY)
     pygame.display.update()






