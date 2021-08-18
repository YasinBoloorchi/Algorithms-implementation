# define an array
arr = [[1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]

# define a function to count and 
# show the selected activitis
def Activity_selector(arr):

    lenth = len(arr[0])

    # put the first activity in answer arr
    ans = [(arr[0][0],arr[1][0])]
    
    # set counter to 1 beacuse we dont count
    # the first array activity in the loop
    counter = 1

    # set the first activity of arr to the key
    key = 0


    # creat a loop to finde the next key
    # in the rest of the array
    for m in range(1,lenth):
        if arr[0][m] >= arr[1][key]:

            # append the selected activity to
            # answer array
            ans.append((arr[0][m],arr[1][m]))
            
            # add 1 to the activity selected counter
            counter +=1

            # set m activity to the key
            key = m

    # print selected activity
    print(ans)

    # return the activity selected counter
    return counter

print(Activity_selector(arr))

# code writen by Yasin Boloorchi
