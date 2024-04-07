from cmu_graphics import *

def onAppStart(app):
    app.width=800
    app.height=600

def redrawAll(app): 
    drawRect(100,100,100,100,fill='black')

    



def main():
    runApp()

main()