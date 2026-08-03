from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3 as sql

def customer_form():
    global back_image
    customer_frame=Frame(root, width=1070, height=567, bg='white')
    customer_frame.place(x=250, y=100, width=1285, height=777)
    haeding_label=Label(customer_frame, text='Manager and Employee Inventory', font=('Times new roman', 16, 'bold'),bg='#0f4d7d', fg='white')
    haeding_label.place(x=0, y=0, relwidth=1)
    back_image=PhotoImage(file='back_button.png')
    back_button=Button(customer_frame, image=back_image, bd=0, cursor='hand2', command=lambda: customer_frame.place_forget())
    back_button.place(x=0, y=30)

    top_frame=LabelFrame(customer_frame, text='Search', bg='white', font=('times new roman',15,'bold'), bd=2, relief=RIDGE, )
    top_frame.place(x=300, y=50, width=600, height=70)
    search_combobox=ttk.Combobox(top_frame, values=('Select','id', 'Name','Email'), font=('times new roman',12, 'bold'), state='readonly', justify=CENTER)
    search_combobox.place(x=10, y=10, width=180)
    search_entry=Entry(top_frame, font=('times new roman',15, 'bold'),bg='lightyellow').place(x=225, y=9, width=150, height=25)
    search_button=Button(top_frame, text= 'Search', font=('times new roman',15,'bold'),bg='#4caf50', fg='white', cursor='hand2').place(x=420, y=5, width=150, height=30 )

    tab_frame=Frame(customer_frame, bg='white')
    tab_frame.place(x=20, y=150, width=1170, height=150)

   
    customer_treeview=ttk.Treeview(tab_frame, column=('ID','Name','Email', 'Position'), show='headings')
    customer_treeview.pack(pady=10)
                                   
    customer_treeview.heading('ID',text='ID')
    customer_treeview.heading('Name',text='Name')
    customer_treeview.heading('Email',text='Email')
    customer_treeview.heading('Position',text='Position')

    customer_treeview.column('ID',width=60)
    customer_treeview.column('Name',width=140)
    customer_treeview.column('Email',width=180)
    customer_treeview.column('Position',width=120)


    haeding_label.place(x=0, y=0, relwidth=1)
    haeding_label.place(x=0, y=0, relwidth=1)

    title=Label(customer_frame, text='Details', font=('Times new roman', 16, 'bold'),bg="#204664", fg='White').place(x=150, y=300, width=1000,relwidth=0)

    
    
    cusid= Label(customer_frame, text='ID', font=('times new roman', 15), bg='white', fg='gray')
    cusid.place(x=330, y=370)
    txt_cusid = Entry(customer_frame, font=('times new roman', 15), bg='lightyellow')
    txt_cusid.place(x=400, y=370, width=180)


    name= Label(customer_frame, text='Name', font=('times new roman', 15), bg='white', fg='gray')
    name.place(x=750, y=370)
    txt_name = Entry(customer_frame, font=('times new roman', 15), bg='lightyellow')
    txt_name.place(x=830, y=370, width=180)


    email= Label(customer_frame, text='Email', font=('times new roman', 15), bg='white', fg='gray')
    email.place(x=320, y=430)
    txt_email= Entry(customer_frame, font=('times new roman', 15), bg='lightyellow')
    txt_email.place(x=400, y=430, width=180)


    postion= Label(customer_frame, text='Position', font=('times new roman', 15), bg='white', fg='gray')
    postion.place(x=750, y=430)
    txt_position = Entry(customer_frame, font=('times new roman', 15))
    txt_position.place(x=830, y=430, width=180)
    position_combobox=ttk.Combobox(customer_frame, values=('Select', 'Admin','Manager'), font=('times new roman',12, 'bold'), state='readonly', justify=CENTER)
    position_combobox.place(x=830, y=430, width=180)


    
    add_button = Button(title, text='Add', font=('times new roman', 12, 'bold'), bg='#0f4d7d', fg='white', bd=0, width=10, cursor='hand2').place(x=620, y=620)
    Update_button = Button(title, text='Update', font=('times new roman', 12, 'bold'), bg='#0f4d7d', fg='white', bd=0, width=10, cursor='hand2').place(x=760, y=620)
    del_button = Button(title, text='Delete', font=('times new roman', 12, 'bold'), bg='#0f4d7d', fg='white', bd=0, width=10, cursor='hand2').place(x=900, y=620)
    clr_button = Button(title, text='Clear', font=('times new roman', 12, 'bold'), bg='#0f4d7d', fg='white', bd=0, width=10, cursor='hand2').place(x=1040, y=620)

root=Tk()

root.title('SmartStock Inventory System')
root.geometry('1350x700+0+0')
leftFrame=Frame(root,bg="#131523")
root.config(bg="#17232C")


