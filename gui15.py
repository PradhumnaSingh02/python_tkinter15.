from tkinter import *

root = Tk()
root.geometry('644x456')
root.title('ScrollBar')

#For connecting scrollbar to a widget
# 1...widget(vscrollcommand = scrollbar.set
# scrollbar.config(command=widget,yview

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y, padx=17)
#listbox = Listbox(root, yscrollcommand = scrollbar.set)
#for i in range (200):
    #listbox.insert(END, f"Item {i}")
text = Text(root, yscrollcommand = scrollbar.set)
text.pack(fill=BOTH)
#listbox.pack(fill='both',padx=67)
#scrollbar.config(command=listbox.yview)
scrollbar.config(command=text.yview)
#Button(root, text='Add Item').pack()


root.mainloop()