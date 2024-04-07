from cmu_graphics import *
from PIL import Image
import os, pathlib
import copy, string, itertools, random
import random, itertools, string, copy
import tkinter as tk

class Clothes: 
    def __init__(self): 
        self.unidress=CMUImage(Image.open('unidress.png'))
        self.cutedress=CMUImage(Image.open('cutedress.png'))
        self.sexydress=CMUImage(Image.open('sexydress.png'))
        self.elegdress=CMUImage(Image.open('elegdress.png'))
        self.unishirt=CMUImage(Image.open('unique.png'))
        self.cuteshirt=CMUImage(Image.open('IMG_1262.PNG'))
        self.sexyshirt=CMUImage(Image.open('IMG_1263.PNG'))
        self.elegshirt=CMUImage(Image.open('elegshirt.png'))
        self.unishoes=CMUImage(Image.open('IMG_1259.PNG'))
        self.cuteshoes=CMUImage(Image.open('cuteshoes.png'))
        self.sexyshoes=CMUImage(Image.open('sexyshoes.png'))
        self.elegshoes=CMUImage(Image.open('elegshoes.png'))
        self.dress=None
        self.shirt=None
        self.shoes=None

        

clo=Clothes()

def onAppStart(app): 
    app.width=1000
    app.height=800
    app.page1=True
    app.page2=True
    app.page3=True
    app.page4=True
    app.page5=True
    app.page6=True
    app.page7=True
    app.pageCloset = True
    app.page8=True
    app.page9=True
    app.page10=True
    # app.page123=True
    app.pageQuiz=True
    app.backgroundImage1 = Image.open("image/background1.jpeg")
    app.backgroundImage1 = CMUImage(app.backgroundImage1)
    app.backgroundImage2 = Image.open("photo/background3")
    app.backgroundImage2 = CMUImage(app.backgroundImage2)
    app.coffeeBackground3 = Image.open('photo/coffeeBackground')
    app.coffeeBackground3 = CMUImage(app.coffeeBackground3)
    app.backgroundImage4 = Image.open("photo/pizzaBackground")
    app.backgroundImage4 = CMUImage(app.backgroundImage4)
    app.sue = Image.open("photo/10.PNG")
    app.sue = CMUImage(app.sue)
    app.textBox1 = Image.open("photo/texbox1.png")
    app.textBox1 = CMUImage(app.textBox1)
    app.sueFinal = Image.open('photo/suefinals.PNG')
    app.sueFinal = CMUImage(app.sueFinal)
    app.background4 = Image.open('photo/background4.png')
    app.background4 = CMUImage(app.background4)
    app.winner_game1=''
    app.Char1=Image.open('photo/2.PNG')
    app.Char1=CMUImage(app.Char1)
    app.Char2=Image.open('photo/3.PNG')
    app.Char2=CMUImage(app.Char2)
    app.Char3=Image.open('photo/6.PNG')
    app.Char3=CMUImage(app.Char3)
    app.Char4=Image.open('photo/8.PNG')
    app.Char4=CMUImage(app.Char4)
    app.backgroundImage5 = Image.open('photo/background5.png')
    app.backgroundImage5 = CMUImage(app.backgroundImage5)
    app.wedding = Image.open('photo/wedding.png')
    app.wedding = CMUImage(app.wedding)
    app.canDrawChar1=False
    app.canDrawChar2=False
    app.canDrawChar3=False
    app.canDrawChar4=False
    app.scores={'Charlie':0,'Charles':0,'Chris':0,'Chase':0}
    app.base=False
    app.topping=False
    app.stove=False
    app.curr1 = None
    app.curr2 = None
    app.curr3 = None
    app.curr4 = None
    app.cx = None
    app.cy = None
    app.dx = None
    app.dy = None
    app.ex = None
    app.ey = None
    app.basecake=CMUImage(Image.open('plain-pizza-clipart.png'))
    app.ingre=[CMUImage(Image.open('WechatIMG79.jpg')),
                CMUImage(Image.open('WechatIMG78.jpg')),CMUImage(Image.open('WechatIMG82.jpg'))]
    app.toppings=[]
    app.result=[]
    app.answers=[(500,500),(600,435),(400,435),(680,330),(320,330),(650,215),(350,215),(565,170),(435,170),(500,235)]
    app.score=[]
    app.eveness=[0,0,0]
    app.dis=[]
    app.distribution=0
    app.backgroundImageHeartBG = Image.open("photo/heartbg.jpeg")
    app.backgroundImageHeartBG = CMUImage(app.backgroundImageHeartBG)
    app.backgroundImageHeart = Image.open("heart.PNG")
    app.backgroundImageHeart = CMUImage(app.backgroundImageHeart)
    app.finalResult=[]
    app.clothScore=dict()
    app.dress=[clo.unidress,clo.cutedress,clo.sexydress,clo.elegdress]
    app.dress2=None
    app.shirt=[clo.unishirt,clo.cuteshirt,clo.sexyshirt,clo.elegshirt]
    app.shirt2=None
    app.shoes=[clo.unishoes,clo.cuteshoes,clo.sexyshoes,clo.elegshoes]
    app.shoes2=None
    app.clothScore=dict()
    app.score_game_3_round_1_b1_add=0
    app.score_game_3_round_2_b2_add=0
    app.score_game_3_round_3_b3_add=0
    app.score_game_3_round_4_b4_add=0
    app.score_game_3=dict()
    app.total_score_game3={'Charlie':0,'Charles':0,'Chris':0,'Chase':0}
    app.game3_next_page=False

    app.sound1 = loadSound("sounds/weddingSong.mp3")

    app.sound1.play(loop = True)

def loadSound(relativePath):
    absolutePath = os.path.abspath(relativePath)
    url = pathlib.Path(absolutePath).as_uri()
    return Sound(url)

def add_game3(app):
    app.scores['Charlie']+=app.score_game_3_round_1_b1_add
    app.scores['Charles']+=app.score_game_3_round_2_b2_add
    app.scores['Chris']+=app.score_game_3_round_3_b3_add
    app.scores['Chase']+=app.score_game_3_round_4_b4_add 

