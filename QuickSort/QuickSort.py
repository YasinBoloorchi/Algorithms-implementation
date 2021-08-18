from random import *
def partiotion(array , low , high):
    i = low(i-1)
    pivot = randint(low ,high)
    


def quicksort(array , low , high):
    if low < high:
        pi = partiotion(arr,low,high)
        quicksort(array, low, pi-1)
        quicksort(array, pi+1 , high)


arr = [2,4,6,8,12,8,6]

quicksort(arr , 0 , len(arr)-1)
