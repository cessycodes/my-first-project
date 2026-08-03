from tkinter import *
from tkinter import ttk, messagebox
import sqlite3 as sql

root = Tk()
root.title("SmartStock Inventory System")
root.geometry("1350x700+0+0")
root.config(bg="#17232C")

# Title
bg_image = PhotoImage(file='inventory.png')
titleLabel = Label(root, image=bg_image, compound=LEFT,text='SmartStock Inventory',font=('times new roman', 40, 'bold'),bg="#353e74", fg='white', anchor='center', padx=20)
titleLabel.place(x=0, y=0, relwidth=1)

subtitleLabel = Label(root, text='Date: 08-01-2026\t\t Time: 01:22 AM',font=('times new roman', 15, 'bold'),bg='#4d636d', fg='white')
subtitleLabel.place(x=0, y=70, relwidth=1)

#Search Bar
searchFrame = Frame(root, bg="#17232C")
searchFrame.place(x=500, y=150, width=850, height=40)

searchLabel = Label(searchFrame, text="Search:", font=("times new roman", 12, "bold"),bg="#17232C", fg="white")
searchLabel.pack(side=LEFT, padx=5)

searchEntry = Entry(searchFrame, font=("times new roman", 12), bg="lightyellow", width=40)
searchEntry.pack(side=LEFT, padx=5)

def search_item():
    query = searchEntry.get()
    messagebox.showinfo("Search", f"Searching for '{query}'")

def refresh_table():
    load_data()

searchBtn = Button(searchFrame, text="Search", font=("times new roman", 12, "bold"),bg="green", fg="white", command=search_item)
searchBtn.pack(side=LEFT, padx=5)

refreshBtn = Button(searchFrame, text="Refresh", font=("times new roman", 12, "bold"),bg="blue", fg="white", command=refresh_table)
refreshBtn.pack(side=LEFT, padx=5)

#Product Information Section
infoFrame = LabelFrame(root, text="Product Information", font=("times new roman", 15, "bold"),bg="#17232C", fg="white", bd=5, relief=RIDGE)
infoFrame.place(x=150, y=250, width=500, height=400)

# Labels + Entry fields
Label(infoFrame, text="Product:", font=("times new roman", 12, "bold"),bg="#17232C", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky=W)
productEntry = Entry(infoFrame, font=("times new roman", 12), width=25)
productEntry.grid(row=0, column=1, padx=10, pady=10)

Label(infoFrame, text="Category:", font=("times new roman", 12, "bold"),bg="#17232C", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky=W)
categoryEntry = Entry(infoFrame, font=("times new roman", 12), width=25)
categoryEntry.grid(row=1, column=1, padx=10, pady=10)

Label(infoFrame, text="Qty:", font=("times new roman", 12, "bold"),bg="#17232C", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky=W)
qtyEntry = Entry(infoFrame, font=("times new roman", 12), width=25)
qtyEntry.grid(row=2, column=1, padx=10, pady=10)

Label(infoFrame, text="Price:", font=("times new roman", 12, "bold"),bg="#17232C", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky=W)
priceEntry = Entry(infoFrame, font=("times new roman", 12), width=25)
priceEntry.grid(row=3, column=1, padx=10, pady=10)

# Buttons
btnFrame = Frame(infoFrame, bg="#17232C")
btnFrame.place(x=50, y=250, width=400)

# Configure columns para pantay
for i in range(4):
    btnFrame.grid_columnconfigure(i, weight=1)

addBtn = Button(btnFrame, text="Add", font=("times new roman", 12, "bold"),bg="blue", fg="white")
addBtn.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

updateBtn = Button(btnFrame, text="Update", font=("times new roman", 12, "bold"),bg="blue", fg="white")
updateBtn.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

deleteBtn = Button(btnFrame, text="Delete", font=("times new roman", 12, "bold"),bg="blue", fg="white")
deleteBtn.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

