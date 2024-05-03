import turtle
import random
turtle.screensize(2500,1400) # scrollable screen
wn = turtle.Screen()
wn.bgcolor("gray10")
A0 = turtle.Turtle() # All the positions to be used in game
A1 = turtle.Turtle()
A2 = turtle.Turtle()
A3 = turtle.Turtle()
A4 = turtle.Turtle()
A5 = turtle.Turtle()
A6 = turtle.Turtle()
A7 = turtle.Turtle()
A8 = turtle.Turtle()
A9 = turtle.Turtle()
B0 = turtle.Turtle()
B1 = turtle.Turtle()
B2 = turtle.Turtle()
B3 = turtle.Turtle()
B4 = turtle.Turtle()
B5 = turtle.Turtle()
B6 = turtle.Turtle()
B7 = turtle.Turtle()
B8 = turtle.Turtle()
B9 = turtle.Turtle()
C0 = turtle.Turtle()
C1 = turtle.Turtle()
C2 = turtle.Turtle()
C3 = turtle.Turtle()
C4 = turtle.Turtle()
C5 = turtle.Turtle()
C6 = turtle.Turtle()
C7 = turtle.Turtle()
C8 = turtle.Turtle()
C9 = turtle.Turtle()
D0 = turtle.Turtle()
D1 = turtle.Turtle()
D2 = turtle.Turtle()
D3 = turtle.Turtle()
D4 = turtle.Turtle()
D5 = turtle.Turtle()
D6 = turtle.Turtle()
D7 = turtle.Turtle()
D8 = turtle.Turtle()
D9 = turtle.Turtle()
E0 = turtle.Turtle()
E1 = turtle.Turtle()
E2 = turtle.Turtle()
E3 = turtle.Turtle()
E4 = turtle.Turtle()
E5 = turtle.Turtle()
E6 = turtle.Turtle()
E7 = turtle.Turtle()
E8 = turtle.Turtle()
E9 = turtle.Turtle()
F0 = turtle.Turtle()
F1 = turtle.Turtle()
F2 = turtle.Turtle()
F3 = turtle.Turtle()
F4 = turtle.Turtle()
F5 = turtle.Turtle()
F6 = turtle.Turtle()
F7 = turtle.Turtle()
F8 = turtle.Turtle()
F9 = turtle.Turtle()
allpoints = [A0,A1,A2,A3,A4,A5,A6,A7,A8,A9,B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,C0,C1,C2,C3,C4,C5,C6,C7,C8,C9,D0,D1,D2,D3,D4,D5,D6,D7,D8,D9,E0,E1,E2,E3,E4,E5,E6,E7,E8,E9,F0,F1,F2,F3,F4,F5,F6,F7,F8,F9]
allpointclr = []
colours = ['firebrick1','PaleGreen','RoyalBlue1','plum1']
coloursdecoded = ['red','green','blue','pink']
for i in allpoints:   # makes the points circular & fast
    i.penup()
    i.speed(2000)
    i.shape('circle')
    i.shapesize(0.7)
def waypoint() : #makes the waypoint looks
    global allpoints,a,allpointclr
    for x in allpoints:
        x.width(3)
        a = random.choice(colours)
        x.color(a)
        allpointclr.append(a)
        x.pendown()
        x.begin_fill()
        x.left(65)
        x.fd(35)
        x.circle(15,extent=226)
        x.fd(35)
        x.end_fill
        x.penup()
        x.setheading(90)
        x.fd(40)
