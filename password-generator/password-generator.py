# importing the tkinter module
from tkinter import *

# importing the pyperclip module to use it to copy our generated 
# password to clipboard
import string
import pyperclip

# random module will be used in generating the random password
import random

# initializing the tkinter
root = Tk()

# setting the width and height of the gui
root.geometry("400x400")    # x is small case here

# declaring a variable of string type and this variable will be 
# used to store the password generated
passstr = StringVar()

# declaring a variable of integer type which will be used to 
# store the length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)


# function to generate the password
def generate():
    # storing the keys in a list which will be used to generate 
    # the password 
    pass1 = string.ascii_lowercase
    pass2 = string.ascii_uppercase
    pass3 = string.digits
    pass4 = string.punctuation
    pass5 = [pass1, pass2, pass3, pass4]

    # declaring the empty string
    password = ""
    m=""
    k=""
    # loop to generate the random password of the length entered           
    # by the user
    a=passlen.get()
    for x in range(a-4):
        m = m + random.choice(pass1+pass2+pass3+pass4)
    # selecting atleast 1 lowercase, 1 uppercase, 1 digit and 1 special character
    for i in range(4):
        b=random.choice(pass5)
        k = k + random.choice(b)
        pass5.remove(b)
    # selecting the index in between at which we will join all these 4 characters 
    y=random.randint(0,a-4)

    password=m[0:y]+k+m[y:]
    
    # setting the password to the entry widget
    passstr.set(password)

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# Creating a text label widget
Label(root, text="Password Generator Application", font="calibri 20 bold").pack()

# Creating a text label widget
Label(root, text="Enter password length").pack(pady=3)

# Creating a entry widget to take password length entered by the 
# user
Entry(root, textvariable=passlen).pack(pady=3)

# button to call the generate function
Button(root, text="Generate Password", command=generate).pack(pady=7)

# entry widget to show the generated password
Entry(root, textvariable=passstr).pack(pady=3)

# button to call the copytoclipboard function
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()

# mainloop() is an infinite loop used to run the application when 
# it's in ready state 
root.mainloop()