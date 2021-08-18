from random import *
#binary search in python 
function_counter = 0

# Returns index of x in arr if present, else -1 
def binarySearch (array, l, r, x, function_counter): 
    if r >= l: 
        mid = l + (r - l)//2
        
        #it's obvious what i did :)) so no coments need 
        if array[mid] == x: 
            function_counter += 1
            return mid , function_counter

        elif array[mid] > x: 
            function_counter += 1
            return binarySearch(array, l, mid-1, x, function_counter) 
        else:     
            
            return binarySearch(array, mid + 1, r, x, function_counter)
            
    else: 
        return -1
        


#creat an array for binary serach purpose
array = []
for  i in range(100,200):
    array.append(i)

#get an int to search it in  our array
x = int(input("""We have 100 number Between 100 and 200.
so help your self and search our array :)  : """))

# Function call
result , counter = binarySearch(array, 0, len(array)-1, x, 0)

if result != -1: 
    print ("Element is present at index {}".format(result))
    print ("Number of compares : {}".format(counter))

else: 
    print ("Element is not present in array")