#put all points to positions
A0.goto(984,-113) #1
A1.goto(820,-100) #2
A2.goto(602,-100) #3
A3.goto(390,-106) #4
A4.goto(194,-101) #5
A5.goto(6,-113) #6
A6.goto(-212,-78) #7
A7.goto(-400,-110) #8
A8.goto(-579,-67) #9
A9.goto(-800,-100) #10
B0.goto(1011,-250) #11
B1.goto(810,-240) #12
B2.goto(600,-250)#13
B3.goto(419,-216)#14
B4.goto(180,-229)#15
B5.goto(1,-266)#16
B6.goto(-200,-250)#17
B7.goto(-400,-250)#18
B8.goto(-600,-250)#19
B9.goto(-840,-248)#20
C0.goto(817,-340)#21
C1.goto(680,-350)#22
C2.goto(570,-419)#23
C3.goto(411,-377)#24
C4.goto(230,-359)#25
C5.goto(-99,-400)#26
C6.goto(-240,-429)#27
C7.goto(-553,-495)#28
C8.goto(-656,-409)#29
C9.goto(-720,-333)#30
D0.goto(819,400)#31
D1.goto(756,36)#32
D2.goto(600,424)#33
D3.goto(480,399)#34
D4.goto(211,417)#35
D5.goto(-66,450)#36
D6.goto(-176,483)#37
D7.goto(-344,457)#38
D8.goto(-580,450)#39
D9.goto(-800,444)#40
E0.goto(912,330)#41
E1.goto(756,290)#42
E2.goto(600,287)#43
E3.goto(530,303)#44
E4.goto(200,300)#45
E5.goto(11,290)#46
E6.goto(-235,279)#47
E7.goto(-450,311)#48
E8.goto(-550,335)#49
E9.goto(-840,309)#50
F0.goto(1000,100)#51
F1.goto(800,100)#52
F2.goto(600,100)#53
F3.goto(400,100)#54
F4.goto(200,100)#55
F5.goto(0,100)#56
F6.goto(-200,100)#57
F7.goto(-400,100)#58
F8.goto(-600,100)#59
F9.goto(-800,100)#60
waypoint()
## ON CLICK CHANGE COLOUR FOR IDEAS FUNCTIONS
A0clr = 1 
def colorchangeA0(x,y):
    global A0clr,allpointclr
    if A0clr == 0:
        A0.color(allpointclr[0])
        print(allpointclr[0])
        A0clr = 1
    elif A0clr == 1:
        A0.color("yellow")
        A0clr = 2
    else:
        A0.color("white")
        A0clr = 0
A0.onclick(colorchangeA0) #A0
A1clr = 1
def colorchangeA1(x,y):
    global A1clr,allpointclr
    if A1clr == 0:
        A1.color(allpointclr[1])
        A1clr = 1
    elif A1clr == 1:
        A1.color("yellow")
        A1clr = 2
    else:
        A1.color("white")
        A1clr = 0
A1.onclick(colorchangeA1)#A1
A2clr = 1
def colorchangeA2(x,y):
    global A2clr,allpointclr
    if A2clr == 0:
        A2.color(allpointclr[2])
        A2clr = 1
    elif A2clr == 1:
        A2.color("yellow")
        A2clr = 2
    else:
        A2.color("white")
        A2clr = 0
A2.onclick(colorchangeA2)#A2
A3clr = 1
def colorchangeA3(x,y):
    global A3clr,allpointclr
    if A3clr == 0:
        A3.color(allpointclr[3])
        A3clr = 1
    elif A3clr == 1:
        A3.color("yellow")
        A3clr = 2
    else:
        A3.color("white")
        A3clr = 0
A3.onclick(colorchangeA3)#A3
A4clr = 1
def colorchangeA4(x,y):
    global A4clr,allpointclr
    if A4clr == 0:
        A4.color(allpointclr[4])
        A4clr = 1
    elif A4clr == 1:
        A4.color("yellow")
        A4clr = 2
    else:
        A4.color("white")
        A4clr = 0
A4.onclick(colorchangeA4)#A4
A5clr = 1
def colorchangeA5(x,y):
    global A5clr,allpointclr
    if A5clr == 0:
        A5.color(allpointclr[5])
        A5clr = 1
    elif A5clr == 1:
        A5.color("yellow")
        A5clr = 2
    else:
        A5.color("white")
        A5clr = 0