clearBtn = Button(btnFrame, text="Clear", font=("times new roman", 12, "bold"),bg="blue", fg="white")
clearBtn.grid(row=0, column=3, padx=10, pady=10, sticky="ew")


# Product List Section
listFrame = LabelFrame(root, text="Product List", font=("times new roman", 15, "bold"),bg="#17232C", fg="white", bd=5, relief=RIDGE)
listFrame.place(x=750, y=230, width=700, height=450)

scroll_x = Scrollbar(listFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(listFrame, orient=VERTICAL)

productTable = ttk.Treeview(listFrame,columns=("ID", "Product", "Category", "Qty", "Price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=productTable.xview)
scroll_y.config(command=productTable.yview)

productTable.heading("ID", text="ID")
productTable.heading("Product", text="Product")
productTable.heading("Category", text="Category")
productTable.heading("Qty", text="Qty")
productTable.heading("Price", text="Price")

productTable.column("ID", width=50)
productTable.column("Product", width=150)
productTable.column("Category", width=150)
productTable.column("Qty", width=100)
productTable.column("Price", width=100)

productTable['show'] = 'headings'
productTable.pack(fill=BOTH, expand=1)


#Bottom Navigation Buttons
bottomFrame = Frame(root, bg="#17232C")
bottomFrame.pack(side=BOTTOM, fill=X, pady=20)

def open_reports():
    messagebox.showinfo("Reports", "Opening reports...")

def logout():
    confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm:
        root.destroy()

reportsBtn = Button(bottomFrame, text="Reports", font=("times new roman", 12, "bold"),bg="blue", fg="white", width=12, command=open_reports)
reportsBtn.pack(side=LEFT, padx=20)

logoutBtn = Button(bottomFrame, text="Logout", font=("times new roman", 12, "bold"),bg="red", fg="white", width=12, command=logout)
logoutBtn.pack(side=RIGHT, padx=20)

#Database Setup
con = sql.connect("inventory.db")
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT NOT NULL,
        category TEXT NOT NULL,
        qty INTEGER NOT NULL,
        price REAL NOT NULL
    )
""")
con.commit()

#Functions
def load_data():
    productTable.delete(*productTable.get_children())
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    for row in rows:
        productTable.insert("", END, values=row)

def add_item():
    product = productEntry.get()
    category = categoryEntry.get()
    qty = qtyEntry.get()
    price = priceEntry.get()

    if product == "" or category == "" or qty == "" or price == "":
        messagebox.showerror("Error", "All fields are required")
        return

    cur.execute("INSERT INTO products (product, category, qty, price) VALUES (?, ?, ?, ?)",(product, category, qty, price))
    con.commit()
    load_data()
    clear_fields()
    messagebox.showinfo("Success", "Product added successfully")

def update_item():
    selected = productTable.focus()
    if not selected:
        messagebox.showerror("Error", "Select a product to update")
        return

    values = productTable.item(selected, "values")
    product_id = values[0]

    cur.execute("UPDATE products SET product=?, category=?, qty=?, price=? WHERE id=?",(productEntry.get(), categoryEntry.get(), qtyEntry.get(), priceEntry.get(), product_id))
    con.commit()
    load_data()
    clear_fields()
    messagebox.showinfo("Success", "Product updated successfully")

def delete_item():
    selected = productTable.focus()
    if not selected:
        messagebox.showerror("Error", "Select a product to delete")
        return

    values = productTable.item(selected, "values")
    product_id = values[0]

    cur.execute("DELETE FROM products WHERE id=?", (product_id,))
    con.commit()
    load_data()
    clear_fields()
    messagebox.showinfo("Success", "Product deleted successfully")

def clear_fields():
    productEntry.delete(0, END)
    categoryEntry.delete(0, END)
    qtyEntry.delete(0, END)
    priceEntry.delete(0, END)

#Bind Buttons
addBtn.config(command=add_item)
updateBtn.config(command=update_item)
deleteBtn.config(command=delete_item)
clearBtn.config(command=clear_fields)

#Load Data Initially
load_data()
root.mainloop()
