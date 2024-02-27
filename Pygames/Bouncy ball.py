import pygame
pygame.init()

width = 500
height = 600
size = width, height
screen = pygame.display.set_mode(size)
screenRect = screen.get_rect()
pygame.display.set_caption("Bounce")

#define some colours
black = [0, 0, 0]
red = [255, 0, 0]

ballSize = 40, 40
#size of ball surface
ballRad = 20
#radius of ball
xSpeed = ySpeed = 1

#ball
ballSurf = pygame.Surface(ballSize)
#the 'ball' is drawn onto this surface
ballRect = ballSurf.get_rect()
#'rect' allows us to know where the center of the object is
center = (ballRect.centerx, ballRect.centery)
ball = pygame.draw.circle(ballSurf, red, center, ballRad)

pygame.mouse.set_visible(False)
#makes the mouse pointerinvisible in graphics window

done = False
#main loop
while not done:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    ballRect = ballRect.move(xSpeed, ySpeed)
    #check if the ball is going off screen
    if ballRect.left < 0 or ballRect.right > width:
        xSpeed = -xSpeed
    if ballRect.top < 0 or ballRect.bottom > height:
        ySpeed = -ySpeed
    #draw the ball & update the display
    screen.blit(ballSurf, ballRect)
    pygame.display.flip()
pygame.quit()