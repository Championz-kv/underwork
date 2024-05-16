import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Time Table Generator')
screen = pygame.display.set_mode((1200, 600),0,32)

#setting font settings
font = pygame.font.SysFont('leelawadeeui', 15)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
# A variable to check for the status later
click = False
 
# Main container function that holds the buttons and game functions
def main_menu():
    while True:
 
        screen.fill((15,15,15))
        draw_text('Generate - A - Time - Table', pygame.font.SysFont('utsaah', 70), (250,250,250), screen, 60, 30) # HEAD TEXT
        mx, my = pygame.mouse.get_pos()
        #creating buttons
        button_gen = pygame.Rect(890, 30, 170, 40)
        button_1 = pygame.Rect(80, 150, 160, 30)
        button_2 = pygame.Rect(80, 200, 160, 30)
        button_3 = pygame.Rect(80, 250, 160, 30)
        button_4 = pygame.Rect(80, 300, 160, 30)
        button_5 = pygame.Rect(80, 350, 160, 30)
        button_6 = pygame.Rect(80, 400, 160, 30)
        button_7 = pygame.Rect(80, 450, 160, 30)
        button_8 = pygame.Rect(80, 500, 160, 30)
        
        pygame.draw.rect(screen, (150, 50, 50), button_1)  #draws the button
        pygame.draw.rect(screen, (150, 50, 50), button_2)
        pygame.draw.rect(screen, (150, 50, 50), button_3)
        pygame.draw.rect(screen, (150, 50, 50), button_4)
        pygame.draw.rect(screen, (150, 50, 50), button_5)
        pygame.draw.rect(screen, (150, 50, 50), button_6)
        pygame.draw.rect(screen, (150, 50, 50), button_7)
        pygame.draw.rect(screen, (150, 50, 50), button_8)
        pygame.draw.rect(screen, (50, 50, 150), button_gen)
 
        #writing text on top of button
        draw_text('Group-1 CUSTOMIZE', font, (255,255,255), screen, 90, 153)
        draw_text('Group-2 CUSTOMIZE', font, (255,255,255), screen, 90, 203)
        draw_text('Group-3 CUSTOMIZE', font, (255,255,255), screen, 90, 253)
        draw_text('Group-4 CUSTOMIZE', font, (255,255,255), screen, 90, 303)
        draw_text('Group-5 CUSTOMIZE', font, (255,255,255), screen, 90, 353)
        draw_text('Group-6 CUSTOMIZE', font, (255,255,255), screen, 90, 403)
        draw_text('Group-7 CUSTOMIZE', font, (255,255,255), screen, 90, 453)
        draw_text('Group-8 CUSTOMIZE', font, (255,255,255), screen, 90, 503)
        draw_text('GENERATE', pygame.font.SysFont('aparajita', 30), (255,255,255), screen, 913, 37)
        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                grp = 1
                game(grp) 
        if button_2.collidepoint((mx, my)):
            if click:
                grp = 2
                game(grp) 
        if button_3.collidepoint((mx, my)):
            if click:
                grp = 3
                game(grp)  
        if button_4.collidepoint((mx, my)):
            if click:
                grp = 4
                game(grp) 
        if button_5.collidepoint((mx, my)):
            if click:
                grp = 5
                game(grp) 
        if button_6.collidepoint((mx, my)):
            if click:
                grp = 6
                game(grp) 
        if button_7.collidepoint((mx, my)):
            if click:
                grp = 7
                game(grp) 
        if button_8.collidepoint((mx, my)):
            if click:
                grp = 8
                game(grp) 
        if button_gen.collidepoint((mx, my)):
            if click:
                generate()
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game(grp): ##################button1
    running = True
    while running:
        screen.fill((0,0,0))
       
        draw_text(f'GAME SCREEN {grp}', font, (255, 255, 255), screen, 20, 20) # txt

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)

def generate(): ##############button2
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('OUTPUT SCREEN IS THIS (INCOMPLETE)', font, (255, 255, 255), screen, 20, 20) #txt

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()