class A: 
    def __init__(self): 
        self.name='Charlie'
        self.score=0

class B: 
    def __init__(self): 
        self.name='Charles'
        self.score=0


class C: 
    def __init__(self): 
        self.name='Chris'
        self.score=0

class D: 
    def __init__(self): 
        self.name='Chase'
        self.score=0

a=A()
b=B()
c=C()
d=D()

def redrawAll(app):
    if app.page1:
        drawPage1(app)
    elif app.page2:
        drawPage2(app)
        drawPage2Buttons(app)
        if app.canDrawChar1:
            drawChar1(app)
        if app.canDrawChar2:
            drawChar2(app)
        if app.canDrawChar3:
            drawChar3(app)
        if app.canDrawChar4:
            drawChar4(app)
    elif app.page3: 
        drawPage3(app)
    elif app.page4:
        drawPage4(app)
   
    elif app.page5: 
        drawPage5(app)
    elif app.page6:
        drawPage6(app)
    elif app.page7:
        drawPage7(app)
    elif app.pageCloset:
        drawCloset(app)
    elif app.page8:
        drawPage8(app)
    elif app.page9:
        drawPage9(app)
    # elif app.page123:
        # drawPage123(app)
    elif app.pageQuiz:
        drawPageQuiz(app)
    elif app.page10:
        add_game3(app)
        drawPage10(app)
    

def drawChar1(app):
    drawOval(260,470,200,150,fill='steelBlue',opacity=40)
    drawOval(800,475,300,200,fill='steelBlue',opacity=40)
    drawImage(app.Char1,275,300,width=350,height=450)
    drawLabel('Charlie',800,400,size=30,fill='white',font='monospace')
    drawLabel('Major: CS',250,450,size=30,fill='white',font='monospace')
    drawLabel('Age: 19',250,500,size=30,fill='white',font='monospace')
    drawLabel('Height: 180 cm',800,450,size=30,fill='white',font='monospace')
    drawLabel('Ideal Type: Cute Type',800,500,size=30,fill='white',font='monospace')

def drawChar2(app):
    drawOval(260,470,200,150,fill='steelBlue',opacity=40)
    drawOval(800,475,300,200,fill='steelBlue',opacity=40)
    drawImage(app.Char2,375,300,width=250,height=450)
    drawLabel('Charles',800,400,size=30,fill='white',font='monospace')
    drawLabel('Major: Math',250,450,size=30,fill='white',font='monospace')
    drawLabel('Age: 20',250,500,size=30,fill='white',font='monospace')
    drawLabel('Height: 178 cm',800,450,size=30,fill='white',font='monospace')
    drawLabel('Ideal Type: Elegant Type',800,500,size=30,fill='white',font='monospace')

def drawChar3(app):
    drawOval(260,470,200,150,fill='steelBlue',opacity=40)
    drawOval(800,475,300,200,fill='steelBlue',opacity=40)
    drawImage(app.Char3,375,300,width=260,height=450)
    drawLabel('Chris',800,400,size=30,fill='white',font='monospace')
    drawLabel('Major: Geometry',250,450,size=30,fill='white',font='monospace')
    drawLabel('Age: 19',250,500,size=30,fill='white',font='monospace')
    drawLabel('Height: 188 cm',800,450,size=30,fill='white',font='monospace')
    drawLabel('Ideal Type: Sexy Type',800,500,size=30,fill='white',font='monospace')

def drawChar4(app):
    drawOval(260,470,200,150,fill='steelBlue',opacity=40)
    drawOval(800,475,300,200,fill='steelBlue',opacity=40)
    drawImage(app.Char4,400,300,width=250,height=450)
    drawLabel('Chase',800,400,size=30,fill='white',font='monospace')
    drawLabel('Major: Athletics',250,450,size=30,fill='white',font='monospace')
    drawLabel('Age: 100',250,500,size=30,fill='white',font='monospace')
    drawLabel('Height: 168 cm',800,450,size=30,fill='white',font='monospace')
    drawLabel('Ideal Type: Unique Type',800,500,size=30,fill='white',font='monospace')

def drawPage2(app):
    print('here')
    drawImage(app.backgroundImage2,0,0, width = 1000, height = 800)
    drawRect(0, 0, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 75, 50, fill = 'white', size = 30)

def drawPageQuiz(app):
    
    drawLabel('Are You My Soulmate(Click Any Where to Next Page)',500,100,size=28,font='monospace',fill='pink')
    drawRect(250-100,300,200,100,fill='pink')
    drawRect(750-100,300,200,100,fill='pink')
    drawRect(250-100,500,200,100,fill='pink')
    drawRect(750-100,500,200,100,fill='pink')
    drawLabel(f'Test 1:{app.score_game_3_round_1_b1_add}',250,350,size=20,font='monospace')
    drawLabel(f'Test 2:{app.score_game_3_round_2_b2_add}',750,350,size=20,font='monospace')
    drawLabel(f'Test 3:{app.score_game_3_round_3_b3_add}',250,550,size=20,font='monospace')
    drawLabel(f'Test 4:{app.score_game_3_round_4_b4_add}',750,550,size=20,font='monospace')
    if app.game3_next_page:
        drawLebal('Click Any Where to Next Page',500,400,size=28)


def drawPage2Buttons(app):
    for i in range(4):
        startLeft=150+200*i
        startTop=100
        drawRect(startLeft,startTop,100,100,fill=None,border='midnightBlue',borderWidth=5)
        drawLabel(i+1,startLeft+50,startTop+50,fill='midnightBlue',size=40,bold=True)
    drawLabel('Press Button to Have a Closer look of Your Boys', 500,50,size=32,fill='navy',font='monospace',bold=True)

def onMouseDrag(app, mouseX, mouseY):
    if app.base: 
        app.cx = mouseX
        app.cy = mouseY
        if 110<=app.cx<=210 and 600<=app.cy<=700: 
            app.curr1=app.ingre[0]
        elif 310<=app.cx<=410 and 600<=app.cy<=700: 
            app.curr1=app.ingre[1]
        elif 510<=app.cx<=610 and 600<=app.cy<=700: 
            app.curr1=app.ingre[2]

