import pygame, sys, openpyxl  
mainClock = pygame.time.Clock()
from pygame.locals import *  
pygame.init()
pygame.display.set_caption('Time Table Generator') #top caption
screen = pygame.display.set_mode((1250, 620),pygame.RESIZABLE)
try: # opening data excel sheet
    wb = openpyxl.load_workbook("tt_data.xlsx") 
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
finaldata = [['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['','']]
#function that inputs the values entered in boxes and put to respective places
def inputval(self):
    global finaldata, period_boxes, input_boxes
    #data = [self.text] #final data
    #finaldata.append(data)
    if self in input_boxes:
        finaldata[input_boxes.index(self)][0] = self.text #subject name
    elif self in period_boxes:
        finaldata[period_boxes.index(self)][1] = self.text # no. of periods per week
#function that saves the value to the excel file
def savefile():
    global finaldata
    wb.active = grp # changes excel sheet according to class grp
    for i in finaldata:
        if i != ['','']: # do not leave empty rows in excel sheet
            #wb.active.append(i)
            m_row = wb.active.max_row
            for n in range(1,m_row+1):
                if i[0] == wb.active.cell(row=n,column=1).value : # checks if a subject is repeated,updates its values
                    if i[1] != '':
                        edit_period = wb.active.cell(row=n,column=2)
                        edit_period.value = i[1]
                    break
            else:
                wb.active.append(i)

    wb.save("tt_data.xlsx") #saves the file
    finaldata = [['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['',''],['','']]

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

    def update(self,wid):
        # Resize the box if the text is too long.
        width = max(wid, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
def classinput(grp):
    clock = pygame.time.Clock()
    global input_boxes , period_boxes
    input_box1 = InputBox(100, 75, 140, 30)
    input_box2 = InputBox(100, 120, 140, 30)
    input_box3 = InputBox(100, 165, 140, 30)
    input_box4 = InputBox(100, 210, 140, 30)
    input_box5 = InputBox(100, 255, 140, 30)
    input_box6 = InputBox(100, 300, 140, 30)
    input_box7 = InputBox(100, 345, 140, 30)
    input_box8 = InputBox(100, 390, 140, 30)
    input_box9 = InputBox(100, 435, 140, 30)
    input_box10 = InputBox(100, 480, 140, 30)
    input_box11 = InputBox(100, 525, 140, 30)
    input_box12 = InputBox(100, 570, 140, 30)
    input_boxes = [input_box1, input_box2,input_box3, input_box4,input_box5, input_box6,input_box7, input_box8,input_box9, input_box10,input_box11, input_box12]
    period_box1 = InputBox(320, 75, 140, 30)
    period_box2 = InputBox(320, 120, 140, 30)
    period_box3 = InputBox(320, 165, 140, 30)
    period_box4 = InputBox(320, 210, 140, 30)
    period_box5 = InputBox(320, 255, 140, 30)
    period_box6 = InputBox(320, 300, 140, 30)
    period_box7 = InputBox(320, 345, 140, 30)
    period_box8 = InputBox(320, 390, 140, 30)
    period_box9 = InputBox(320, 435, 140, 30)
    period_box10 = InputBox(320, 480, 140, 30)
    period_box11 = InputBox(320, 525, 140, 30)
    period_box12 = InputBox(320, 570, 140, 30)
    period_boxes = [period_box1, period_box2,period_box3, period_box4,period_box5, period_box6,period_box7, period_box8,period_box9, period_box10,period_box11, period_box12]
    
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for box in input_boxes:
                box.handle_event(event)
            for period in period_boxes:
                period.handle_event(event)
            if event.type == KEYDOWN:  #quit game with esc
                if event.key == K_ESCAPE: 
                    done = True
                if event.key == pygame.K_END:
                    savefile()
                    done = True
        screen.fill((30, 30, 30)) 
        draw_text(f'You are editing group {grp}', pygame.font.SysFont('utsaah', 40), (100,250,250), screen, 930, 30)
        draw_text('Edit the details', pygame.font.SysFont('utsaah', 30), (250,250,200), screen, 1005, 70)
        draw_text('according to the given', pygame.font.SysFont('utsaah', 30), (250,250,200), screen, 960, 95)
        draw_text('specifications.', pygame.font.SysFont('utsaah', 30), (250,250,200), screen, 1003, 120)
        for box in input_boxes:
            box.update(200)
        for box in input_boxes:
            box.draw(screen)
        for period in period_boxes:
            period.update(40)
        for period in period_boxes:
            period.draw(screen)

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