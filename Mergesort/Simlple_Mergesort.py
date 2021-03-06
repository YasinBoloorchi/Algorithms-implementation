def merge(A): 
	if len(A) >1: 
		mid = len(A)//2 
		L = A[:mid] 
		R = A[mid:] 

		merge(L) 
		merge(R) 

		i = j = k = 0
		
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				A[k] = L[i] 
				i+=1
			else: 
				A[k] = R[j] 
				j+=1
			k+=1

		while i < len(L): 
			A[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			A[k] = R[j] 
			j+=1
			k+=1

array = []
counter = 0
while True :
    counter +=1
    inputer = input("Please Enter Array number #{} (Press Enter To Exit) :".format(counter))
    if inputer == "":
        break
    array.append(int(inputer))

merge(array)
print(array)
input()
