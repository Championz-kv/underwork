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
global grpno_1,grpno_2,grpno_3,grpno_4,grpno_5,grpno_6,grpno_7,grpno_8
grpno_1 =grpno_2 =grpno_3 =grpno_4 =grpno_5 =grpno_6 =grpno_7 =grpno_8 = 0
finaldata = [['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','','']]
#function that inputs the values entered in boxes and put to respective places
def inputval(self):
    global finaldata, period_boxes, input_boxes, maxpd_boxes
    #data = [self.text] #final data
    #finaldata.append(data)
    if self in input_boxes:
        finaldata[input_boxes.index(self)][0] = self.text #subject name
    elif self in period_boxes:
        finaldata[period_boxes.index(self)][1] = self.text # no. of periods per week
    elif self in maxpd_boxes:
        finaldata[maxpd_boxes.index(self)][2] = self.text # no. of max-periods per day 
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
                    if i[2] != '':
                        edit_maxpd = wb.active.cell(row=n,column=3)
                        edit_maxpd.value = i[2]
                    break
            else:
                wb.active.append(i)
    i=1
    while i < wb.active.max_row:
        if wb.active.cell(row=i,column=1).value == None or wb.active.cell(row=i,column=1).value == '':
            wb.active.delete_rows(idx=i)
        else:
            i+=1
    wb.save("tt_data.xlsx") #saves the file
    finaldata = [['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','','']]
