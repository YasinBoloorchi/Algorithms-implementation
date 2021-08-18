string = input("pleas Enter your string : ")
# ['', 'a', '', 'z', '', 'i', '', 'z', '', 'i', '', 'e', '', 'l']
# ['0','1','2', '3', '4','5', '6','7', '8','9','10','11','12','13']

def MPS(string):
    listed_string = list(string)
    mps = 0
    final_max = 0 
    first_letter = 0
    last_letter = 0
    listed_string2 = []
    lenth = len(listed_string)

    for i in range(lenth):
        listed_string2.append("")
        listed_string2.append(listed_string[i])

    lenth2 = len(listed_string2)
    print(listed_string2)

    for i in range(lenth2):
        c = 1
        temp_mps = 0
        while True:
            # print("\n\ni = {} ===> " .format(i) , listed_string2[i])
            if i-c >=0 and i+c<lenth2:
                # print("i-1 : " , i-c  , listed_string2[i-c])
                # print("i+1 : " , i+c , listed_string2[i+c])
                # print("if 1 ok")
                if listed_string2[i-c] == listed_string2[i+c]:
                    # print("if 2 ok ")
                    temp_mps += 1
                    # print("temp mps = " , temp_mps)
                    temp_first_letter = i-c
                    temp_last_letter = i+c
                    # print("sting ========> " , string[first_letter:last_letter+1])
                    c += 1
                    if temp_mps > mps:
                        first_letter = temp_first_letter
                        last_letter = temp_last_letter
                        mps = temp_mps
                else:
                    c += 1
                    break
            else:
                c += 1
                break
        # print("max till now : " , mps)

    print("maximum substring :" , end=" ")
    for i in range(first_letter, last_letter+1):
        if listed_string2[i] != "" :
            final_max +=1
            print(listed_string2[i],end="")
    print("\nmaximum substring lenth : " , final_max)

    return final_max , first_letter , last_letter
        

ans = MPS(string)
input()

# code written by Yasin Boloorchi. 
