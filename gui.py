import tkinter as tk
from tkinter import *
import os


root = tk.Tk()
canvas = tk.Canvas(root, height=500, width=550, bg="#388C4E")

canvas.pack()

frame = tk.Frame(root, bg="#DDFCD4")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

newbut = tk.Button(root, bg="#54D7C1", text="New Project", padx=5, pady=2, bd=0)

delbut = tk.Button(root, bg="#54D7C1", text="Delete Project", padx=5, pady=2, bd=0)
archibut = tk.Button(root, bg="#54D7C1", text="Archive Project", padx=5, pady=2, bd=0)
archibut.place()


root.mainloop()
