'''
Random Key Generator using Python
Author: Fatih Ünal
'''

# import the necessary modules!
import random
from tkinter import *
from tkinter.ttk import *
import string


def Key_generate():
	entry.delete(0, END)
	length = var1.get()
	password = ""

	# low key generator
	if var.get() == 0:
		letters = string.ascii_lowercase + string.ascii_uppercase
		password = password.join(random.choice(letters) for i in range(length))
		return password

	# medium key generator
	elif var.get() == 1:
		letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
		password = password.join(random.choice(letters) for i in range(length))
		return password

	# strong key generator
	elif var.get() == 2:
		letters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
		password = password.join(random.choice(letters) for i in range(length))
		return password
	else:
		print("Please choose an option")

def generate():
	password1 = Key_generate()
	entry.insert(10, password1)

#Create Tkinter GUI window
root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Key Generator")
root.geometry("400x50")

Random_key = Label(root, text="Key")
Random_key.grid(row=0)

entry = Entry(root)
entry.grid(row=0, column=1)

len = Label(root, text="Length")
len.grid(row=1)

g_button = Button(root, text="Generate", command=generate)
g_button.grid(row=0, column=2)

r_low = Radiobutton(root, text="Low", variable=var, value=0)
r_low.grid(row=1, column=2, sticky='E')

r_middle = Radiobutton(root, text="Medium", variable=var, value=1)
r_middle.grid(row=1, column=3, sticky='E')

r_strong = Radiobutton(root, text="Strong", variable=var, value=2)
r_strong.grid(row=1, column=4, sticky='E')


comb = Combobox(root, textvariable=var1)
comb['values'] = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
comb.current(0)
comb.bind('<<ComboboxSelected>>')
comb.grid(column=1, row=1)

root.mainloop()