A5.onclick(colorchangeA5)#A5
A6clr = 1
def colorchangeA6(x,y):
    global A6clr,allpointclr
    if A6clr == 0:
        A6.color(allpointclr[6])
        A6clr = 1
    elif A6clr == 1:
        A6.color("yellow")
        A6clr = 2
    else:
        A6.color("white")
        A6clr = 0
A6.onclick(colorchangeA6)#A6
A7clr = 1
def colorchangeA7(x,y):
    global A7clr,allpointclr
    if A7clr == 0:
        A7.color(allpointclr[7])
        A7clr = 1
    elif A7clr == 1:
        A7.color("yellow")
        A7clr = 2
    else:
        A7.color("white")
        A7clr = 0
A7.onclick(colorchangeA7)#A7
A8clr = 1
def colorchangeA8(x,y):
    global A8clr,allpointclr
    if A8clr == 0:
        A8.color(allpointclr[8])
        A8clr = 1
    elif A8clr == 1:
        A8.color("yellow")
        A8clr = 2
    else:
        A8.color("white")
        A8clr = 0
A8.onclick(colorchangeA8)#A8
A9clr = 1
def colorchangeA9(x,y):
    global A9clr,allpointclr
    if A9clr == 0:
        A9.color(allpointclr[9])
        A9clr = 1
    elif A9clr == 1:
        A9.color("yellow")
        A9clr = 2
    else:
        A9.color("white")
        A9clr = 0
A9.onclick(colorchangeA9)#A9
B0clr = 1
def colorchangeB0(x,y):
    global B0clr,allpointclr
    if B0clr == 0:
        B0.color(allpointclr[10])
        B0clr = 1
    elif B0clr == 1:
        B0.color("yellow")
        B0clr = 2
    else:
        B0.color("white")
        B0clr = 0
B0.onclick(colorchangeB0)#B0
B1clr = 1
def colorchangeB1(x,y):
    global B1clr,allpointclr
    if B1clr == 0:
        B1.color(allpointclr[11])
        B1clr = 1
    elif B1clr == 1:
        B1.color("yellow")
        B1clr = 2
    else:
        B1.color("white")
        B1clr = 0
B1.onclick(colorchangeB1)#B1
B2clr = 1
def colorchangeB2(x,y):
    global B2clr,allpointclr
    if B2clr == 0:
        B2.color(allpointclr[12])
        B2clr = 1
    elif B2clr == 1:
        B2.color("yellow")
        B2clr = 2
    else:
        B2.color("white")
        B2clr = 0
B2.onclick(colorchangeB2)#B2
B3clr = 1
def colorchangeB3(x,y):
    global B3clr,allpointclr
    if B3clr == 0:
        B3.color(allpointclr[13])
        B3clr = 1
    elif B3clr == 1:
        B3.color("yellow")
        B3clr = 2
    else:
        B3.color("white")
        B3clr = 0
B3.onclick(colorchangeB3)#B3
B4clr = 1
def colorchangeB4(x,y):
    global B4clr,allpointclr
    if B4clr == 0:
        B4.color(allpointclr[14])
        B4clr = 1
    elif B4clr == 1:
        B4.color("yellow")
        B4clr = 2
    else:
        B4.color("white")
        B4clr = 0
B4.onclick(colorchangeB4) #B4
B5clr = 1
def colorchangeB5(x,y):
    global B5clr,allpointclr
    if B5clr == 0:
        B5.color(allpointclr[15])
        B5clr = 1
    elif B5clr == 1:
        B5.color("yellow")
        B5clr = 2
    else:
        B5.color("white")
        B5clr = 0
B5.onclick(colorchangeB5) #B5
B6clr = 1
def colorchangeB6(x,y):
    global B6clr,allpointclr
    if B6clr == 0:
        B6.color(allpointclr[16])
        B6clr = 1
    elif B6clr == 1:
        B6.color("yellow")
        B6clr = 2
    else:
        B6.color("white")
        B6clr = 0
