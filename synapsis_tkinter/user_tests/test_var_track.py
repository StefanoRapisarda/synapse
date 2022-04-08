import tkinter as tk

def my_func(var, indx, mode):
    print(entry.get())
root = tk.Tk()

var  =tk.StringVar(root)
print(dir(var))
var.trace('w',lambda x: entry.name = entry.get()) 
print(test)

entry = tk.Entry(root,textvariable = var,width = 50)
entry.pack()

root.mainloop()
