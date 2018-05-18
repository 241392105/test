from Tkinter import *
root=Tk()
l1=['a','v','g','d']
l2=['b','c','k','t']
list1=Listbox(root)
list2=Listbox(root)
for i in l1:
    list1.insert(0,i)
for i in l2:
    list2.insert(0,i)
list1.pack()
list2.pack()
root.mainloop()