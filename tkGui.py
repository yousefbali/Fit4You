# Import module 
from tkinter import *

# Create object 
root = Tk() 

# Adjust size 
root.geometry( "500x500" ) 

# Change the label text 
def show(): 
	label.config( text = clicked.get() ) 

# Dropdown menu options 
options = [ 
	"Red", 
	"Orange", 
	"Yellow", 
	"Green", 
	"Blue", 
	"Indigo", 
	"Violet",
	"White",
	"Black",
	"Grey",
	"Tan",
	"Beige",
]

# datatype of menu text 
clicked = StringVar() 

# initial menu text 
clicked.set( "Colors" ) 

# Create Dropdown menu 
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 

# Create button, it will change label text 
button = Button( root , text = "Search" , height = 3, width = 5 ).pack() 

# Create Label 
label = Label( root , text = " " ) 
label.pack() 

# Execute tkinter 
root.mainloop() 
