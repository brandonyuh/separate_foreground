import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()


def main():
    root.geometry("1500x500")
    menu_setup(root)
    root.mainloop()


def menu_setup(root):
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", underline=0, menu=filemenu)
    filemenu.add_command(label="Open Image...", command=open_image)
    filemenu.add_command(label="Save Image...", command=save_image)
    filemenu.add_command(label="Exit", underline=1, command=quit)

    editmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Clipboard", underline=0, menu=editmenu)
    editmenu.add_command(label="Paste from Clipboard", command=paste_image)
    editmenu.add_command(label="Copy foreground to clipboard", command=copy_fore)
    editmenu.add_command(label="Copy background to clipboard", command=copy_back)

    paintmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Paint", underline=0, menu=paintmenu)
    paintmenu.add_command(label="Paint Foreground")
    paintmenu.add_command(label="Paint Background")
    paintmenu.add_command(label="Erase")

    adjustmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Adjust", underline=0, menu=adjustmenu)
    adjustmenu.add_command(label="Fill Background")
    adjustmenu.add_command(label="Tolerance Foreground")
    adjustmenu.add_command(label="Color Tolerance Foreground")
    adjustmenu.add_command(label="Distance Tolerance Foreground")
    adjustmenu.add_separator()
    adjustmenu.add_command(label="Tolerance Background")
    adjustmenu.add_command(label="Color Tolerance Background")
    adjustmenu.add_command(label="Distance Tolerance Background")

    helpmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", underline=0, menu=helpmenu)
    helpmenu.add_command(label="About", command=about_command)
    helpmenu.add_command(label="Help", command=help_command)

    root.config(menu=menubar)


def quit():
    print("TODO: check for changes")
    root.quit()


def open_image():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
    print(root.filename)
    print("TODO: load image into UI")


def save_image():
    print("TODO: save image")


def paste_image():
    print("TODO: paste image")


def copy_fore():
    print("TODO: copy fore")


def copy_back():
    print("TODO: copy back")


def about_command():
    messagebox.showinfo('About', 'Version: 0')


def help_command():
    print("TODO: show help")


if __name__ == "__main__":
    main()
