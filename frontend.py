from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selection

        index = list_box.curselection()[0]
        selection = list_box.get(index)
        title_entry.delete(0, END)
        title_entry.insert(END, selection[1])
        publisher_entry.delete(0, END)
        publisher_entry.insert(END, selection[2])
        year_entry.delete(0, END)
        year_entry.insert(END, selection[3])
        upc_entry.delete(0, END)
        upc_entry.insert(END, selection[4])
    except IndexError:
        pass
    
def view_command():
    list_box.delete(0, END)
    for row in backend.view():
        list_box.insert(END, row)

def search_command():
    list_box.delete(0, END)
    for row in backend.search(title_text.get(), publisher_text.get(), year_text.get(), upc_text.get()):
        list_box.insert(END, row)

def add_command():
    backend.insert(title_text.get(), publisher_text.get(), year_text.get(), upc_text.get())
    list_box.delete(0, END)
    list_box.insert(END, (title_text.get(), publisher_text.get(), year_text.get(), upc_text.get()))

def delete_command():
    backend.delete(selection[0])

def update_command():
    backend.update(selection[0], title_text.get(), publisher_text.get(), year_text.get(), upc_text.get())


window = Tk()
window.wm_title("Game Library")

title_label = Label(window, text="Title")
title_label.grid(row=2, column=0)
title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=2, column=1, columnspan=2)

publisher_label = Label(window, text="Publisher")
publisher_label.grid(row=3, column=0)
publisher_text = StringVar()
publisher_entry = Entry(window, textvariable=publisher_text)
publisher_entry.grid(row=3, column=1, columnspan=2)

year_label = Label(window, text="Year")
year_label.grid(row=4, column=0)
year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=4, column=1, columnspan=2)

upc_label = Label(window, text="UPC")
upc_label.grid(row=5, column=0)
upc_text = StringVar()
upc_entry = Entry(window, textvariable=upc_text)
upc_entry.grid(row=5, column=1, columnspan=2)

view_all_button = Button(window, text="View all entries", width=12, command=view_command)
view_all_button.grid(row=0, column=0)

add_entry_button = Button(window, text="Add entry", width=12, command=add_command)
add_entry_button.grid(row=0, column=1)

delete_entry_button = Button(window, text="Delete entry",width=12, command=delete_command)
delete_entry_button.grid(row=0, column=2)

search_button = Button(window, text="Search entry", width=12, command=search_command)
search_button.grid(row=1, column=0)

update_button = Button(window, text="Update entry", width=12, command=update_command)
update_button.grid(row=1, column=1)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=1, column=2)

list_box = Listbox(window, height= 8, width=65)
list_box.grid(row=0, rowspan=8, column=3)
scroll_bar = Scrollbar(window)
scroll_bar.grid(row=2, rowspan=6, column=4)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>', get_selected_row)


window.mainloop()