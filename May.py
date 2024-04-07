from cmu_graphics import *
from PIL import Image
import os, pathlib

def onAppStart(app): 
    app.width=1000
    app.height=800
    app.backgroundImage = Image.open("hack112 image/background1.jpeg")
    

def redrawAll(app):
    drawPage1(app)
    # drawBackground1(app)

def drawPage1(app):
    # app.image = Image.open("images/Caaaaat.jpg")
    drawImage(app.backgroundImage,200,200,width=100,height=100)
    # textBox1 = CMUImage(Image.open('textbox1'))
    # drawImage(textBox1, 300, 300, width = 100, height = 100)
    
    

def main():
    runApp()

main()  
