from graphics import *
from time import *
from random import *

class graphical_it():
    rects = []
    texts = []

    def __init__(self,arr):
        self.arr = arr
        self.win = GraphWin("quickSort",1000,200)

    def generate(self):
        x = 0
        y = 100

        for i in range(len(self.arr)):

            arr_i_index_data = self.arr[i] 
            r = Rectangle(Point(x,10),Point(y,100))
            r.setFill("white")
            d = Line(Point(x,10),Point(y,100))
            dc = d.getCenter()
            t = Text(dc ,"{}".format(arr_i_index_data))
            graphical_it.rects.append(r)
            graphical_it.texts.append(t)
            x += 100
            y += 100


    def draw_(self):
        graphical_it.generate(self)
        print("draw rects : ", graphical_it.rects)
        print("draw texts : ", graphical_it.texts)
        for i in range(len(arr)):
            graphical_it.rects[i].draw(self.win)
            graphical_it.texts[i].draw(self.win)
            sleep(0.05)


    def change_text(self,first,second):
        sleep(1)
        graphical_it.texts[second].undraw()
        graphical_it.texts[first].undraw()
        sleep(0.5)
        t1 = graphical_it.texts[first].getText()
        t2 = graphical_it.texts[second].getText()
        graphical_it.texts[first].setText(t2)
        graphical_it.texts[second].setText(t1)
        graphical_it.texts[second].draw(self.win)
        graphical_it.texts[first].draw(self.win)

        

    def set_too_small(self,old,new):
        graphical_it.rects[old].setFill("white")
        graphical_it.rects[new].setFill("yellow")

    def set_too_big(self,old,new):
        graphical_it.rects[old].setFill("white")
        graphical_it.rects[new].setFill("yellow")

    def set_pivot(self,old,new):
        graphical_it.rects[old].setFill("white")
        graphical_it.rects[new].setFill("blue")



arr = [3,5,7,1,8,9,0,4,6]
G = graphical_it(arr)
G.draw_()
sleep(0.3)
G.set_pivot(0,0)
sleep(0.5)
G.set_pivot(0,3)
G.set_too_big(1,1)
G.set_too_small(6,6)
sleep(1)
G.set_too_big(1,2)
G.set_too_small(6,5)
G.change_text(1,3)
G.change_text(2,5)