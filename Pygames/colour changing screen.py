import pygame
pygame.init()
#starting pygame at the start of the program

width = 300
height = 300
size = width, height
screen = pygame.display.set_mode(size)
#creates the graphics window
screenRect = screen.get_rect()
#makes it easier to control things on the screen
pygame.display.set_caption("Click to change colour")
#The title

#defining colours
red = [255, 0, 0]
orange = [252, 140, 3]
yellow = [252, 236, 3]
black = [0, 0, 0]
white = [255, 255, 255]
blue = [0, 0, 255]
green = [0, 255, 0]
raspberry = [135, 38, 87]
#storing the colours
colours = [red, orange, yellow, black, white, blue, green, raspberry]
cLen = len(colours)
#we will need this length later on

c = done = flag = 0
#creating a counter,
#then creating a 'done' falg and another flag to
    #check that the mouse has been released

#main loop
while not done:
    screen.fill(colours[c])
    #set up exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #set up mouse click feature
    if event.type == pygame.MOUSEBUTTONDOWN and not flag:
        flag = True
        c = (c + 1) % cLen
    #the flag colour changing many times per one click
    if event.type == pygame.MOUSEBUTTONUP:
        flag = False
    #update the display
    pygame.display.flip()
#close pygame
pygame.quit()

while not done:
    screen.fill(colours[c])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True