import tkinter as tk

root = tk.Tk()
root.title("Basic Example")
root.minsize(500,250)

button = tk.Button(text="This is a button")
button.pack()

root.mainloop()
