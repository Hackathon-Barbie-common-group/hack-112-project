from cmu_graphics import *
from PIL import Image
import os, pathlib

def onAppStart(app): 
    app.width=1000
    app.height=800
    app.backgroundImage = Image.open("image/background1.jpeg")
    app.backgroundImage = CMUImage(app.backgroundImage)
    app.sue = Image.open("photo/10.PNG")
    app.sue = CMUImage(app.sue)
    app.textBox1 = Image.open("image/textbox1.png")
    app.textBox1 = CMUImage(app.textBox1)
    

def redrawAll(app):
    drawPage1(app)
    # drawBackground1(app)

def drawPage1(app):
    
    drawImage(app.backgroundImage,0,0, width = 1000, height = 800)
    drawImage(app.sue, 100, 300, width = 200, height = 500)
    drawImage(app.textBox1, 200, 300)
    # drawLabel('112 is so hard, I wish that I could have a date.', 200, 300, fill = 'black', size = 50)
    # drawRect(200, 300, )
    
    

def main():
    runApp()

main()  
