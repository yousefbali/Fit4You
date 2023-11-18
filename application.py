import tkinter as tk
from tkinter import ttk

class ClothingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clothing Selector")

        self.add_button = ttk.Button(root, text="Add Item", command=self.open_options)
        self.add_button.pack()

        self.add_to_list_button = ttk.Button(root, text="Add to List", command=self.add_to_list)
        self.add_to_list_button.pack()

        self.listbox = tk.Listbox(root)
        self.listbox.pack()

        self.colors = ["White", "Black", "Red", "Green", "Blue", "Yellow"]
        self.types = ["Shoes", "Shirt", "Pants"]
        self.shades = ["Light", "Dark", "Regular"]

        self.color_var = tk.StringVar()
        self.type_var = tk.StringVar()
        self.shade_var = tk.StringVar()

        self.color_dropdown = ttk.Combobox(root, textvariable=self.color_var, values=self.colors, state="readonly")
        self.type_dropdown = ttk.Combobox(root, textvariable=self.type_var, values=self.types, state="readonly")
        self.shade_dropdown = ttk.Combobox(root, textvariable=self.shade_var, values=self.shades, state="readonly")

    def open_options(self):
        self.color_dropdown.pack()
        self.type_dropdown.pack()
        self.shade_dropdown.pack_forget()  # Initially hide the shade dropdown

        # Add trace to color dropdown to handle the visibility of shade dropdown
        self.color_var.trace('w', self.toggle_shade_dropdown)

    def toggle_shade_dropdown(self, *args):
        color = self.color_var.get()
        if color not in ["White", "Black"]:
            self.shade_dropdown.pack()
        else:
            self.shade_dropdown.pack_forget()

    def add_to_list(self):
        color = self.color_var.get()
        type_ = self.type_var.get()
        shade = self.shade_var.get()

        if color and type_:
            item = f"{color} {type_}"
            if color not in ["White", "Black"]:
                item += f" ({shade})"
            self.listbox.insert(tk.END, item)

# Create the main window
root = tk.Tk()
app = ClothingApp(root)
root.mainloop()
