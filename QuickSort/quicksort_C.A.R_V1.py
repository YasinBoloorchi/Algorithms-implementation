from random import *
def partition(arr,low,high,print_value):
    pivot = arr[low]
    too_big= low+1
    too_small= high 

    if print_value == 1:
        print("[",end="")

        for h in range(low,high+1):
            print(arr[h],end=",")
            print("]")

        print("\npivot :", pivot)
        print("too_big:",too_big)
        print("too_small:",too_small)


    while True:
        while too_big <= too_small and arr[too_big] <= pivot:
            too_big += 1
            if print_value == 1 :
                print("too_big:",too_big)

        while arr[too_small] >= pivot and too_small >= too_big:
            too_small -=1
            if print_value == 1 :
                print("too_small:",too_small)

        if too_small < too_big:
            break
        else:
            if print_value == 1 :
                print("array [too_big] : " ,arr[too_big])
                print("array [too_small] : " ,arr[too_small])
            arr[too_big],arr[too_small] = arr[too_small],arr[too_big]
            
            if print_value == 1 :
                print(arr)
    if print_value == 1 :
        print("array [too_small] : " , arr[too_small])
        print("array [pivot] : " , arr[low])
    arr[too_small],arr[low] = arr[low],arr[too_small]
    return too_small


def quicksort(arr,low,high,print_value):
    if low < high:
        p = partition(arr,low, high,print_value)
        quicksort(arr,low,p-1,print_value)
        quicksort(arr,p+1,high,print_value)


def user_insert():
    array = []
    counter = 0
    while True:
        array_temp = input("pleas Enter array[{}] : ".format(counter))
        if array_temp == "":
            break
        else:
            array.append(int(array_temp))
            counter += 1
    print("Input array is : " , array)
    quicksort(array,0,len(array)-1,1)
    print("Sorted array is : " , array)
    input()


def testing():
    print("....::::TESTING SORT ALGORITHM::::....")
    test_case_size = int(input("please enter size of test cases : "))
    number_of_test_cases = int(input("please enter number of test cases : "))

    miss = 0
    for j in range(number_of_test_cases):
        arr = []
        for i in range(test_case_size):
            arr.append(randint(0,99))
        print("Input array : " , arr)
        quicksort(arr,0,len(arr)-1,0) 
        print("Sorted array :",arr)
        for h in range(len(arr)-1):
            if arr[h]>arr[h+1]:
                miss +=1
    if miss > 0:
        print("number of fault : {}".format(miss))
    else :
        print("Code Runed Perfectly!")
    input()

option = "empty"
while option != 1 or option!= 2 :
    print("..:::Hello Welcome To quicksort Algorithm Test and try:::..")
    print("\nPlease Enter one of our options \n1.Testing \n2.Try algorithm by insert an array")
    option = int(input(">>> "))
    if option == 1:
        testing()
        break
    elif option == 2:
        user_insert()
        break