def onMousePress(app,mouseX,mouseY):
    #test
    if app.pageQuiz and not app.page1 and not app.page2 and not app.page3 and not app.page4 and not app.page5 and not app.page6 and not app.page7 and not app.page8 and not app.page9 and not app.pageCloset:
        MousePressQuiz(app, mouseX, mouseY)

    if 0<=mouseX<=200 and 0<=mouseY<=100: 
        if app.page1: 
            app.page1=False
        elif app.page2: 
            app.page2=False
        elif app.page3: 
            app.page3=False
        elif app.page4:
            app.page4 = False
        elif app.page5:
            app.page5 = False
        elif app.page6:
            app.page6 = False
        elif app.page7:
            app.page7= False
        elif app.pageCloset:
            app.pageCloset = False
        elif app.page8:
            app.page8 = False
        elif app.page9:
            app.page9 = False
        # elif app.page123:
        #     app.page123=False
        elif app.pageQuiz:
            app.pageQuiz = False
    if 700<=mouseX<=900 and 650<=mouseY<=750 and app.page5:
        app.page5 = False
        # elif app.page5: 
        #     app.page5=False
    if 150<=mouseX<=250 and 100<=mouseY<=200:
        app.canDrawChar1=True
        app.canDrawChar2=False
        app.canDrawChar3=False
        app.canDrawChar4=False
    elif 350<=mouseX<=450 and 100<=mouseY<=200:
        app.canDrawChar2=True
        app.canDrawChar1=False
        app.canDrawChar3=False
        app.canDrawChar4=False
    elif 550<=mouseX<=650 and 100<=mouseY<=200:
        app.canDrawChar3=True
        app.canDrawChar1=False
        app.canDrawChar2=False
        app.canDrawChar4=False
    elif 750<=mouseX<=850 and 100<=mouseY<=200:
        app.canDrawChar4=True
        app.canDrawChar1=False
        app.canDrawChar2=False
        app.canDrawChar3=False
    if (550>=mouseX>=400) and (525>=mouseY>=375):
        app.canDrawChar1=True
            #app.base=True#start the pizza game
        app.winner_game1='Charlie'
        if app.page4:
            app.page4=False
            app.base=True
    elif (750>=mouseX>=600) and (525>=mouseY>=375):
        app.canDrawChar2=True
            #start the pizza game
        app.winner_game1='Charles'
        if app.page4:
            app.page4=False
            app.base=True
    elif (550>=mouseX>=400) and (700>=mouseY>=550):
        app.canDrawChar3=True
            #start the pizza game
        # print(app.result)
        app.winner_game1='Chris'
        if app.page4:
            app.page4=False
            app.base=True
        
    elif (750>=mouseX>=600) and (700>=mouseY>=550):
        app.canDrawChar4=True
            #start the pizza game
        # print(app.result)
        app.winner_game1='Chase'
        if app.page4:
            app.page4=False
            app.base=True
    if 850<=mouseX<=950 and 650<=mouseY<=750: 
        # print(app.result)
        # print(app.scores)
        # print(sum(app.result))
        app.scores[app.winner_game1]=(100-(sum(app.result)//5))
        # print(app.scores)
        if app.base: 
            app.base=False
#  def loadSound(relativePath):
#     absolutePath = os.path.abspath(relativePath)
#     url = pathlib.Path(absolutionPath).as_uri()
    if clo.dress==None and clo.shirt==None and clo.shoes==None: 
        app.dx = mouseX
        app.dy = mouseY
        if 650<=app.dx<=700 and 300<=app.dy<=400: 
            app.curr2=app.dress[3]
        elif 800<=app.dx<=875 and 325<=app.dy<=435: 
            app.curr2=app.dress[2]
        elif 725<=app.dx<=785 and 500<=app.dy<=560: 
            app.curr2=app.dress[1]
        elif 835<=app.dx<=910 and 470<=app.dy<=560: 
            app.curr2=app.dress[0]
        clo.dress=app.curr2
        if clo.dress==clo.cutedress:
            a.score+=20
        elif clo.dress==clo.elegdress:
            b.score+=20
        elif clo.dress==clo.sexydress:
            c.score+=20
        elif clo.dress==clo.unidress:
            d.score+=20
    elif clo.dress!=None and clo.shirt==None and clo.shoes==None: 
        app.ex = mouseX
        app.ey = mouseY
        if 650<=app.ex<=700 and 300<=app.ey<=400: 
            app.curr3=app.shirt[0]
        elif 580<=app.ex<=660 and 500<=app.ey<=600: 
            app.curr3=app.shirt[2]
        elif 700<=app.ex<=780 and 500<=app.ey<=600: 
            app.curr3=app.shirt[1]
        elif 820<=app.ex<880 and 500<=app.ey<=600: 
            app.curr3=app.shirt[3]
        clo.shirt=app.curr3
        if clo.shirt==clo.cuteshirt:
            a.score+=50
        elif clo.shirt==clo.elegshirt:
            b.score+=50
        elif clo.shirt==clo.sexyshirt:
            c.score+=50
        elif clo.shirt==clo.unishirt:
            d.score+=50
        print(clo.shirt)
    elif clo.dress!=None and clo.shirt!=None and clo.shoes==None: 
        app.fx = mouseX
        app.fy = mouseY
        if 800<=app.fx<=870 and 280<=app.fy<=390: 
            app.curr4=app.shoes[2]
        elif 650<=app.fx<=760 and 270<=app.fy<=420: 
            app.curr4=app.shoes[0]
        elif 650<=app.fx<=760 and 500<=app.fy<=600: 
            app.curr4=app.shoes[3]
        elif 800<=app.fx<=870 and 400<=app.fy<=560: 
            app.curr4=app.shoes[1]
        app.shoes=[clo.unishoes,clo.cuteshoes,clo.sexyshoes,clo.elegshoes]
        clo.shoes=app.curr4
        if clo.shoes==clo.cuteshoes:
            a.score+=30
        elif clo.shoes==clo.elegshoes:
            b.score+=30
        elif clo.shoes==clo.sexyshoes:
            c.score+=30
        elif clo.shoes==clo.unishoes:
            d.score+=30
    app.clothScore[a.name]=a.score//3
    app.clothScore[b.name]=b.score//3
    app.clothScore[c.name]=c.score//3
    app.clothScore[d.name]=d.score//3


def MousePressQuiz(app, mouseX, mouseY):
    if (350>=mouseX>=150) and (400>=mouseY>=300):
        root = tk.Tk()
        game1 = CodeTracing(root)
        root.mainloop()
        app.score_game_3_round_1_b1_add=game1.score
        app.total_score_game3['Charlie']=game1.score
    elif (850>=mouseX>=650) and (400>=mouseY>=300):
        root = tk.Tk()
        game2 = MathGame(root)
        root.mainloop()
        app.score_game_3_round_2_b2_add=game2.score
        app.total_score_game3['Charles']=game2.score
    elif (350>=mouseX>=150) and (600>=mouseY>=500):
        root = tk.Tk()
        game3 = GeographyGame(root)
        root.mainloop()
        app.score_game_3_round_3_b3_add=game3.score
        app.total_score_game3['Chris']=game3.score
    elif (850>=mouseX>=650) and (600>=mouseY>=500):
        root = tk.Tk()
        game4 = SportsTriviaGame(root)
        root.mainloop()
        app.score_game_3_round_4_b4_add=game4.score
        app.total_score_game3['Chase']=game4.score
        

def drawPage1(app):
    drawImage(app.backgroundImage1,0,0, width = 1000, height = 800)
    # drawImage(app.backgroundImage2, 0, 0, width = 1000, height = 800)
    drawImage(app.sue, 100, 300, width = 200, height = 500)
    # imageWidth, imageHeight = getImageSize(app.textBox1)
    # print(imageWidth, imageHeight)
    # drawImage(app.textBox1, 300, 350, width = 280, height = 100)
    # drawRect(550, 412, 500, 100, align = 'center', opacity = 80, fill = 'white')
    text = '''
        112 is so hard,
        I wish that I could have date. 
        I think I might have four options.'''
    
    drawImage(app.textBox1, 550, 412, align = 'center', width = 500, height = 300)
    lines = text.splitlines()
    for i in range (len(lines)):
        line = lines[i]
        drawLabel(line, 500, 350 + i + i * 30, size = 15, fill = 'black', font= 'monospace')
    
    drawRect(0, 0, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 75, 50, fill = 'white', size = 30)

def drawPage3(app): 
    drawImage(app.coffeeBackground3, 0, 0, width = 1000, height = 800)
    drawImage(app.sue, 100, 300, width = 200, height = 500)
    text = '''
        It's carnival soon, 
        I could make a pizza for my boy'''
    
    drawImage(app.textBox1, 550, 412, align = 'center', width = 500, height = 300)
    lines = text.splitlines()
    for i in range (len(lines)):
        line = lines[i]
        drawLabel(line, 500, 350 + i + i * 30, size = 15, fill = 'black', font= 'monospace')
    
    drawRect(0, 0, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 75, 50, fill = 'white', size = 30)
    

def drawPage4(app):
    drawImage(app.backgroundImage4,0,0, width = 1000, height = 800)
    drawLabel('Making Pizza For Your Boy',500,100,fill='white',size=40,font='monospace',bold=True)
    drawLabel('Click button to choose the boy you want to make pizza for',500,175,fill='mediumOrchid',size=18,font='monospace',bold=True)
    drawLabel('Try your best to drag toppings match with the black point',500,225,fill='mediumOrchid',size=18,font='monospace',bold=True)
    drawLabel('Also try to make the number of toppings more even',500,275,fill='mediumOrchid',size=18,font='monospace',bold=True)
    drawLabel('The more you are closer to the black point and more even, the more the boy is falling for you',500,325,fill='mediumOrchid',size=17,font='monospace',bold=True)
    for i in range(2):
        drawRect(400+200*i,375,150,150,border='darkOrchid',fill=None)
    for i in range(2):
        drawRect(400+200*i,550,150,150,border='darkOrchid',fill=None)
    drawLabel('Charlie',475,450,size=30,fill='darkOrchid',font='monospace',bold=True)
    drawLabel('Charles',675,450,size=30,fill='darkOrchid',font='monospace',bold=True)
    drawLabel('Chris',475,625,size=30,fill='darkOrchid',font='monospace',bold=True)
    drawLabel('Chase',675,625,size=30,fill='darkOrchid',font='monospace',bold=True)
              
#def drawPage4(app): 
    #drawImage(app.background4, 0, 0, width = 1000, height = 800)
    #drawImage(app.sueFinal, 100, 300, width = 200, height = 500)
    #text = '''
        #Finally finished my finals, 
            #I want to have a sweet date with my boys'''
    
    #drawImage(app.textBox1, 550, 412, align = 'center', width = 500, height = 300)
    #lines = text.splitlines()
    #for i in range (len(lines)):
        #line = lines[i]
        #drawLabel(line, 500, 350 + i + i * 30, size = 15, fill = 'black', font= 'monospace')
    #drawRect(700, 650, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    #drawLabel('Continue', 800, 700, fill = 'white', size = 30)    
    #instruction = '''
              #Remember that each boy has a different ideal type?
             #Try to put on the best fit for you boy
             #to get that boy fall for you! 
             #'''
    #instructionLines = instruction.splitlines()
    #for i in range (len(instructionLines)):
        #instructionLine = instructionLines[i]
        #drawLabel(instructionLine, 400, 100 + i * 30, size = 30, fill = 'darkGreen', bold = True, font = 'monospace')

#def drawPage4(app):
    #drawImage(app.backgroundImage5,0,0, width = 1000, height = 800)
    #drawImage(app.Char1,-50,300,width=315,height=405)
    #drawImage(app.Char2,300,300,width=225,height=405)
    #drawImage(app.Char3,500,300,width=234,height=405)
    #drawImage(app.Char4,750,300,width=225,height=405)
    #drawRect(100, 80, 800, 80, fill = 'white', opacity = 80)
    #drawLabel('Babe, are you my soulmate~',500,120,size=40,font='monospace',fill='paleVioletRed', bold=True)
    #drawRect(200, 175, 600, 125, fill = 'white', opacity = 80)
   # quizInstruction = '''
    #                    Babe, I am looking for someone who can 
    #                    really understand me and my major,
    #                    can you answer these questions for me?'''
    #quizLines = quizInstruction.splitlines()
    #for i in range (len(quizLines)):
    #    quizLine = quizLines[i]
    #    drawLabel(quizLine, 400, 175 + i * 30, fill = 'paleVioletRed', size = 30)
    #drawRect(700, 650, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    #drawLabel('Continue', 800, 700, fill = 'white', size = 30) 
    

#def drawPage5(app): 
    #drawImage(app.wedding, 0, 0, width = 1000, height = 800)
    #drawImage(app.sue, 300, 300, width = 200, height = 500)

def drawPage5(app):
    drawRect(0,0,1000,800,fill='pink')
    drawRect(900,700,100,100,align='center',fill='black')
    drawImage(app.basecake,500,300,width=500,height=500,align='center')
    for i in range(3):
        drawImage(app.ingre[i],110+200*i,650,width=100,height=100)
    for k in app.answers: 
       drawCircle(k[0],k[1],5,fill='black')
    for j in app.toppings: 
        drawImage(j[0],j[1],j[2],width=80,height=80,align='center')
    if app.curr1!=None: 
        drawImage(app.curr1,app.cx,app.cy,width=80,height=80,align='center')
    if app.score==[]: 
        drawLabel(f'Accuracy: {100}',135,50,size=35) 
        drawLabel(f'Eveness: None',135,100,size=35) 
    elif len(app.toppings)==10:
        drawLabel(f'Accuracy: {100-sum(app.result)//8}',135,50,size=35)
        print(100-sum(app.result)//8)
        drawLabel(f'Eveness: {app.distribution}',135,100,size=35) 
    elif app.score!=[]:
        drawLabel(f'Accuracy: {100-sum(app.result)//8}',135,50,size=35)
        drawLabel(f'Eveness: None',135,100,size=35) 

def distance(x0,y0,x1,y1): 
    return int(((x1-x0)**2+(y0-y1)**2)**0.5)
def onKeyPress(app,key):
    if key=='up':
        print(app.scores)

def onMouseRelease(app, mouseX, mouseY):
    if app.curr1!=None and [app.curr1,mouseX,mouseY] not in app.toppings:
        app.toppings+=[[app.curr1,mouseX,mouseY]]
    app.curr1=None

    for i in app.toppings: 
        smallest=[]
        for j in app.answers: 
            smallest+=[distance(i[1],i[2],j[0],j[1])] 
        app.score+=[min(smallest)]
    app.result=app.score[len(app.score)-len(app.toppings):]
    app.eveness=helper1(app.toppings,[0,0,0],app.ingre)
    if sorted(app.eveness)==[3,3,4]:
        app.distribution=100
    elif sorted(app.eveness)==[2,3,5]:
        app.distribution=93
    elif sorted(app.eveness)==[2,4,4]:
        app.distribution=97
    elif sorted(app.eveness)==[2,2,6]:
        app.distribution=90
    elif sorted(app.eveness)==[1,2,7]:
        app.distribution=87
    elif sorted(app.eveness)==[1,3,6]:
        app.distribution=80
    elif sorted(app.eveness)==[1,4,5]:
        app.distribution=83
    elif sorted(app.eveness)==[0,5,5]:
        app.distribution=77
    elif sorted(app.eveness)==[0,4,6]:
        app.distribution=73
    elif sorted(app.eveness)==[0,3,7]:
        app.distribution=70
    elif sorted(app.eveness)==[0,2,8]:
        app.distribution=67
    else: 
        app.distribution=60
    print(app.result)
    
def helper1(L,res,M):
    if L==[]: 
        return res
    else: 
        num=L[0]
        rest=L[1:]
        if num[0]==M[0]: 
            res[0]+=1
        elif num[0]==M[1]: 
            res[1]+=1
        elif num[0]==M[2]: 
            res[2]+=1
        return helper1(rest,res,M)

def drawPage6(app):
    print('page6')
    drawImage(app.backgroundImageHeartBG,0,0, width = 1000, height = 800)
    drawImage(app.backgroundImageHeart,100,400,width=400,height=200)
    drawLabel('Babe, I am falling for you~',500,120,size=40,font='monospace',fill='paleVioletRed',bold=True)
    
    maxScore=0
    maxWinner=None

    for char in app.scores:
        if app.scores[char]>maxScore:
            maxWinner=char
    
    if maxWinner=='Charlie':
        drawImage(app.Char1,275,300,width=350,height=450)
        drawLabel(100-app.scores[maxWinner],275,500,size=30,bold=True)
    if maxWinner=='Charles':
        drawImage(app.Char2,275,300,width=350,height=450)
        drawLabel(100-app.scores[maxWinner],275,500,size=30,bold=True)
    if maxWinner=='Chris':
        drawImage(app.Char3,275,300,width=350,height=450)
        drawLabel(100-app.scores[maxWinner],275,500,size=30,bold=True)
    if maxWinner=='Chase':
        drawImage(app.Char4,275,300,width=350,height=450)
        drawLabel(100-app.scores[maxWinner],275,500,size=30,bold=True)
    drawRect(0, 0, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 75, 50, fill = 'white', size = 30)


def drawCloset(app):
    drawRect(0,0,1000,800,fill='pink')
    drawImage(CMUImage(Image.open('Naked.png')),150,110,width=150,height=450)
    if clo.dress==None:
        drawImage(CMUImage(Image.open('skirt.png')),500,110,width=450,height=600)
    elif clo.shirt==None: 
        drawImage(clo.dress,230,425,width=135,height=110,align='center')
        drawImage(CMUImage(Image.open('clothes.png')),500,110,width=450,height=600)
    elif clo.shoes==None: 
        drawImage(clo.dress,230,425,width=135,height=110,align='center')
        drawImage(clo.shirt,235,335,width=150,height=125,align='center')
        drawImage(CMUImage(Image.open('shoes.png')),500,110,width=450,height=600)
    else:
        drawImage(clo.dress,230,425,width=135,height=110,align='center')
        drawImage(clo.shirt,235,335,width=150,height=125,align='center')
        drawImage(clo.shoes,230,560,width=100,height=110,align='center')
    drawRect(0, 0, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 75, 50, fill = 'white', size = 30)


def drawPage7(app): 
    drawImage(app.background4, 0, 0, width = 1000, height = 800)
    drawImage(app.sueFinal, 100, 300, width = 200, height = 500)
    text = '''
        Finally finished my finals, 
            I want to have a sweet date with my boys'''
    
    drawImage(app.textBox1, 550, 412, align = 'center', width = 500, height = 300)
    lines = text.splitlines()
    for i in range (len(lines)):
        line = lines[i]
        drawLabel(line, 500, 350 + i + i * 30, size = 15, fill = 'black', font= 'monospace')
    drawRect(0, 0, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 75, 50, fill = 'white', size = 30)

    instruction = '''
              Remember that each boy has a different ideal type?
             Try to put on the best fit for you boy
             to get that boy fall for you! 
             '''
    instructionLines = instruction.splitlines()
    for i in range (len(instructionLines)):
        instructionLine = instructionLines[i]
        drawLabel(instructionLine, 400, 100 + i * 30, size = 30, fill = 'darkGreen', bold = True, font = 'monospace')


def drawPage8(app):
    # drawImage(app.backgroundImageHeartBG,0,0, width = 1000, height = 800)
    # drawImage(app.backgroundImageHeart,100,400,width=400,height=200)
    
    # if app.canDrawChar1:
    #     drawImage(app.Char1,300,300,width=350,height=450)
    #     # drawLabel(f'{app.scores['Charlie']}',300,500,size=40)
    # if app.canDrawChar2:
    #     drawImage(app.Char2,375,300,width=250,height=450)
    #     # drawLabel(f'{app.scores['Charles']}',300,500,size=40)
    # if app.canDrawChar3:
    #     drawImage(app.Char3,375,300,width=260,height=450)
    #     # drawLabel(f'{app.scores['Chris']}',300,500,size=40)
    # if app.canDrawChar4:
    #     drawImage(app.Char4,400,300,width=250,height=450)
        # drawLabel(f'{app.scores['Chase']}',300,500,size=40)
    drawRect(0, 0, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 75, 50, fill = 'white', size = 30)
    drawImage(app.backgroundImage5,0,0, width = 1000, height = 800)
    drawImage(app.Char1,-50,300,width=315,height=405)
    drawImage(app.Char2,300,300,width=225,height=405)
    drawImage(app.Char3,500,300,width=234,height=405)
    drawImage(app.Char4,750,300,width=225,height=405)
    drawRect(0, 0, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 75, 50, fill = 'white', size = 30)
    drawLabel('Babe, I am falling for you~',500,120,size=40,font='monospace',fill='paleVioletRed',bold=True)
    for key in app.scores:
        print(key, app.Char1)
        if key=='Charlie':
            drawLabel(app.scores[key],200,300,size=40,bold=True, fill = 'red')
        if key=='Charles':
            drawLabel(app.scores[key],400,300,size=40,bold=True, fill = 'red')
        if key=='Chris':
            drawLabel(app.scores[key],600,300,size=40,bold=True, fill = 'red')
        if key=='Chase':
            drawLabel(app.scores[key],850,300,size=40,bold=True, fill = 'red')

def drawPage9(app):
    drawImage(app.backgroundImage5,0,0, width = 1000, height = 800)
    drawImage(app.Char1,-50,300,width=315,height=405)
    drawImage(app.Char2,300,300,width=225,height=405)
    drawImage(app.Char3,500,300,width=234,height=405)
    drawImage(app.Char4,750,300,width=225,height=405)
    drawRect(100, 80, 800, 80, fill = 'white', opacity = 80)
    drawLabel('Babe, are you my soulmate~',500,120,size=40,font='monospace',fill='paleVioletRed', bold=True)
    drawRect(200, 175, 600, 125, fill = 'white', opacity = 80)
    quizInstruction = '''
                        Babe, I am looking for someone who can 
                        really understand me and my major,
                        can you answer these questions for me?'''
    quizLines = quizInstruction.splitlines()
    for i in range (len(quizLines)):
        quizLine = quizLines[i]
        drawLabel(quizLine, 400, 175 + i * 30, fill = 'paleVioletRed', size = 30)
    drawRect(0, 0, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 75, 50, fill = 'white', size = 30)


def drawPage10(app):
    drawImage(app.wedding, 0, 0, width = 1000, height = 800)
    drawImage(app.sue, 300, 300, width = 200, height = 500)
    maxScore=0
    maxWinner=None
    for char in app.scores:
        if app.scores[char]>maxScore:
            maxWinner=char
    if maxWinner=='Charlie':
        drawImage(app.Char1,275,300,width=350,height=450)
        drawLabel(app.scores['Charlie'],450,200,size=40,font='monospace',bold=True)
    if maxWinner=='Charles':
        drawImage(app.Char2,275,300,width=350,height=450)
        drawLabel(app.scores['Charles'],450,200,size=40,font='monospace',bold=True)
    if maxWinner=='Chris':
        drawImage(app.Char3,275,300,width=350,height=450)
        drawLabel(app.scores['Chris'],450,200,size=40,font='monospace',bold=True)
    if maxWinner=='Chase':
        drawImage(app.Char4,275,300,width=350,height=450)
        drawLabel(app.scores['Chase'],450,200,size=40,font='monospace',bold=True)
    drawRect(0, 0, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 75, 50, fill = 'white', size = 30)

# def drawPage123(app):
#     drawPage123Helper(app)
#     drawChar1H(app)
#     drawChar2H(app)
#     drawChar3H(app)
#     drawChar4H(app)

# def drawPage123Helper(app):
#     # app.image = Image.open("images/Caaaaat.jpg")
#     #drawImage(app.backgroundImageHeart,0,0, width = 1000, height = 800)
#     drawLabel('Babe, we are all falling for you~',500,70,size=40,font='monospace',fill='paleVioletRed',bold=True)
    # textBox1 = CMUImage(Image.open('textbox1'))
    # drawImage(textBox1, 300, 300, width = 100, height = 100)

def drawChar1H(app):
    drawImage(app.backgroundHeart,50,100,width=200,height=200)
    drawImage(app.Char1,-100,300,width=350,height=450)
    
def drawChar2H(app):
    drawImage(app.backgroundHeart,275,100,width=200,height=200)
    drawImage(app.Char2,250,300,width=250,height=450)
    
def drawChar3H(app):
    drawImage(app.backgroundHeart,520,100,width=200,height=200)
    drawImage(app.Char3,500,300,width=260,height=450)
    
def drawChar4H(app):
    drawImage(app.backgroundHeart,750,100,width=200,height=200)
    drawImage(app.Char4,750,300,width=250,height=450)




class CodeTracing:
    def __init__(self, master):
        self.master = master
        self.master.title("Code Tracing")
        self.master.geometry("1000x800")

        self.score = 0
        self.current_question = 0
        self.questions = [
            {"definition": "def ct(t):\n    L = [ ]\n    for x,y in t:\n        L.append(x+y)\n    return tuple(L) + t[1]\nt = ((3, -4), (-5, 5), (3, 1))\nprint(ct(t))",
             "options": ["(-1, 1, -2, -4, -5, 1)", "(-1, 1, -2, 1, 2, 1)", "(2, 1, -2, 1, 1, 1)", "(-1, 1, 1, 2, -5, 1)"],
             "answer": "(-1, 1, -2, -4, -5, 1)"},
            {"definition": "def ct(L):\n    M = [ (L[i-1], L[i]) for i in range(1, len(L)) ]\n    t = tuple(M)\n    t += ((min(L), max(L)),)\n    return t\nprint(ct([5, -3, 5, -1]))",
             "options": ["((5, -3), (5, -1), (-3, 5), (5, 5), (-3, -1), (5, -1))", "((5, 5), (-3, -1), (5, -1), (5, 5), (-3, 5), (5, -3))", "((5, -3), (-1, 5), (-3, 5), (5, 5), (5, -1), (5, -3))", "((-3, 5), (-3, -1), (5, -3), (5, 5), (5, -1), (5, -3))"],
             "answer": "((5, -3), (5, -1), (-3, 5), (5, 5), (-3, -1), (5, -1))"},
            {"definition": "def ct(L):\n    M = list(range(len(L)))\n    for i in range(1, len(M)):\n        L[i] += M[i]\n        M[-i] += M[i]\n    return M\nL = [0, 4, 5, 3]\nprint(ct(L))\nprint(L)",
             "options": ["[0, 4, 5, 3]\n[0, 4, 5, 3]", "[0, 3, 5, 6]\n[0, 3, 5, 6]", "[0, 3, 5, 6]\n[0, 4, 5, 3]", "[0, 4, 5, 3]\n[0, 3, 5, 6]"],
             "answer": "[0, 3, 5, 6]\n[0, 4, 5, 3]"},
            {"definition": "import copy\ndef ct(L):\n    A = copy.deepcopy(L)\n    B = [A[0], L[1]]\n    B[1][0] = 1\n    A[0].pop()\n    A = A[1] + A[0]\n    B[1] = sorted(B[0])\n    print(A)\n    print(B)\nL = [[2, 1, 4], [5, 3]]\nct(L)\nprint(L)",
             "options": ["[1, 5, 3, 2, 1, 4]\n[[2, 1, 4], [1, 3]]\n[[2, 1, 4], [5, 3]]", "[1, 5, 3, 2, 1, 4]\n[[2, 1, 4], [1, 3]]\n[[1, 3], [2, 1, 4]]", "[1, 5, 3, 2, 1, 4]\n[[2, 1, 4], [2, 1, 4]]\n[[2, 1, 4], [5, 3]]", "[1, 5, 3, 2, 1, 4]\n[[2, 1, 4], [2, 1, 4]]\n[[1, 3], [2, 1, 4]]"],
             "answer": "[1, 5, 3, 2, 1, 4]\n[[2, 1, 4], [1, 3]]\n[[2, 1, 4], [5, 3]]"},
            {"definition": "import copy\ndef ct(L):\n    a = L\n    b = copy.copy(L)\n    c = copy.deepcopy(L)\n    a[0] = b[1]\n    b[1][1] = c[0]\n    c[1].append(b[1])\n    a[0][0] += (b[1].pop())[0]\n    return (a,b,c)",
             "options": ["([1, 3], [2, [2, 1, 4]])", "([1, 3], [[2, 1, 4], [2, 1, 4]])", "([2, [2, 1, 4]], [[2, 1, 4], [2, 1, 4]])", "([[2, 1, 4], [2, 1, 4]], [[1, 3], [2, [2, 1, 4]])"],
             "answer": "([1, 3], [2, [2, 1, 4]])"}
        ]

        self.question_label = tk.Label(master, text="", font=("Arial", 14), wraplength=800, justify="left")
        self.question_label.pack(pady=(20, 200))

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", font=("Arial", 12), width=80, wraplength=800, justify="left", command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=10)
            self.option_buttons.append(button)

        self.update_question()

    def update_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["definition"])
            options = question_data["options"]
            random.shuffle(options)
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
        else:
            self.show_score()
            self.master.update()  # 立即更新窗口
            self.master.after(1000, self.master.destroy)  # 等待3秒后关闭窗口

    def check_answer(self, idx):
        if self.option_buttons[idx].cget("text") == self.questions[self.current_question]["answer"]:
            self.score += 1
            
        self.current_question += 1
        self.update_question()

    def show_score(self):
        self.question_label.config(text=f"你的得分是: {self.score}/5")
        
        for button in self.option_buttons:
            button.pack_forget()
class MathGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Math Game")
        self.master.geometry("1000x800")

        self.questions = {
            "1. 5×6+9÷3−2 = ?": ["23", "24", "25", "26"],
            "2. 7×4−8÷2+3 = ?": ["29", "30", "31", "32"],
            "3. 10×2+12÷3−5 = ?": ["25", "26", "27", "28"],
            "4. 8×5−10÷2+6 = ?": ["39", "40", "41", "42"],
            "5. 5^6-9÷3+2 = ?": ["15616", "15617", "15618", "15619"]
        }

        self.current_question = None
        self.answers = None
        self.correct_answer = None
        self.score = 0
        self.question_count = 0

        self.create_widgets()
        self.ask_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.question_label.pack(pady=20)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.master, text="", font=("Helvetica", 16), width=20, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.answer_buttons.append(button)

        self.score_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.score_label.pack(pady=20)

    def ask_question(self):
        if self.question_count < 5:
            self.current_question, self.answers = random.choice(list(self.questions.items()))
            self.correct_answer = self.answers[0]
            random.shuffle(self.answers)

            self.question_label.config(text=self.current_question)
            for i in range(4):
                self.answer_buttons[i].config(text=self.answers[i])
        else:
            self.show_score()
            self.master.update()  # 立即更新窗口
            self.master.after(1000, self.master.destroy)  # 等待3秒后关闭窗口

    def check_answer(self, index):
        selected_answer = self.answers[index]
        if selected_answer == self.correct_answer:
            self.score += 1
        self.question_count += 1
        self.ask_question()

    def show_score(self):
        self.question_label.config(text="Game Over")
        for button in self.answer_buttons:
            button.pack_forget()
        self.score_label.config(text=f"Your score: {self.score}/5")
        self.score_label.pack(pady=20) 
        
class GeographyGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Geography Game")
        self.master.geometry("1000x800")

        self.questions = {
            "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid"],
            "What is the currency of Japan?": ["Yen", "Dollar", "Euro", "Pound"],
            "What is the chemical symbol for water?": ["H2O", "CO2", "NaCl", "O2"],
            "What is the capital of China?": ["Beijing", "Shanghai", "Guangzhou", "Hong Kong"],
            "What is the capital of India?": ["New Delhi", "Mumbai", "Kolkata", "Chennai"]
        }

        self.current_question = None
        self.answers = None
        self.correct_answer = None
        self.score = 0
        self.question_count = 0

        self.create_widgets()
        self.ask_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.question_label.pack(pady=20)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.master, text="", font=("Helvetica", 16), width=20, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.answer_buttons.append(button)

        self.score_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.score_label.pack(pady=20)


    def ask_question(self):
        if self.question_count < 5:
            self.current_question, self.answers = random.choice(list(self.questions.items()))
            self.correct_answer = self.answers[0]
            random.shuffle(self.answers)

            self.question_label.config(text=self.current_question)
            for i in range(4):
                self.answer_buttons[i].config(text=self.answers[i])
        else:
            self.show_score()
            self.master.update()  # 立即更新窗口
            self.master.after(1000, self.master.destroy)  # 等待3秒后关闭窗口

    def check_answer(self, index):
        selected_answer = self.answers[index]
        if selected_answer == self.correct_answer:
            self.score += 1
        self.question_count += 1
        self.ask_question()

    def show_score(self):
        self.question_label.config(text="Game Over")
        for button in self.answer_buttons:
            button.pack_forget()
        self.score_label.config(text=f"Your score: {self.score}/5")
        self.score_label.pack(pady=20)

class SportsTriviaGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sports Trivia Game")
        self.master.geometry("1000x800")

        self.questions = {
            "Who is the winner of the 18th World Cup?": ["France", "Brazil", "Germany", "Italy"],
            "Which country's player is Crowe?": ["Portugal", "Argentina", "Brazil", "Spain"],
            "Who is called 'The Lord of the Rings' in basketball NBA?": ["Russell", "Jordan", "Bryant", "LeBron"],
            "Who was MLB's MVP in '21?": ["Ohtani Shohei", "Mike Trout", "Bryce Harper", "Jacob deGrom"],
            "Who won the champion of figure skating in 2014 and 2018 Olympics?": ["Hanyu Yuzuru", "Nathan Chen", "Yuna Kim", "Evgenia Medvedeva"]
        }

        self.current_question = None
        self.answers = None
        self.correct_answer = None
        self.score = 0
        self.question_count = 0

        self.create_widgets()
        self.ask_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.question_label.pack(pady=20)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.master, text="", font=("Helvetica", 16), width=20, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.answer_buttons.append(button)

        self.score_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.score_label.pack(pady=20)

    def ask_question(self):
        if self.question_count < 5:
            self.current_question, self.answers = random.choice(list(self.questions.items()))
            self.correct_answer = self.answers[0]
            random.shuffle(self.answers)

            self.question_label.config(text=self.current_question)
            for i in range(4):
                self.answer_buttons[i].config(text=self.answers[i])
        else:
            self.show_score()
            self.master.update()  # 立即更新窗口
            self.master.after(1000, self.master.destroy)  # 等待3秒后关闭窗口

    def check_answer(self, index):
        selected_answer = self.answers[index]
        if selected_answer == self.correct_answer:
            self.score += 1
        self.question_count += 1
        self.ask_question()

    def show_score(self):
        self.question_label.config(text="Game Over")
        for button in self.answer_buttons:
            button.pack_forget()
        self.score_label.config(text=f"Your score: {self.score}/5")
        self.score_label.pack(pady=20)





def main():
    runApp()

main()
