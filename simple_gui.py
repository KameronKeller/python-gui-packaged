import tkinter as tk

root = tk.Tk()
root.title("Basic Example")

button = tk.Button(text="This is a button")
button.pack()

root.minsize(500,250)
root.mainloop()