bg_image=PhotoImage(file='inventory.png')
titleLabel=Label(root, image=bg_image, compound=LEFT,text='SmartStock Inventory', font=('times new roman',40,'bold'),bg="#353e74",fg='white', anchor='center', padx=20)
titleLabel.place(x=0,y=0,relwidth=1)


logoutButton=Button(root, text='Logout', font=('times new roman',20,'bold'), fg='#010c48')
logoutButton.place(x=1400, y=10)

subtitleLabel=Label(root,text='Date: 08-01-2026\t\t Time: 08:41 AM', font=('times new roman',15, 'bold'),bg='#4d636d', fg='white')
subtitleLabel.place(x=0,y=70, relwidth=1)

leftFrame=Frame(root,bd=2, relief=RIDGE, bg="#171A2D")
leftFrame.place(x=0, y=99, width=250, height=777 )

logoimage=PhotoImage(file='logo.png')
imagelabel=Label(leftFrame, image=logoimage)
imagelabel.pack(fill=X)



menuLabel=Label(leftFrame, text='Menu', font=('times new roman',25,'bold'),bg="#030F0E", fg='white')
menuLabel.pack(fill=X)


customer_button=Button(leftFrame, text='Customer',font=('times new roman',25,'bold'),bg='#009688', command=customer_form)
customer_button.pack(fill=X)

supplier_button=Button(leftFrame, text='Supplier', font=('times new roman',25,'bold'),bg='#009688')
supplier_button.pack(fill=X)

category_button=Button(leftFrame, text='Category', font=('times new roman',25,'bold'),bg='#009688')
category_button.pack(fill=X)

product_button=Button(leftFrame, text='Product', font=('times new roman',25,'bold'),bg='#009688')
product_button.pack(fill=X)

cus_frame=Frame(root, bg="#2C3E50", bd=3, relief=RIDGE)
cus_frame.place(x=400, y=150, height=170, width=280)
total_cus_icon=PhotoImage(file='total_cus.png')
total_cus_label=Label(cus_frame, image=total_cus_icon)
total_cus_icon_label=Label(cus_frame, image=total_cus_icon, bg='#2C3E50')
total_cus_icon_label.pack(pady=15)

total_cus_label=Label(cus_frame,text='Total Customers',bg="#2C3E50", fg='white',font=('times new roman',20,'bold'))
total_cus_label.pack()

total_cus_count_label=Label(cus_frame,text='0',bg="#2C3E50", fg='white',font=('times new roman',20,'bold'))
total_cus_count_label.pack()

sup_frame=Frame(root, bg="#8E44AD", bd=3, relief=RIDGE)
sup_frame.place(x=800, y=150, height=170, width=280)
total_sup_icon=PhotoImage(file='total_sup.png')
total_sup_label=Label(cus_frame, image=total_sup_icon)
total_sup_icon_label=Label(sup_frame, image=total_sup_icon, bg='#8E44AD')
total_sup_icon_label.pack(pady=15)

total_sup_label=Label(sup_frame,text='Total Suppliers',bg="#8E44AD", fg='white',font=('times new roman',20,'bold'))
total_sup_label.pack()

total_sup_count_label=Label(sup_frame,text='0',bg="#8E44AD", fg='white',font=('times new roman',20,'bold'))
total_sup_count_label.pack()

cat_frame=Frame(root, bg="#27AE60", bd=3, relief=RIDGE)
cat_frame.place(x=400, y=400, height=170, width=280)
total_cat_icon=PhotoImage(file='total_cat.png')
total_cat_label=Label(cus_frame, image=total_cat_icon)
total_cat_icon_label=Label(cat_frame, image=total_cat_icon, bg='#27AE60')
total_cat_icon_label.pack(pady=15)

total_cat_label=Label(cat_frame,text='Total Categories',bg="#27AE60", fg='white',font=('times new roman',20,'bold'))
total_cat_label.pack()

total_cat_count_label=Label(cat_frame,text='0',bg="#27AE60", fg='white',font=('times new roman',20,'bold'))
total_cat_count_label.pack()

prod_frame=Frame(root, bg="#E74C3C", bd=3, relief=RIDGE)
prod_frame.place(x=800, y=400, height=170, width=280)
total_prod_icon=PhotoImage(file='total_prod.png')
total_prod_label=Label(cus_frame, image=total_prod_icon)
total_prod_icon_label=Label(prod_frame, image=total_prod_icon, bg='#E74C3C')
total_prod_icon_label.pack(pady=15)

total_prod_label=Label(prod_frame,text='Total Products',bg="#E74C3C", fg='white',font=('times new roman',20,'bold'))
total_prod_label.pack()

total_prod_count_label=Label(prod_frame,text='0',bg="#E74C3C", fg='white',font=('times new roman',20,'bold'))
total_prod_count_label.pack()






root.mainloop()

