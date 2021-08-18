def merge_inversion(arr , r , q , n):
    n1 = q - r + 1
    n2 = n - q
    L , R = [] , []
    for i in range(n1-1):
        L.append(arr[r + i -1])

    for j in range(n2 , n):
        R.append(arr[q + j])
    print(L)
    print(R)

    k = r
    i , j = 0 , 0
    inversion = 0

    for k in range(n):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else :
            arr[k] = R[j]
            j += 1
            inversion += n1 - i + 1
    return inversion



def inversion_count(arr, r , n):
    inversion = 0
    if (r < n):
        q = int((r + n)/2)
        inversion += inversion_count(arr , r , q)
        inversion += inversion_count(arr,q+1,n)
        inversion += merge_inversion(arr , r ,q , n)
    return inversion

arr = [i for i in range(20)]

print(inversion_count(arr , 0 , len(arr)))
input()

# code written by Yasin Boloorchi. 