# Main container function that holds the buttons and game functions
def main_menu():
    global grpno_1,grpno_2,grpno_3,grpno_4,grpno_5,grpno_6,grpno_7,grpno_8, grp
    while True:
        screen.fill((15,15,15)) #screen colour
        draw_text('Generate A Time Table', pygame.font.SysFont('utsaah', 70), (250,250,250), screen, 60, 30) # HEAD TEXT
        mx, my = pygame.mouse.get_pos()
        #creating buttons
        button_gen = pygame.Rect(890, 30, 170, 40) #main menu buttons initialize
        button_teacher = pygame.Rect(890, 80, 170, 40)
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
        pygame.draw.rect(screen, (50, 50, 150), button_teacher)

        button_1no = pygame.Rect(280, 150, 50, 30)
        button_2no = pygame.Rect(280, 200, 50, 30)
        button_3no = pygame.Rect(280, 250, 50, 30)
        button_4no = pygame.Rect(280, 300, 50, 30)
        button_5no = pygame.Rect(280, 350, 50, 30)
        button_6no = pygame.Rect(280, 400, 50, 30)
        button_7no = pygame.Rect(280, 450, 50, 30)
        button_8no = pygame.Rect(280, 500, 50, 30)    
        pygame.draw.rect(screen, (50, 150, 50), button_1no)  #draws the buttons
        pygame.draw.rect(screen, (50, 150, 50), button_2no)
        pygame.draw.rect(screen, (50, 150, 50), button_3no)
        pygame.draw.rect(screen, (50, 150, 50), button_4no)
        pygame.draw.rect(screen, (50, 150, 50), button_5no)
        pygame.draw.rect(screen, (50, 150, 50), button_6no)
        pygame.draw.rect(screen, (50, 150, 50), button_7no)
        pygame.draw.rect(screen, (50, 150, 50), button_8no)
        #writing text on top of button
        draw_text('Group-1 CUSTOMIZE', font, (255,255,255), screen, 90, 153)
        draw_text('Group-2 CUSTOMIZE', font, (255,255,255), screen, 90, 203)
        draw_text('Group-3 CUSTOMIZE', font, (255,255,255), screen, 90, 253)
        draw_text('Group-4 CUSTOMIZE', font, (255,255,255), screen, 90, 303)
        draw_text('Group-5 CUSTOMIZE', font, (255,255,255), screen, 90, 353)
        draw_text('Group-6 CUSTOMIZE', font, (255,255,255), screen, 90, 403)
        draw_text('Group-7 CUSTOMIZE', font, (255,255,255), screen, 90, 453)
        draw_text('Group-8 CUSTOMIZE', font, (255,255,255), screen, 90, 503)
        draw_text(str(grpno_1), font, (255,255,255), screen, 290, 153)
        draw_text(str(grpno_2), font, (255,255,255), screen, 290, 203)
        draw_text(str(grpno_3), font, (255,255,255), screen, 290, 253)
        draw_text(str(grpno_4), font, (255,255,255), screen, 290, 303)
        draw_text(str(grpno_5), font, (255,255,255), screen, 290, 353)
        draw_text(str(grpno_6), font, (255,255,255), screen, 290, 403)
        draw_text(str(grpno_7), font, (255,255,255), screen, 290, 453)
        draw_text(str(grpno_8), font, (255,255,255), screen, 290, 503)
        draw_text('GENERATE', pygame.font.SysFont('aparajita', 30), (255,255,255), screen, 913, 37)
        draw_text('No. of Teachers', pygame.font.SysFont('aparajita', 30), (255,255,255), screen, 900, 87)
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
        if button_teacher.collidepoint((mx, my)):
            if click:
                grp = 0
                classinput(grp)
        if button_1no.collidepoint((mx, my)):
            if click:
                grpno_1 += 1
                if grpno_1 ==9:
                    grpno_1 = 0
        if button_2no.collidepoint((mx, my)):
            if click:
                grpno_2 += 1
                if grpno_2 ==9:
                    grpno_2 = 0
        if button_3no.collidepoint((mx, my)):
            if click:
                grpno_3 += 1
                if grpno_3 ==9:
                    grpno_3 = 0
        if button_4no.collidepoint((mx, my)):
            if click:
                grpno_4 += 1
                if grpno_4 ==9:
                    grpno_4 = 0
        if button_5no.collidepoint((mx, my)):
            if click:
                grpno_5 += 1
                if grpno_5 ==9:
                    grpno_5 = 0
        if button_6no.collidepoint((mx, my)):
            if click:
                grpno_6 += 1
                if grpno_6 ==9:
                    grpno_6 = 0
        if button_7no.collidepoint((mx, my)):
            if click:
                grpno_7 += 1
                if grpno_7 ==9:
                    grpno_7 = 0
        if button_8no.collidepoint((mx, my)):
            if click:
                grpno_8 += 1
                if grpno_8 ==9:
                    grpno_8 = 0
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
    global input_boxes , period_boxes, maxpd_boxes
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
    maxpd_box1 = InputBox(380, 75, 140, 30)
    maxpd_box2 = InputBox(380, 120, 140, 30)
    maxpd_box3 = InputBox(380, 165, 140, 30)
    maxpd_box4 = InputBox(380, 210, 140, 30)
    maxpd_box5 = InputBox(380, 255, 140, 30)
    maxpd_box6 = InputBox(380, 300, 140, 30)
    maxpd_box7 = InputBox(380, 345, 140, 30)
    maxpd_box8 = InputBox(380, 390, 140, 30)
    maxpd_box9 = InputBox(380, 435, 140, 30)
    maxpd_box10 = InputBox(380, 480, 140, 30)
    maxpd_box11 = InputBox(380, 525, 140, 30)
    maxpd_box12 = InputBox(380, 570, 140, 30)
    maxpd_boxes = [maxpd_box1, maxpd_box2,maxpd_box3, maxpd_box4,maxpd_box5, maxpd_box6,maxpd_box7, maxpd_box8,maxpd_box9, maxpd_box10,maxpd_box11, maxpd_box12]
    done = False


    button_done = pygame.Rect(80, 500, 160, 30)    
    pygame.draw.rect(screen, (150, 50, 50), button_done)


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for box in input_boxes:
                box.handle_event(event)
            for period in period_boxes:
                period.handle_event(event)
            if grp != 0:
                for maxpd in maxpd_boxes:
                    maxpd.handle_event(event)
            if event.type == KEYDOWN:  #quit game with esc
                if event.key == K_ESCAPE: 
                    done = True
                if event.key == pygame.K_END:
                    savefile()
                    done = True
        screen.fill((30, 30, 30)) 
        if grp != 0:
            draw_text(f'You are editing group {grp}', pygame.font.SysFont('utsaah', 40), (100,250,250), screen, 930, 20)
            draw_text('Edit the details', pygame.font.SysFont('utsaah', 30), (250,250,200), screen, 1005, 70)
            draw_text('according to the given', pygame.font.SysFont('utsaah', 30), (250,250,200), screen, 960, 95)
            draw_text('specifications.', pygame.font.SysFont('utsaah', 30), (250,250,200), screen, 1003, 120)
            draw_text('Click on the box,', pygame.font.SysFont('utsaah', 30), (250,210,210), screen, 997, 160)
            draw_text('type, and press enter.', pygame.font.SysFont('utsaah', 30), (250,210,210), screen, 972, 185)
            draw_text('press end when you', pygame.font.SysFont('utsaah', 30), (250,210,210), screen, 975, 210)
            draw_text('have completed filling', pygame.font.SysFont('utsaah', 30), (250,210,210), screen, 965, 235)
            draw_text('the boxes', pygame.font.SysFont('utsaah', 30), (250,210,210), screen, 1025, 260)
            draw_text('To cancel and exit,', pygame.font.SysFont('utsaah', 30), (200,200,250), screen, 985, 300)
            draw_text('press esc', pygame.font.SysFont('utsaah', 30), (200,200,250), screen, 1027, 325)
            draw_text('To edit, just rewrite', pygame.font.SysFont('utsaah', 30), (250,250,250), screen, 983, 365)
            draw_text('the subject and the', pygame.font.SysFont('utsaah', 30), (250,250,250), screen, 986, 390)
            draw_text('new specifications', pygame.font.SysFont('utsaah', 30), (250,250,250), screen, 988, 415)
        for box in input_boxes:
            box.update(200)
        for box in input_boxes:
            box.draw(screen)
        for period in period_boxes:
            period.update(40)
        for period in period_boxes:
            period.draw(screen)
        if grp != 0:
            for maxpd in maxpd_boxes:
                maxpd.update(40)
            for maxpd in maxpd_boxes:
                maxpd.draw(screen)
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
def teacher(): #generate
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('TEACHER SCREEN', font, (255, 255, 255), screen, 20, 20) #txt
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN: 
                if event.key == K_ESCAPE: 
                    running = False     
        pygame.display.update()
        mainClock.tick(60) 
def make_tt():
    a=1
main_menu()