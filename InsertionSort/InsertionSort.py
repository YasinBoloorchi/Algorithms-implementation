from random import *

lisst = list(range(8))
shuffle(lisst)

for j in range(1 ,len(lisst)):
    key = lisst[j]
    i = j - 1
    
    while i >= 0 and lisst[i]>key:
        lisst[i+1] = lisst[i]

        i -= 1

    lisst[i+1] = key
    print(lisst)

input()