from cmu_graphics import *
from PIL import Image

class Pizza: 
    def __init__(self): 
        self.time=0

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

class A: 
    def __init__(self): 
        self.well=None

class B: 
    def __init__(self): 
        self.well=None

class C: 
    def __init__(self): 
        self.well=None

class D: 
    def __init__(self): 
        self.well=None

pizza=Pizza()

def onAppStart(app):
    app.width=1000
    app.height=800
    app.stepsPerSecond=1
    app.base=True
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
    app.dress=[clo.unidress,clo.cutedress,clo.sexydress,clo.elegdress]
    app.dress2=None
    app.shirt=[clo.unishirt,clo.cuteshirt,clo.sexyshirt,clo.elegshirt]
    app.shirt2=None
    app.shoes=[clo.unishoes,clo.cuteshoes,clo.sexyshoes,clo.elegshoes]
    app.shoes2=None

def redrawAll(app): 
    drawRect(900,700,100,100,align='center',fill='black')
    if app.base:
        drawImage(app.basecake,500,300,width=500,height=500,align='center')
        for i in range(3):
            drawImage(app.ingre[i],110+300*i,650,width=100,height=100)
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
            drawLabel(f'Eveness: {app.distribution}',135,100,size=35) 
        elif app.score!=[]:
            drawLabel(f'Accuracy: {100-sum(app.result)//8}',135,50,size=35)
            drawLabel(f'Eveness: None',135,100,size=35) 
    else: 
        drawRect(0,0,1000,800,fill='black')
        drawImage(CMUImage(Image.open('Naked.png')),150,110,width=150,height=450)
        if clo.dress==None:
            drawImage(CMUImage(Image.open('skirt.png')),500,110,width=450,height=600)
        elif clo.shirt==None: 
            drawImage(clo.dress,230,425,width=135,height=110,align='center')
            drawImage(CMUImage(Image.open('clothes.png')),500,110,width=450,height=600)
        elif clo.shoes==None: 
            drawImage(clo.dress,230,425,width=135,height=110,align='center')
            drawImage(clo.shirt,220,325,width=150,height=125,align='center')
            drawImage(CMUImage(Image.open('shoes.png')),500,110,width=450,height=600)
        else:
            drawImage(clo.dress,230,425,width=135,height=110,align='center')
            drawImage(clo.shirt,220,325,width=150,height=125,align='center')
            drawImage(clo.shoes,230,560,width=100,height=110,align='center')

            
        
def onMouseDrag(app, mouseX, mouseY):
    if app.base: 
        app.cx = mouseX
        app.cy = mouseY
        if 110<=app.cx<=210 and 600<=app.cy<=700: 
            app.curr1=app.ingre[0]
        elif 410<=app.cx<=510 and 600<=app.cy<=700: 
            app.curr1=app.ingre[1]
        elif 710<=app.cx<=810 and 600<=app.cy<=700: 
            app.curr1=app.ingre[2]
    

def distance(x0,y0,x1,y1): 
    return int(((x1-x0)**2+(y0-y1)**2)**0.5)

def onMousePress(app,mouseX,mouseY): 
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
        print(clo.shirt)
    elif clo.dress!=None and clo.shirt!=None and clo.shoes==None: 
        app.fx = mouseX
        app.fy = mouseY
        if 110<=app.fx<=210 and 560<=app.fy<=680: 
            app.curr4=app.shoes[0]
        elif 310<=app.fx<=410 and 600<=app.fy<=700: 
            app.curr4=app.shoes[1]
        elif 510<=app.fx<=690 and 600<=app.fy<=750: 
            app.curr4=app.shoes[2]
        elif 800<=app.fx<=870 and 400<=app.fy<=560: 
            app.curr4=app.shoes[1]
        clo.shoes=app.curr4
    if 850<=mouseX<=950 and 650<=mouseY<=750: 
        if app.base: 
            app.base=False

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

def onStep(app): 
    if app.stove: 
        pizza.time+=1  

def stove(app): 
    if app.stove: 
        pizza.time+=1

def onKeyPress(app,keys): 
    if keys=='space': 
        app.stove=not app.stove 

def main():
    runApp()

main()