B6.onclick(colorchangeB6) #B6
B7clr = 1
def colorchangeB7(x,y):
    global B7clr,allpointclr
    if B7clr == 0:
        B7.color(allpointclr[17])
        B7clr = 1
    elif B7clr == 1:
        B7.color("yellow")
        B7clr = 2
    else:
        B7.color("white")
        B7clr = 0
B7.onclick(colorchangeB7) #B7
B8clr = 1
def colorchangeB8(x,y):
    global B8clr,allpointclr
    if B8clr == 0:
        B8.color(allpointclr[18])
        B8clr = 1
    elif B8clr == 1:
        B8.color("yellow")
        B8clr = 2
    else:
        B8.color("white")
        B8clr = 0
B8.onclick(colorchangeB8) #B8
B9clr = 1
def colorchangeB9(x,y):
    global B9clr,allpointclr
    if B9clr == 0:
        B9.color(allpointclr[19])
        B9clr = 1
    elif B9clr == 1:
        B9.color("yellow")
        B9clr = 2
    else:
        B9.color("white")
        B9clr = 0
B9.onclick(colorchangeB9) #B9
C0clr = 1
def colorchangeC0(x,y):
    global C0clr,allpointclr
    if C0clr == 0:
        C0.color(allpointclr[20])
        C0clr = 1
    elif C0clr == 1:
        C0.color("yellow")
        C0clr = 2
    else:
        C0.color("white")
        C0clr = 0
C0.onclick(colorchangeC0) #C0
C1clr = 1
def colorchangeC1(x,y):
    global C1clr,allpointclr
    if C1clr == 0:
        C1.color(allpointclr[21])
        C1clr = 1
    elif C1clr == 1:
        C1.color("yellow")
        C1clr = 2
    else:
        C1.color("white")
        C1clr = 0
C1.onclick(colorchangeC1) #C1
C2clr = 1
def colorchangeC2(x,y):
    global C2clr,allpointclr
    if C2clr == 0:
        C2.color(allpointclr[22])
        C2clr = 1
    elif C2clr == 1:
        C2.color("yellow")
        C2clr = 2
    else:
        C2.color("white")
        C2clr = 0
C2.onclick(colorchangeC2) #C2
C3clr = 1
def colorchangeC3(x,y):
    global C3clr,allpointclr
    if C3clr == 0:
        C3.color(allpointclr[23])
        C3clr = 1
    elif C3clr == 1:
        C3.color("yellow")
        C3clr = 2
    else:
        C3.color("white")
        C3clr = 0
C3.onclick(colorchangeC3) #C3
C4clr = 1
def colorchangeC4(x,y):
    global C4clr,allpointclr
    if C4clr == 0:
        C4.color(allpointclr[24])
        C4clr = 1
    elif C4clr == 1:
        C4.color("yellow")
        C4clr = 2
    else:
        C4.color("white")
        C4clr = 0
C4.onclick(colorchangeC4) #C4
C5clr = 1
def colorchangeC5(x,y):
    global C5clr,allpointclr
    if C5clr == 0:
        C5.color(allpointclr[25])
        C5clr = 1
    elif C5clr == 1:
        C5.color("yellow")
        C5clr = 2
    else:
        C5.color("white")
        C5clr = 0
C5.onclick(colorchangeC5) #C5
C6clr = 1
def colorchangeC6(x,y):
    global C6clr,allpointclr
    if C6clr == 0:
        C6.color(allpointclr[26])
        C6clr = 1
    elif C6clr == 1:
        C6.color("yellow")
        C6clr = 2
    else:
        C6.color("white")
        C6clr = 0
C6.onclick(colorchangeC6) #C6
C7clr = 1
def colorchangeC7(x,y):
    global C7clr,allpointclr
    if C7clr == 0:
        C7.color(allpointclr[27])
        C7clr = 1
    elif C7clr == 1:
        C7.color("yellow")
        C7clr = 2
    else:
        C7.color("white")
        C7clr = 0
