import pygame, sys, openpyxl  
mainClock = pygame.time.Clock()
from pygame.locals import *  
pygame.init()
pygame.display.set_caption('Time Table Generator') #top caption
screen = pygame.display.set_mode((1250, 620),0,32)
try: # opening data excel sheet
    wb = openpyxl.load_workbook("ttdata.xlsx") 
except:
    wb = openpyxl.Workbook()
    sheet1 = wb.create_sheet(title="1")
    sheet2 = wb.create_sheet(title="2")
    sheet3 = wb.create_sheet(title="3")
    sheet4 = wb.create_sheet(title="4")
    sheet5 = wb.create_sheet(title="5")
    sheet6 = wb.create_sheet(title="6")
    sheet7 = wb.create_sheet(title="7")
    sheet8 = wb.create_sheet(title="8")
sheet = wb.active 
#defining sheets



#setting font settings
font = pygame.font.SysFont('leelawadeeui', 15) # customize wala font
COLOR_INACTIVE = pygame.Color('lightskyblue3') #classgrp button colours
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 28)
def draw_text(text, font, color, surface, x, y): #font on the input box text
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
# A variable to check for the status later
click = False
global grp
global finaldata
#function that inputs the values entered in the tt_data file
def inputval(self):
    global finaldata
    finaldata = [self.text] #final data
    savefile()###check
def savefile():
    global finaldata
    wb.active = grp # changes excel sheet according to class grp
    wb.active.append(finaldata) #appends data into the sheet
    wb.save("ttdata.xlsx") #saves the file

# Main container function that holds the buttons and game functions
def main_menu():
    global grp
    while True:
        screen.fill((15,15,15)) #screen colour
        draw_text('Generate A Time Table', pygame.font.SysFont('utsaah', 70), (250,250,250), screen, 60, 30) # HEAD TEXT
        mx, my = pygame.mouse.get_pos()
        #creating buttons
        button_gen = pygame.Rect(890, 30, 170, 40) #main menu buttons initialize
        button_1 = pygame.Rect(80, 150, 160, 30)
        button_2 = pygame.Rect(80, 200, 160, 30)
        button_3 = pygame.Rect(80, 250, 160, 30)
        button_4 = pygame.Rect(80, 300, 160, 30)
        button_5 = pygame.Rect(80, 350, 160, 30)
        button_6 = pygame.Rect(80, 400, 160, 30)
        button_7 = pygame.Rect(80, 450, 160, 30)
        button_8 = pygame.Rect(80, 500, 160, 30)
        
        pygame.draw.rect(screen, (150, 50, 50), button_1)  #draws the buttons
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
                classinput(grp) 
        if button_2.collidepoint((mx, my)):
            if click:
                grp = 2
                classinput(grp) 
        if button_3.collidepoint((mx, my)):
            if click:
                grp = 3
                classinput(grp)  
        if button_4.collidepoint((mx, my)):
            if click:
                grp = 4
                classinput(grp) 
        if button_5.collidepoint((mx, my)):
            if click:
                grp = 5
                classinput(grp) 
        if button_6.collidepoint((mx, my)):
            if click:
                grp = 6
                classinput(grp) 
        if button_7.collidepoint((mx, my)):
            if click:
                grp = 7
                classinput(grp) 
        if button_8.collidepoint((mx, my)):
            if click:
                grp = 8
                classinput(grp) 
        if button_gen.collidepoint((mx, my)):
            if click:
                generate()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:  #quit game ofc
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  #quit game with esc
                if event.key == K_ESCAPE: 
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN: #pata nahi kya tha...bhool gya
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.checkable = True

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                if self.checkable == True :
                    self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    inputval(self)
                    self.checkable = False
                    self.active = False
                    #self.text = '' ###CHECK
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
def classinput(grp):
    clock = pygame.time.Clock()
    input_box1 = InputBox(100, 45, 140, 30)
    input_box2 = InputBox(100, 90, 140, 30)
    input_box3 = InputBox(100, 135, 140, 30)
    input_box4 = InputBox(100, 180, 140, 30)
    input_box5 = InputBox(100, 225, 140, 30)
    input_box6 = InputBox(100, 270, 140, 30)
    input_box7 = InputBox(100, 315, 140, 30)
    input_box8 = InputBox(100, 360, 140, 30)
    input_box9 = InputBox(100, 405, 140, 30)
    input_box10 = InputBox(100, 450, 140, 30)
    input_box11 = InputBox(100, 495, 140, 30)
    input_box12 = InputBox(100, 540, 140, 30)
    input_boxes = [input_box1, input_box2,input_box3, input_box4,input_box5, input_box6,input_box7, input_box8,input_box9, input_box10,input_box11, input_box12]
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
            if event.type == KEYDOWN:  #quit game with esc
                if event.key == K_ESCAPE: 
                    done = True
                    
        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(30)
    
def generate(): #generate
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