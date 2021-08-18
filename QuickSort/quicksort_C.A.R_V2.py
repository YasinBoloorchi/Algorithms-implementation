from random import *
from graphics import *
from time import *

arr = [59,34,12,34,65,87,90]
class graphical_it():
    rects = []
    texts = []
    old_pivot = -100
    old_too_big = -100
    old_too_small = -100
    
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


G = graphical_it(arr)
G.draw_()

def partition(arr,low,high):
    pivot = arr[low]
    too_big= low+1
    too_small= high 
    G.set_pivot(low)
    G.set_too_big(too_big)
    G.set_too_small(too_small)
    print("[",end="")
    for h in range(low,high+1):
       print(arr[h],end=",")
    print("]")

    print("\np :", pivot)
    print("too_big:",too_big)
    print("too_small:",too_small)


    while True:
        while too_big <= too_small and arr[too_big] <= pivot:
            too_big += 1
            G.set_too_big(too_big)
            sleep(1)

            print("too_big:",too_big)
        while arr[too_small] >= pivot and too_small >= too_big:
            too_small -=1
            G.set_too_small(too_small)
            sleep(1)
            print("too_small:",too_small)
        if too_small < too_big:
            break
        else:
            print("a [too_big] : " ,arr[too_big])
            print("a [too_small] : " ,arr[too_small])
            arr[too_big],arr[too_small] = arr[too_small],arr[too_big]
            G.change_text(too_big,too_small)
            sleep(1)
            print(arr)

    print("a[too_small] : " , arr[too_small])
    print("a[p] : " , arr[low])
    arr[too_small],arr[low] = arr[low],arr[too_small]
    G.change_text(too_small,low)
    sleep(1)
    return too_small


    
def quicksort(arr,low,high):
    if low < high:
        p = partition(arr,low, high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)

def testing():
    miss = 0
    for j in range(1):
        arr = []
        for i in range(5):
            arr.append(randint(0,99))
        print("Input array : " , arr)
        quicksort(arr,0,len(arr)-1) 
        print("Sorted array :",arr)
        for h in range(len(arr)-1):
            if arr[h]>arr[h+1]:
                miss +=1
                # print(arr[h])
    if miss > 0:
        print("number of fault : {}".format(miss))
    else :
        print("Code Runed Perfectly!")

# testing()

quicksort(arr,0,len(arr)-1)
print("sorted array is :" , arr)

sleep(1)