C7.onclick(colorchangeC7) #C7
C8clr = 1
def colorchangeC8(x,y):
    global C8clr,allpointclr
    if C8clr == 0:
        C8.color(allpointclr[28])
        C8clr = 1
    elif C8clr == 1:
        C8.color("yellow")
        C8clr = 2
    else:
        C8.color("white")
        C8clr = 0
C8.onclick(colorchangeC8) #C8
C9clr = 1
def colorchangeC9(x,y):
    global C9clr,allpointclr
    if C9clr == 0:
        C9.color(allpointclr[29])
        C9clr = 1
    elif C9clr == 1:
        C9.color("yellow")
        C9clr = 2
    else:
        C9.color("white")
        C9clr = 0
C9.onclick(colorchangeC9) #C9
D0clr = 1 
def colorchangeD0(x,y):
    global D0clr,allpointclr
    if D0clr == 0:
        D0.color(allpointclr[30])
        D0clr = 1
    elif D0clr == 1:
        D0.color("yellow")
        D0clr = 2
    else:
        D0.color("white")
        D0clr = 0
D0.onclick(colorchangeD0) #D0
D1clr = 1
def colorchangeD1(x,y):
    global D1clr,allpointclr
    if D1clr == 0:
        D1.color(allpointclr[31])
        D1clr = 1
    elif D1clr == 1:
        D1.color("yellow")
        D1clr = 2
    else:
        D1.color("white")
        D1clr = 0
D1.onclick(colorchangeD1)#D1
D2clr = 1
def colorchangeD2(x,y):
    global D2clr,allpointclr
    if D2clr == 0:
        D2.color(allpointclr[32])
        D2clr = 1
    elif D2clr == 1:
        D2.color("yellow")
        D2clr = 2
    else:
        D2.color("white")
        D2clr = 0
D2.onclick(colorchangeD2)#D2
D3clr = 1
def colorchangeD3(x,y):
    global D3clr,allpointclr
    if D3clr == 0:
        D3.color(allpointclr[33])
        D3clr = 1
    elif D3clr == 1:
        D3.color("yellow")
        D3clr = 2
    else:
        D3.color("white")
        D3clr = 0
D3.onclick(colorchangeD3)#D3
D4clr = 1
def colorchangeD4(x,y):
    global D4clr,allpointclr
    if D4clr == 0:
        D4.color(allpointclr[34])
        D4clr = 1
    elif D4clr == 1:
        D4.color("yellow")
        D4clr = 2
    else:
        D4.color("white")
        D4clr = 0
D4.onclick(colorchangeD4)#D4
D5clr = 1
def colorchangeD5(x,y):
    global D5clr,allpointclr
    if D5clr == 0:
        D5.color(allpointclr[35])
        D5clr = 1
    elif D5clr == 1:
        D5.color("yellow")
        D5clr = 2
    else:
        D5.color("white")
        D5clr = 0
D5.onclick(colorchangeD5)#D5
D6clr = 1
def colorchangeD6(x,y):
    global D6clr,allpointclr
    if D6clr == 0:
        D6.color(allpointclr[36])
        D6clr = 1
    elif D6clr == 1:
        D6.color("yellow")
        D6clr = 2
    else:
        D6.color("white")
        D6clr = 0
D6.onclick(colorchangeD6)#D6
D7clr = 1
def colorchangeD7(x,y):
    global D7clr,allpointclr
    if D7clr == 0:
        D7.color(allpointclr[37])
        D7clr = 1
    elif D7clr == 1:
        D7.color("yellow")
        D7clr = 2
    else:
        D7.color("white")
        D7clr = 0
D7.onclick(colorchangeD7)#D7
D8clr = 1
def colorchangeD8(x,y):
    global D8clr,allpointclr
    if D8clr == 0:
        D8.color(allpointclr[38])
        D8clr = 1
    elif D8clr == 1:
        D8.color("yellow")
        D8clr = 2
    else:
        D8.color("white")
        D8clr = 0
