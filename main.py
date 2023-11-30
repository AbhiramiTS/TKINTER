from tkinter import *

# Create the main window
window = Tk()
window.title("My GUI Program")
window.minsize(width=1000, height=500)

# Create a label
my_label = Label(text="My Label", font=("Arial", 24, "bold"))
my_label.pack()

# Configure the label with new text
my_label.config(text="New Label")

# Function to handle button click
def button_clicked():
    new_text = entry.get()
    my_label.config(text=new_text)

# Create a button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entries
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")  # Add some initial text
print(entry.get())  # Gets text in entry
entry.pack()

# Text
text = Text(height=5, width=30)
text.focus()  # Puts cursor in the textbox
text.insert(END, "Example of multi-line text entry.")  # Adds some initial text
print(text.get("1.0", END))  # Get the current value in textbox at line 1, character 0
text.pack()

# Spinbox
def spinbox_used():
    print(spinbox.get())  # Gets the current value in spinbox

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
def scale_used(value):
    print(value)  # Called with the current scale value

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbutton_used():
    print(checked_state.get())  # Prints 1 if On button checked, otherwise 0

checked_state = IntVar()  # Variable to hold the checked state, 0 is off, 1 is on
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())  # Variable to hold which radio button value is checked

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))  # Gets the current selection from the listbox

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Start the main event loop
window.mainloop()
