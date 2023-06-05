import tkinter as tk
from tkinter import ttk
import connect_mongo as db
from tkcalendar import DateEntry


def show_data(param):
    count = 2
    selected_date = date_entry.get()
    selected_id = entry.get()
    clear_treeview(tree)
    if param == 'byDate':  
        docs = db.fetch_by_date(selected_date)
    if param == 'byId':    
        docs = db.fetch_by_id(selected_id) 
    if param == 'both':
        docs = db.fetch_by_IdDate(selected_id, selected_date)
    for doc in docs:
        tree.insert(parent='', index='end',values=(doc['id'],doc['name'], doc['time']))
    for item in tree.get_children():
        if(count%2==0): tree_tag = ('white')
        else: tree_tag = ('black')
        tree.item(item, tags=('Treeitem',tree_tag)) 
        count = count + 1

def clear_treeview(tree):
    item_ids = tree.get_children()
    for item_id in item_ids:
        tree.delete(item_id)

root = tk.Tk()
root.geometry('600x600')
root.resizable(False, False)
style = ttk.Style()
style.theme_use('clam')
style_font =('Verdana', 10)
btn_style = ttk.Style(root)
btn_style.configure('Custom.TButton' ,foreground = 'black', font = ('Verdana', 8, 'bold'))
btn_style.map("Custom.TButton", background=[("active", "#B0B0B0")])

title_label = tk.Label(root, text='Employee Attendance', font=('Verdana', 14, 'bold'), bg="black", fg="white", width=30).pack(pady=10)

label1 = tk.Label(root, text='Enter employee ID: ', font=style_font)
label1.place(x = 90, y= 60)

label2 = tk.Label(root, text='Choose Date: ', font=style_font)
label2.place(x = 90, y= 99)

entry = ttk.Entry(root, width=17, font=style_font)
entry.pack(pady=15)
show_data_btn2 = ttk.Button(root, text="Show by ID", style='Custom.TButton', command=lambda:show_data("byId"), width=16)
show_data_btn2.place(x = 390, y = 60)

date_entry = DateEntry(root, width = 15, font=style_font, date_pattern = "dd-mm-yyyy")
date_entry.pack()

show_data_btn = ttk.Button(root, text="Show by Date", style='Custom.TButton', command=lambda:show_data("byDate"), width=16)
show_data_btn.place(x = 390, y = 99)

show_data_btn3 = ttk.Button(root, text="Show via both", style='Custom.TButton', command=lambda:show_data("both"), width=16)
show_data_btn3.pack(pady=10)

tree_style = ttk.Style(root)
tree_style.configure("Custom.Treeview.Heading", font=('Verdana', 10, 'bold'))
tree = ttk.Treeview(root, columns=('Id','Name', 'Time'), show='headings', style="Custom.Treeview", height=18)
tree.heading('Id', text='Id')
tree.heading('Name', text='Name')
tree.heading('Time', text='Time')
tree.column('Id', anchor='center', width=180)
tree.column('Name', anchor='center', width=180)
tree.column('Time', anchor='center', width=180)
tree.tag_configure('Treeitem', font=style_font)
tree.tag_configure('black', background="#808898", foreground="white")
tree.tag_configure('white', background="white")
tree.pack(pady=30)
root.mainloop()