D8.onclick(colorchangeD8)#D8
D9clr = 1
def colorchangeD9(x,y):
    global D9clr,allpointclr
    if D9clr == 0:
        D9.color(allpointclr[39])
        D9clr = 1
    elif D9clr == 1:
        D9.color("yellow")
        D9clr = 2
    else:
        D9.color("white")
        D9clr = 0
D9.onclick(colorchangeD9)#D9
E0clr = 1
def colorchangeE0(x,y):
    global E0clr,allpointclr
    if E0clr == 0:
        E0.color(allpointclr[40])
        E0clr = 1
    elif E0clr == 1:
        E0.color("yellow")
        E0clr = 2
    else:
        E0.color("white")
        E0clr = 0
E0.onclick(colorchangeE0)#E0
E1clr = 1
def colorchangeE1(x,y):
    global E1clr,allpointclr
    if E1clr == 0:
        E1.color(allpointclr[41])
        E1clr = 1
    elif E1clr == 1:
        E1.color("yellow")
        E1clr = 2
    else:
        E1.color("white")
        E1clr = 0
E1.onclick(colorchangeE1)#E1
E2clr = 1
def colorchangeE2(x,y):
    global E2clr,allpointclr
    if E2clr == 0:
        E2.color(allpointclr[42])
        E2clr = 1
    elif E2clr == 1:
        E2.color("yellow")
        E2clr = 2
    else:
        E2.color("white")
        E2clr = 0
E2.onclick(colorchangeE2)#E2
E3clr = 1
def colorchangeE3(x,y):
    global E3clr,allpointclr
    if E3clr == 0:
        E3.color(allpointclr[43])
        E3clr = 1
    elif E3clr == 1:
        E3.color("yellow")
        E3clr = 2
    else:
        E3.color("white")
        E3clr = 0
E3.onclick(colorchangeE3)#E3
E4clr = 1
def colorchangeE4(x,y):
    global E4clr,allpointclr
    if E4clr == 0:
        E4.color(allpointclr[44])
        E4clr = 1
    elif E4clr == 1:
        E4.color("yellow")
        E4clr = 2
    else:
        E4.color("white")
        E4clr = 0
E4.onclick(colorchangeE4) #E4
E5clr = 1
def colorchangeE5(x,y):
    global E5clr,allpointclr
    if E5clr == 0:
        E5.color(allpointclr[45])
        E5clr = 1
    elif E5clr == 1:
        E5.color("yellow")
        E5clr = 2
    else:
        E5.color("white")
        E5clr = 0
E5.onclick(colorchangeE5) #E5
E6clr = 1
def colorchangeE6(x,y):
    global E6clr,allpointclr
    if E6clr == 0:
        E6.color(allpointclr[46])
        E6clr = 1
    elif E6clr == 1:
        E6.color("yellow")
        E6clr = 2
    else:
        E6.color("white")
        E6clr = 0
E6.onclick(colorchangeE6) #E6
E7clr = 1
def colorchangeE7(x,y):
    global E7clr,allpointclr
    if E7clr == 0:
        E7.color(allpointclr[47])
        E7clr = 1
    elif E7clr == 1:
        E7.color("yellow")
        E7clr = 2
    else:
        E7.color("white")
        E7clr = 0
E7.onclick(colorchangeE7) #E7
E8clr = 1
def colorchangeE8(x,y):
    global E8clr,allpointclr
    if E8clr == 0:
        E8.color(allpointclr[48])
        E8clr = 1
    elif E8clr == 1:
        E8.color("yellow")
        E8clr = 2
    else:
        E8.color("white")
        E8clr = 0
