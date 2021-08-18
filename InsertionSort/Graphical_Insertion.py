from time import *
from random import *
from graphics import *

lisst = []

for i in range(10):
    lisst_temp = input("Please Enter array[{}] : ".format(i))
    if lisst_temp == "":
        break
    else:
        lisst.append(int(lisst_temp))


class graphical_it():
    rects = []
    texts = []
    old_pivot = -100
    old_too_big = -100
    old_too_small = -100
    
    def __init__(self,arr):
        self.arr = arr
        self.win = GraphWin("Insertion Sort",1000,120)

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
        for i in range(len(self.arr)):
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

        

    def set_too_small(self,new):
        if graphical_it.old_too_small== -100:
            graphical_it.rects[new].setFill("white")
        else:
            graphical_it.rects[graphical_it.old_too_small].setFill("white")
        
        graphical_it.rects[new].setFill("yellow")

        graphical_it.old_too_small=new

    def set_too_big(self,new):
        if graphical_it.old_too_big == -100:
            graphical_it.rects[new].setFill("white")
        else:
            graphical_it.rects[graphical_it.old_too_big].setFill("white")
        
        graphical_it.rects[new].setFill("yellow")

        graphical_it.old_too_big=new

    def set_pivot(self,new):
        if graphical_it.old_pivot == -100:
            graphical_it.rects[new].setFill("white")
        else:
            graphical_it.rects[graphical_it.old_pivot].setFill("white")
        graphical_it.rects[new].setFill("blue")
        graphical_it.old_pivot=new

    def set_blue(self, index):
        graphical_it.rects[index].setFill("blue")

    def set_yellow(self, index):
        graphical_it.rects[index].setFill("yellow")

    def set_white(self, index):
        graphical_it.rects[index].setFill("white")

    def set_green(self, index):
        graphical_it.rects[index].setFill("green")
    
    def get_mouse(self):
        self.win.getMouse()



G = graphical_it(lisst)
G.draw_()

for j in range(1 ,len(lisst)):
    key = lisst[j]
    G.set_blue(j)

    i = j - 1
    G.set_too_small(i)
    sleep(0.3)

    while i >= 0 and lisst[i]>key:
        lisst[i+1] = lisst[i]
        G.change_text(i,i+1)
        G.set_white(i+1)
        G.set_blue(i)
        sleep(0.2)
        if i>0:
            G.set_yellow(i-1)
            sleep(1)
        i -= 1
        sleep(0.2)


    if j==(len(lisst)-1):
        for k in range(len(lisst)):
            G.set_white(k)
        sleep(0.3)
        for k in range(len(lisst)):
            G.set_green(k)
            sleep(0.05)
            
    else:   
        for h in range(j-1):
            G.set_white(h)
    lisst[i+1] = key
    print(lisst)

G.get_mouse()

