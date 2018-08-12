import pygame
import random

pygame.init()

width=1280
height=720
red=(255,0,0)

screen=pygame.display.set_mode((width,height))

bg_img = pygame .image.load("C:\\Users\\adisethi123\\Desktop\\pygame\\images/background.png")
aim_pointer = pygame.image.load("C:\\Users\\adisethi123\\Desktop\\pygame\\images/aim4.png")
zombie_1 = pygame.image.load("C:\\Users\\adisethi123\\Desktop\\pygame\\images/zombie1.png")
zombie_2 = pygame.image.load("C:\\Users\\adisethi123\\Desktop\\pygame\\images/zombie2.png")
zombie_3 = pygame.image.load("C:\\Users\\adisethi123\\Desktop\\pygame\\images/zombie3.png")
zombie_4 = pygame.image.load("C:\\Users\\adisethi123\\Desktop\\pygame\\images/zombie6.png")


zombielist=[zombie_1,zombie_2,zombie_3,zombie_4]
zombieimage=random.choice(zombielist)

zombie_x = random.randint(0,width-198)
zombie_y = random.randint(0,height-255)


shotsound = pygame.mixer.Sound("C:\\Users\\adisethi123\\Desktop\\pygame\\music/shot_noise.wav")
reloadsound=pygame.mixer.Sound("C:\\Users\\adisethi123\\Desktop\\pygame\\music/reload.wav")
bgmusic=pygame.mixer.Sound("C:\\Users\\adisethi123\\Desktop\\pygame\\music/background.wav")
bgmusic.play()

def score(counter):
    font=pygame.font.SysFont(None,40)
    text=font.render("Score:"+str(counter),True,red)
    screen.blit(text,(10,10))

    
def game():
    
    zombielist=[zombie_1,zombie_2,zombie_3,zombie_4]
    zombieimage=random.choice(zombielist)

    zombie_x = random.randint(0,width-198)
    zombie_y = random.randint(0,height-255)
    shot=4

    counter=0
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                shot=shot-1
                if shot>=0:
                 shotsound.play()
                 if rect_1.colliderect(rect_2):
                        print("collision detected!!!")
                        zombieimage=random.choice(zombielist)
                        zombie_x = random.randint(0,width-198)
                        zombie_y = random.randint(0,height-255)
                        counter=counter+1
              
            if event.type==pygame.KEYDOWN:
                 if event.key == pygame.K_r:
                    shot=4
                    reloadsound.play()

        posx,posy = pygame.mouse.get_pos()

        screen.blit(bg_img,(0,0))
        screen.blit(zombieimage,(zombie_x,zombie_y))
        screen.blit((aim_pointer) , (posx-20,posy-21) )
      

        rect_1=pygame.Rect(posx-20,posy-21,40,43)
        rect_2=pygame.Rect(zombie_x,zombie_y,zombieimage.get_width(),zombieimage.get_height())

        score(counter)
        
        pygame.display.update()
        
game()
