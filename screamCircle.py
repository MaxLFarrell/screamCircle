import PIL
from pygame import mixer
from graphics import *
mixer.init()
mixer.music.load('hell-Mike_Koenig-144950046.wav')
mixer.music.play()

def main():
    win = GraphWin("My Circle",500,500)
    c=Circle(Point(250,250),200)
    c.setFill("white")
    c.draw(win)
    win.getMouse()
    win.close()

main()



