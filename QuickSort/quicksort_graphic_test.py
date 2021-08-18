from graphics import *
from time import *
from random import *

def graphical_it(arr,pivots,too_smalls,too_bigs,swaps):
    win = GraphWin("quickSort",1000,1000)

    rects = []
    texts = []


    def generate():
        x = 0
        y = 100
        for i in range(len(arr)):
            arr_i_index_data = arr[i] 
            r = Rectangle(Point(x,10),Point(y,100))
            r.setFill("white")
            d = Line(Point(x,10),Point(y,100))
            dc = d.getCenter()
            t = Text(dc ,"{}".format(arr_i_index_data))
            rects.append(r)
            texts.append(t)
            x += 100
            y += 100

    def draw_():
        for i in range(len(arr)):
            rects[i].draw(win)
            texts[i].draw(win)
            sleep(0.05)

    def change_text(first,second):
        sleep(1)
        texts[second].undraw()
        texts[first].undraw()
        sleep(0.5)
        t1 = texts[first].getText()
        t2 = texts[second].getText()
        texts[first].setText(t2)
        texts[second].setText(t1)
        texts[second].draw(win)
        texts[first].draw(win)
        

    def set_too_small(old,new):
        rects[old].setFill("white")
        rects[new].setFill("yellow")

    def set_too_big(old,new):
        rects[old].setFill("white")
        rects[new].setFill("yellow")

    def set_pivot(p):
        rects[p].setFill("blue")

    generate()
    draw_()
    s=0
    for i in range(len(pivots)):
        while s!="/":
            set_pivot(pivots[i])
            for tbl in range(len(too_bigs)):
                if too_bigs[tbl]=="/":
                    break
                elif tbl == 0:
                    tblm1 = too_bigs[tbl]
                elif too_bigs[tbl-1] == "/":
                    tblm1 = too_bigs[tbl-2]
                else:
                    tblm1 = too_bigs[tbl-1]
                set_too_big(tblm1,too_bigs[tbl])

            for tsl in range(len(too_smalls)-1):
                if tsl == 0:
                    tslm1 = too_smalls[tsl]
                elif too_smalls[tsl]=="/":
                    break
                else :
                    sleep(0.5)
                    if too_smalls[tsl-1] == "/":
                        tslm1 = too_smalls[tsl-2]
                    else:
                        tslm1 = too_smalls[tsl-1]
                    print(tslm1,too_smalls[tsl]) 
                    set_too_small(tslm1,too_smalls[tsl])
            sleep(0.5)
            change_text(swaps[s],swaps[s+1])
            s+=2

        


    change_text(2,5)

    win.getMouse()

arr = [3,4,5,1,5,6,9]
pivots = [0]
too_smalls = [6,5,4,3,"/",2,1]
too_bigs = [1,"/",2]
swaps = [1,3,0,1,"/"]


graphical_it(arr,pivots,too_smalls,too_bigs,swaps)
