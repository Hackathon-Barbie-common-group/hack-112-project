from cmu_graphics import *
from PIL import Image
import os, pathlib

def onAppStart(app): 
    app.width=1000
    app.height=800
    app.page1=False
    app.page2=False
    app.page3=True
    app.backgroundImage = Image.open("image/background1.jpeg")
    app.backgroundImage = CMUImage(app.backgroundImage)
    app.sue = Image.open("photo/10.PNG")
    app.sue = CMUImage(app.sue)
    app.textBox1 = Image.open("photo/texbox1.png")
    app.textBox1 = CMUImage(app.textBox1)
    app.backgroundImage2 = Image.open('photo/background2')
    app.backgroundImage2 = CMUImage(app.backgroundImage2)
    # app.textBox = Image.open('photo/textbox1.PNG')
    # app.textBox = CMUImage(app.textBox)
    app.coffeeBackground = Image.open('photo/coffeeBackground')
    app.coffeeBackground = CMUImage(app.coffeeBackground)
    app.sueFinal = Image.open('photo/suefinals.PNG')
    app.sueFinal = CMUImage(app.sueFinal)
    app.background4 = Image.open('photo/background4.png')
    app.background4 = CMUImage(app.background4)
    
    
def redrawAll(app):
    if app.page1:
        drawPage1(app)
    elif app.page2: 
        drawPage2(app)
    elif app.page3: 
        drawPage3(app)
    
   

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




def onMousePress(app,mouseX,mouseY): 
    if 700<=mouseX<=900 and 650<=mouseY<=750: 
        if app.page1: 
            app.page1=False
        elif app.page2: 
            app.page2=False
        elif app.page3: 
            app.page3=False

def main():
    runApp()

main()  
