from random import *
def quickSort(arr,low,high):
    if low<high:
        p = partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)

def partition(arr,low,high):
    pivot = arr[low]
    too_big = low+1
    too_small = high

    while True:
        while too_big <= too_small and arr[too_big] <= pivot:
            too_big += 1

        while arr[too_small] >= pivot and too_small >= too_big:
            too_small -= 1

        if too_small < too_big:
            break
        else:
            arr[too_big] , arr[too_small] = arr[too_small] , arr[too_big]
        
    arr[low] , arr[too_small] = arr[too_small], arr[low]

    return too_small

def testing():
    ridi = 0
    for j in range(100):
        arr = []
        for i in range(100):
            arr.append(randint(0,99))
        quickSort(arr,0,len(arr)-1) 
        # print(arr)
        for h in range(len(arr)-1):
            if arr[h]>arr[h+1]:
                ridi +=1
                # print(arr[h])

    print("+chanta ridi?")
    if ridi == 0 :
        print("Hichi badbakht")
    else :
        print("{} ta".format(ridi))


testing()