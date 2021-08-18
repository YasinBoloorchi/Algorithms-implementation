import huffman
from tkinter import *

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

# finding the frequenci of
def find_frequenci(input_string):
    freq_arr = [[],[]]
    code_book = []

    # search all the string to find the frequenci of
    # any character in the file
    for letter in input_string:

        # if there was a char that's not in the frequenci
        # add it to the array and add a 1 for it's count
        # in the second dimantion
        if letter not in freq_arr[0]:
            freq_arr[0].append(letter)
            freq_arr[1].append(1)

        # if the character do exist in the array then just
        # add 1 to it's count
        else :
            for arr_index in range(len(freq_arr[0])):
                if freq_arr[0][arr_index] == letter:
                    freq_arr[1][arr_index] += 1
        
    # put all the char and their count to a dictionery
    for i in range(len(freq_arr[0])):
        code_book.append((freq_arr[0][i],freq_arr[1][i]))
            
    return code_book


# encrypt the string
def encrypt(input_string , haffman_table):
    coded = ""
    for char in input_string:
        coded += haffman_table[char]
    print(coded)
    return coded


# decrypt the string
def decrypt (encrypted_string , huffman_table):
    buffer = ""
    decrypted_string = ""
    for char in encrypted_string :
        buffer += char
        for key in huffman_table:
            if buffer == huffman_table[key]:
                print(key , end ="")
                decrypted_string += key
                buffer = ""
    return decrypted_string


# ==========================Grahical layer==================================

# creat a widow by tkinter module
win = Tk()
win.title("compresor")
win.maxsize(661,500)
win.minsize(661,500)

text_box = Text(win)
text_box.pack(side = 'left' , fill='y')
text_scrollbar = Scrollbar(win , command = text_box.yview)
text_scrollbar.pack(side = 'right' , fill = 'y')
text_box.config(yscrollcommand = text_scrollbar.set)

# define a global variable for table of huffman code
table = {}

def print_string():
    string = text_box.get("1.0",END)
    print(string)

# this function get the text from textbox and 
# give it to huffman algorithm to encrypt it and
# put the encrypted text in the text box 
def encrypt_string():
    global table 
    string = text_box.get("1.0",END)
    text_box.delete("1.0",END)
    code_book = find_frequenci(string)
    print("freq_arr :" , code_book)
    table = huffman.codebook(code_book)
    print("huffman :" , table)
    encrypted_string = encrypt(string , table)
    text_box.insert(END, encrypted_string)


# this function get the encrypted text from textbox and 
# encrypt it with the code table and finally put the 
# encrypted text in the text box 
def decrypt_string():
    global table
    string = text_box.get("1.0",END)
    text_box.delete("1.0",END)
    decrypted_string = decrypt(string , table)
    text_box.insert(END ,decrypted_string)


# this function open a window for user
# to open any file
def open_file():
    file_path = askopenfilename(filetypes = (("Text file" , "*.txt") , ("All Files" , "*.*")))
    print(file_path)
    selected_file = open(file_path , "r+")
    text_box.delete("1.0",END)

    for line in selected_file:
        text_box.insert(END ,line)


# a save function that can be added to the
#  program in the next version
def save_file():
    pass
    

# creat a menu bar for the master window 
# to add encrypt and other options to it
# for user to use
menubar = Menu(win)
win.config(menu = menubar)
filemenu = Menu(menubar,tearoff=0)
huffmanmenu = Menu(menubar,tearoff=0)

# file menu commands
filemenu.add_command(label = "Print" , command= print_string)
filemenu.add_separator()
filemenu.add_command(label = "Open" , command= open_file)
filemenu.add_command(label = "Save" , command= save_file)

# huffman menue commands
huffmanmenu.add_command(label = "Encrypt" , command= encrypt_string)
huffmanmenu.add_command(label = "Decrypt" , command= decrypt_string)

# add all the menus to the master window
menubar.add_cascade(label= "File" , menu=filemenu)
menubar.add_cascade(label= "Huffman Coding" , menu= huffmanmenu)


mainloop()