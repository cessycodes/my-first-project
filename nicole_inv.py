from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk

root = Tk()
root.title('SmartStock Inventory System')
root.geometry('1350x700+0+0')
root.config(bg="#17232C")

bg_image = PhotoImage(file='inventory.png')
titleLabel = Label(root, image=bg_image, compound=LEFT,
                   text='SmartStock Inventory',
                   font=('times new roman', 40, 'bold'),
                   bg="#353e74", fg='white', anchor='center', padx=20)
titleLabel.place(x=0, y=0, relwidth=1)

subtitleLabel = Label(root, text='Date: 08-01-2026\t\t Time: 08:41 AM',
                      font=('times new roman', 15, 'bold'),
                      bg='#4d636d', fg='white')
subtitleLabel.place(x=0, y=70, relwidth=1)

# --- Product Information Frame ---
infoFrame = Frame(root, bg="#17232C")
infoFrame.place(x=50, y=200, width=400, height=250)

Label(infoFrame, text="Product Name", font=("times new roman", 12, "bold"),
      bg="#17232C", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
Label(infoFrame, text="Category", font=("times new roman", 12, "bold"),
      bg="#17232C", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
Label(infoFrame, text="Quality", font=("times new roman", 12, "bold"),
      bg="#17232C", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
Label(infoFrame, text="Price", font=("times new roman", 12, "bold"),
      bg="#17232C", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
Label(infoFrame, text="Supplier", font=("times new roman", 12, "bold"),
      bg="#17232C", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")

product_var = StringVar()
category_var = StringVar()
quality_var = StringVar()
price_var = StringVar()
supplier_var = StringVar()

Entry(infoFrame, textvariable=product_var, font=("times new roman", 12), bg="lightyellow").grid(row=0, column=1, padx=10, pady=10)
Entry(infoFrame, textvariable=category_var, font=("times new roman", 12), bg="lightyellow").grid(row=1, column=1, padx=10, pady=10)
Entry(infoFrame, textvariable=quality_var, font=("times new roman", 12), bg="lightyellow").grid(row=2, column=1, padx=10, pady=10)
Entry(infoFrame, textvariable=price_var, font=("times new roman", 12), bg="lightyellow").grid(row=3, column=1, padx=10, pady=10)
Entry(infoFrame, textvariable=supplier_var, font=("times new roman", 12), bg="lightyellow").grid(row=4, column=1, padx=10, pady=10)

# --- Table Frame ---
tableFrame = Frame(root, bg="#17232C")
tableFrame.place(x=430, y=200, width=850, height=400)

scroll_x = Scrollbar(tableFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(tableFrame, orient=VERTICAL)

inventoryTable = ttk.Treeview(tableFrame,
                              columns=("ID", "Product Name", "Category", "Quality", "Price", "Supplier"),
                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=inventoryTable.xview)
scroll_y.config(command=inventoryTable.yview)

inventoryTable.heading("ID", text="ID")
inventoryTable.heading("Product Name", text="Product Name")
inventoryTable.heading("Category", text="Category")
inventoryTable.heading("Quality", text="Quality")
inventoryTable.heading("Price", text="Price")
inventoryTable.heading("Supplier", text="Supplier")

inventoryTable.column("ID", width=50)
inventoryTable.column("Product Name", width=150)
inventoryTable.column("Category", width=100)
inventoryTable.column("Quality", width=80)
inventoryTable.column("Price", width=100)
inventoryTable.column("Supplier", width=120)

inventoryTable['show'] = 'headings'
inventoryTable.pack(fill=BOTH, expand=1)

# --- Search Frame ---
searchFrame = Frame(root, bg="#17232C")
searchFrame.place(x=500, y=150, width=600, height=40)

Label(searchFrame, text="Search", font=("times new roman", 12, "bold"),
      bg="#17232C", fg="white").pack(side=LEFT, padx=5)

search_var = StringVar()
searchEntry = Entry(searchFrame, textvariable=search_var, font=("times new roman", 12), bg="lightyellow", width=40)
searchEntry.pack(side=LEFT, padx=5)

def search_item():
    query = search_var.get().lower()
    for child in inventoryTable.get_children():
        values = inventoryTable.item(child)["values"]
        if query in str(values).lower():
            inventoryTable.selection_set(child)
            inventoryTable.focus(child)
            return
    messagebox.showinfo("Search", "No match found")

def refresh_table():
    inventoryTable.selection_remove(inventoryTable.selection())

searchBtn = Button(searchFrame, text="Search", font=("times new roman", 12, "bold"),
                   bg="green", fg="white", command=search_item)
searchBtn.pack(side=LEFT, padx=5)

refreshBtn = Button(searchFrame, text="Refresh", font=("times new roman", 12, "bold"),
                    bg="orange", fg="white", command=refresh_table)
refreshBtn.pack(side=LEFT, padx=5)

# --- Button Functions ---
def add_record():
    if product_var.get() == "" or category_var.get() == "":
        messagebox.showerror("Error", "Please fill all fields")
        return
    inventoryTable.insert("", "end", values=(len(inventoryTable.get_children())+1,
                                             product_var.get(),
                                             category_var.get(),
                                             quality_var.get(),
                                             price_var.get(),
                                             supplier_var.get()))
    clear_fields()

def update_record():
    selected = inventoryTable.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to update")
        return
    inventoryTable.item(selected[0], values=(inventoryTable.item(selected[0])["values"][0],
                                             product_var.get(),
                                             category_var.get(),
                                             quality_var.get(),
                                             price_var.get(),
                                             supplier_var.get()))

def delete_record():
    selected = inventoryTable.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to delete")
        return
    inventoryTable.delete(selected[0])

def clear_fields():
    product_var.set("")
    category_var.set("")
    quality_var.set("")
    price_var.set("")
    supplier_var.set("")

# --- Button Frame ---
buttonFrame = Frame(root, bg="#17232C")
buttonFrame.place(relx=0.5, rely=0.85, anchor="center")

addBtn = Button(buttonFrame, text="Add", font=("times new roman", 12, "bold"),
                bg="blue", fg="white", width=12, command=add_record)
addBtn.grid(row=0, column=0, padx=10, pady=10)

updateBtn = Button(buttonFrame, text="Update", font=("times new roman", 12, "bold"),
                   bg="blue", fg="white", width=12, command=update_record)
updateBtn.grid(row=0, column=1, padx=10, pady=10)

deleteBtn = Button(buttonFrame, text="Delete", font=("times new roman", 12, "bold"),
                   bg="blue", fg="white", width=12, command=delete_record)
deleteBtn.grid(row=0, column=2, padx=10, pady=10)

clearBtn = Button(buttonFrame, text="Clear", font=("times new roman", 12, "bold"),
                  bg="blue", fg="white", width=12, command=clear_fields)
clearBtn.grid(row=0, column=3, padx=10, pady=10)

root.mainloop()