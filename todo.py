import tkinter as tk
from pydoc import text
from tkinter import *
from tkinter import Label, Tk
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
from tkinter.filedialog import asksaveasfilename, askopenfilename, askopenfile
from tkinter import colorchooser

root = Tk()
root.title("Tout Doux")
root.geometry("500x500")
root.minsize(180, 180)
root.maxsize(2080, 1720)
root.iconbitmap("")
root.config(background='grey')



def callback():
    result = messagebox.askyesno('New note', 'Creation of new not')
    clearTextInput()


def clearTextInput():
    text_todo.delete("1.0", "end")


def choose_color():
    color = colorchooser.askcolor()
    print(color)
    text_todo.tag_config("colored_text", foreground=color[1])
    text_todo.tag_add("colored_text", "1.0", "end")


def save_text():
    content = text_todo.get("1.0", tk.END)
    file = asksaveasfilename(title="save", filetypes=[("text file", "*txt")])
    with open(file, "w") as data:
        data.write(content)


def open_file():
    text_todo.delete("1.0", END)
    file = askopenfile(mode="r", filetypes=[("text files", "*txt")])
    if file is not None:
        content = file.read()
        text_todo.insert("1.0", content)


frame = Frame(root, bg='grey')


label_title = Label(text="Note ", font=("courrier", 40), bg='grey', fg='orange')
label_title.pack(expand=NO)

menubar = Menu(root)
root.config(menu=menubar)


menufichier = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=menufichier)
menufichier.add_command(label="New", command=callback)
menufichier.add_command(label="Open", command=open_file)
menufichier.add_command(label="Save", command=save_text)
menufichier.add_separator()
menufichier.add_command(label="Quit", command=root.quit)

menufichier = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Police", menu=menufichier)
menufichier.add_command(label="Color", command=choose_color)


text_todo = Text(height=300, width=300)
text_todo.pack()


root.config(menu=menubar)
root.mainloop()
