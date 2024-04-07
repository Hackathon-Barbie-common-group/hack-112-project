from cmu_graphics import *
from PIL import Image
import os, pathlib

def onAppStart(app): 
    app.width=1000
    app.height=800
    app.backgroundImage = Image.open("photo/background3")
    app.backgroundImage = CMUImage(app.backgroundImage)
    app.Char1=Image.open('photo/2.PNG')
    app.Char1=CMUImage(app.Char1)
    app.Char2=Image.open('photo/3.PNG')
    app.Char2=CMUImage(app.Char2)
    app.Char3=Image.open('photo/6.PNG')
    app.Char3=CMUImage(app.Char3)
    app.Char4=Image.open('photo/8.PNG')
    app.Char4=CMUImage(app.Char4)
    app.canDrawChar1=False
    app.canDrawChar2=False
    app.canDrawChar3=False
    app.canDrawChar4=False
    

def redrawAll(app):
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
    drawLabel('Ideal Type: Lady Type',800,500,size=30,fill='white',font='monospace')

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
    # app.image = Image.open("images/Caaaaat.jpg")
    drawImage(app.backgroundImage,0,0, width = 1000, height = 800)
    # textBox1 = CMUImage(Image.open('textbox1'))
    # drawImage(textBox1, 300, 300, width = 100, height = 100)

def drawPage2Buttons(app):
    for i in range(4):
        startLeft=150+200*i
        startTop=100
        drawRect(startLeft,startTop,100,100,fill=None,border='midnightBlue',borderWidth=5)
        drawLabel(i+1,startLeft+50,startTop+50,fill='midnightBlue',size=40,bold=True)
    drawLabel('Press Button to Have a Closer look of Your Boys', 500,50,size=32,fill='navy',font='monospace',bold=True)

def onMousePress(app,mouseX,mouseY):
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

def main():
    runApp()

main()


from cmu_graphics import *
from PIL import Image
import os, pathlib

def onAppStart(app): 
    app.width=1000
    app.height=800
    app.backgroundImage = Image.open("photo/pizzaBackground")
    app.backgroundImage = CMUImage(app.backgroundImage)

def redrawAll(app):
    drawBG(app)

def drawBG(app):
    drawImage(app.backgroundImage,0,0, width = 1000, height = 800)
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

#def onMousePress(app,mouseX,mouseY):
    #if 400<=mouseX<=550 and 375<=mouseY<=500:
    #
    #elif 600<=mouseX<=750 and 375<=mouseY<=500:
    #
    #elif 400<=mouseX<=550 and 550<=mouseY<=700:
    #
    #elif 600<=mouseX<=750 and 550<=mouseY<=700:

def main():
    runApp(app)

main()