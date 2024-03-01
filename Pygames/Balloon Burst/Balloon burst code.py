#Balloon Burst
import pygame
import random
pygame.init()

screen = pygame.display.set_mode([800,400])
#setting the width and height
pygame.display.set_caption("Balloon Burst :)")
#naming the window
background = pygame.image.load("SkyBackground.png").convert()
#importing the background image from files
pygame.mouse.set_visible(False)
done = False
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

################### MAIN PROGRAM ###################
while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #update sprites here:
    yCoord = random.randint(50,350)
    #random y coordinate between these numbers
    balloonType = random.randint(1,4)
    balloon = Balloon(0,yCoord,"Right",balloonType)

    screen.blit(background, [0,0])
    #the blit command is used to draw one surface on top of another
    #it also coordinates the position of one image over another
    pygame.display.flip()
    clock.tick(20)

pygame.quit()


#defining the balloons (sprites):

class Balloon(pygame.sprite.Sprite):
#this class will inherit the attributes of a pygame sprite
   
    def __init__(self, x, y, direction, balloonType):
        pygame.sprite.Sprite.__init__(self)
        #creating different variables: coordinates, direction (left & right) and the balloons

        #class properties:
        self.Direction = direction
        self.BalloonType = balloonType

        #each balloon is assigned a different speed and score
        if balloonType == 1:
            balloonImage = pygame.image.load("RedBalloon.png")
            self.Speed = 3
            self.Score = 5
        if balloonType == 2:
            balloonImage = pygame.image.load("YellowBalloon.png")
            self.Speed = 7
            self.Score = 15
        if balloonType == 3:
            balloonImage = pygame.image.load("GreenBalloon.png")
            self.Speed = 5
            self.Score = 10
        if balloonType == 4:
            balloonImage = pygame.image.load("BlueBalloon.png")
            self.Speed = 10
            self.Score = 0

        self.image = pygame.Surface([26,50])
        #creating a new surface for the balloons
        self.image.set_colorkey(black)
        #making the png parts transparent
        self.image.blit(balloonImage,(0,0))
        #the chosen balloon is copied onto a new surface
        self.rect = self.image.get_rect()
        #to store and manipulate rectangular areas
        self.rect.x = x
        self.rect.y = y
        #positioning the rectangle so it can be used to move the balloon later
