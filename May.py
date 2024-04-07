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
    app.textBox1 = Image.open("photo/textbox1.PNG")
    app.textBox1 = CMUImage(app.textBox1)
    
    

def redrawAll(app):
    drawPage1(app)
    # drawBackground1(app)

def drawPage1(app):
    
    drawImage(app.backgroundImage,0,0, width = 1000, height = 800)
    drawImage(app.sue, 100, 300, width = 200, height = 500)
    imageWidth, imageHeight = getImageSize(app.textBox1)
    print(imageWidth, imageHeight)
    drawImage(app.textBox1, 300, 350, width = 280, height = 100)

    

def main():
    runApp()

main()  
