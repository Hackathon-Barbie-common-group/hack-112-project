from cmu_graphics import *
from PIL import Image
import os, pathlib

def loadSound(relativePath):
    absolutePath = os.path.abspath(relativePath)
    url = pathlib.Path(absolutePath).as_uri()
    return Sound(url)

def onAppStart(app): 
    app.width=1000
    app.height=800
    app.page1=True
    app.page2=True
    app.page3=True
    app.page4=True
    app.page5=True
    app.backgroundImage = Image.open("image/background1.jpeg")
    app.backgroundImage = CMUImage(app.backgroundImage)
    app.sue = Image.open("photo/10.PNG")
    app.sue = CMUImage(app.sue)
    app.textBox1 = Image.open("photo/texbox1.png")
    app.textBox1 = CMUImage(app.textBox1)
    app.backgroundImage2 = Image.open('photo/background2')
    app.backgroundImage2 = CMUImage(app.backgroundImage2)
    app.coffeeBackground = Image.open('photo/coffeeBackground')
    app.coffeeBackground = CMUImage(app.coffeeBackground)
    app.sueFinal = Image.open('photo/suefinals.PNG')
    app.sueFinal = CMUImage(app.sueFinal)
    app.background4 = Image.open('photo/background4.png')
    app.background4 = CMUImage(app.background4)
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
    app.sound1 = loadSound("sounds/weddingSong.mp3")
    app.sound1.play(restart = True)
   

def redrawAll(app):
    if app.page1:
        drawPage1(app)
    elif app.page2: 
        drawPage2(app)
    elif app.page3: 
        drawPage3(app)
    elif app.page4:
        drawPage4(app)
    elif app.page5:
        drawPage5(app)
    
   

def drawPage1(app):
    drawImage(app.backgroundImage,0,0, width = 1000, height = 800)
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
    
    drawRect(700, 650, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 800, 700, fill = 'white', size = 30)
    
def drawPage2(app): 
    drawImage(app.coffeeBackground, 0, 0, width = 1000, height = 800)
    drawImage(app.sue, 100, 300, width = 200, height = 500)
    text = '''
        It's carnival soon, 
        I could make a pizza for my boy'''
    
    drawImage(app.textBox1, 550, 412, align = 'center', width = 500, height = 300)
    lines = text.splitlines()
    for i in range (len(lines)):
        line = lines[i]
        drawLabel(line, 500, 350 + i + i * 30, size = 15, fill = 'black', font= 'monospace')
    
    drawRect(700, 650, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 800, 700, fill = 'white', size = 30)

def drawPage3(app): 
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
    drawRect(700, 650, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 800, 700, fill = 'white', size = 30)    
    instruction = '''
              Remember that each boy has a different ideal type?
              Try to put on the best fit for you boy
              to get that boy fall for you! 
              '''
    instructionLines = instruction.splitlines()
    for i in range (len(instructionLines)):
        instructionLine = instructionLines[i]
        drawLabel(instructionLine, 400, 100 + i * 30, size = 30, fill = 'darkGreen', bold = True, font = 'monospace')

def drawPage4(app):
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
    drawRect(700, 650, 200, 100, fill = 'pink', opacity = 80, border = 'lightCoral', borderWidth = 10)
    drawLabel('Continue', 800, 700, fill = 'white', size = 30) 
    

def drawPage5(app): 
    drawImage(app.wedding, 0, 0, width = 1000, height = 800)
    drawImage(app.sue, 300, 300, width = 200, height = 500)


def onMousePress(app,mouseX,mouseY): 
    if 700<=mouseX<=900 and 650<=mouseY<=750: 
        if app.page1: 
            app.page1=False
        elif app.page2: 
            app.page2=False
        elif app.page3: 
            app.page3=False
        elif app.page4: 
            app.page4=False
        elif app.page5: 
            app.page5=False


def main():
    runApp()

main()  
