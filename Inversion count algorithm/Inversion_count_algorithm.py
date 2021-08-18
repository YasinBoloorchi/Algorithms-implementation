arr = []
counter = 0
while True:
    temp = input("please enter arr[{}] (press enter for exit) :".format(counter))
    if temp == "":
        break
    else:
        arr.append(temp)
        counter += 1

counter = 0
for i in range (len(arr)):
    j = i
    for j in range(i+1 , len(arr)):
        if arr[i] > arr[j]:
            counter += 1
        j += 1

print(arr)
print("Tedade varoonegi : " , counter)
input()

# code written by Yasin Boloorchi. 