E8.onclick(colorchangeE8) #E8
E9clr = 1
def colorchangeE9(x,y):
    global E9clr,allpointclr
    if E9clr == 0:
        E9.color(allpointclr[49])
        E9clr = 1
    elif E9clr == 1:
        E9.color("yellow")
        E9clr = 2
    else:
        E9.color("white")
        E9clr = 0
E9.onclick(colorchangeE9) #E9
F0clr = 1
def colorchangeF0(x,y):
    global F0clr,allpointclr
    if F0clr == 0:
        F0.color(allpointclr[50])
        F0clr = 1
    elif F0clr == 1:
        F0.color("yellow")
        F0clr = 2
    else:
        F0.color("white")
        F0clr = 0
F0.onclick(colorchangeF0) #F0
F1clr = 1
def colorchangeF1(x,y):
    global F1clr,allpointclr
    if F1clr == 0:
        F1.color(allpointclr[51])
        F1clr = 1
    elif F1clr == 1:
        F1.color("yellow")
        F1clr = 2
    else:
        F1.color("white")
        F1clr = 0
F1.onclick(colorchangeF1) #F1
F2clr = 1
def colorchangeF2(x,y):
    global F2clr,allpointclr
    if F2clr == 0:
        F2.color(allpointclr[52])
        F2clr = 1
    elif F2clr == 1:
        F2.color("yellow")
        F2clr = 2
    else:
        F2.color("white")
        F2clr = 0
F2.onclick(colorchangeF2) #F2
F3clr = 1
def colorchangeF3(x,y):
    global F3clr,allpointclr
    if F3clr == 0:
        F3.color(allpointclr[53])
        F3clr = 1
    elif F3clr == 1:
        F3.color("yellow")
        F3clr = 2
    else:
        F3.color("white")
        F3clr = 0
F3.onclick(colorchangeF3) #F3
F4clr = 1
def colorchangeF4(x,y):
    global F4clr,allpointclr
    if F4clr == 0:
        F4.color(allpointclr[54])
        F4clr = 1
    elif F4clr == 1:
        F4.color("yellow")
        F4clr = 2
    else:
        F4.color("white")
        F4clr = 0
F4.onclick(colorchangeF4) #F4
F5clr = 1
def colorchangeF5(x,y):
    global F5clr,allpointclr
    if F5clr == 0:
        F5.color(allpointclr[55])
        F5clr = 1
    elif F5clr == 1:
        F5.color("yellow")
        F5clr = 2
    else:
        F5.color("white")
        F5clr = 0
F5.onclick(colorchangeF5) #F5
F6clr = 1
def colorchangeF6(x,y):
    global F6clr,allpointclr
    if F6clr == 0:
        F6.color(allpointclr[56])
        F6clr = 1
    elif F6clr == 1:
        F6.color("yellow")
        F6clr = 2
    else:
        F6.color("white")
        F6clr = 0
F6.onclick(colorchangeF6) #F6
F7clr = 1
def colorchangeF7(x,y):
    global F7clr,allpointclr
    if F7clr == 0:
        F7.color(allpointclr[57])
        F7clr = 1
    elif F7clr == 1:
        F7.color("yellow")
        F7clr = 2
    else:
        F7.color("white")
        F7clr = 0
F7.onclick(colorchangeF7) #F7
F8clr = 1
def colorchangeF8(x,y):
    global F8clr,allpointclr
    if F8clr == 0:
        F8.color(allpointclr[58])
        F8clr = 1
    elif F8clr == 1:
        F8.color("yellow")
        F8clr = 2
    else:
        F8.color("white")
        F8clr = 0
F8.onclick(colorchangeF8) #F8
F9clr = 1
def colorchangeF9(x,y):
    global F9clr,allpointclr
    if F9clr == 0:
        F9.color(allpointclr[59])
        F9clr = 1
    elif F9clr == 1:
        F9.color("yellow")
        F9clr = 2
    else:
        F9.color("white")
        F9clr = 0
F9.onclick(colorchangeF9) #F9


wn.listen()
turtle.done()