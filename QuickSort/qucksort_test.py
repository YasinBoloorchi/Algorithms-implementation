def partition(arr,low,high):
    too_big = 1
    print("0_too_big : " , too_big)
    
    too_small = high
    print("0_too_small : ", too_small)
    
    pivot = low
    print("0_pivot : ",pivot)
    while too_small < too_big:

        while arr[too_big] <= arr[pivot]:
            too_big +=1
            print("0_too_big : " , too_big)

        
        while arr[too_small] > arr[pivot]:
            too_small -=1
            print("0_too_small : " , too_small)
        
        if too_big < too_small:
            arr[too_big] , arr[too_small] = arr[too_small] , arr[too_big]
    
        arr[too_small] , arr[pivot] = arr[pivot] , arr[too_small]

        # print(arr)
        # print("it will return : ", too_small)

        return too_small


def quicksort(arr,low,high):
    if low < high:
        p = partition(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)



array =[3,5,7,1,2,9]

quicksort(array,0,len(array)-1)

print(array)