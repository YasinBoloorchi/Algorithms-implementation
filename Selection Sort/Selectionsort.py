def selectionsort(A):
    # Traverse through all array elements 
    for i in range(len(A)): 
        
        # Find the minimum element
        mini = i 
        for j in range(i+1, len(A)): 
            if A[mini] > A[j]: 
                mini = j 
                
        # Swap the first and the minimum  
        A[i], A[mini] = A[mini], A[i] 

    return A

array=[]
c=0
print("...:::SelectionSort:::...\nPlease Enter number's that have the same Digit's")
while True:
    inputer = input("Enter array index {} (Press Enter To Exit) :  ".format(c))
    c+=1
    if inputer=="":
        break
    else:
        array.append(inputer)

print(array)
print(selectionsort(array))
