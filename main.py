import tkinter as tk
root = tk.Tk()

def main():
    menu_setup(root)
    root.mainloop()

def menu_setup(root):
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

def quit():
    root.quit()

if __name__ == "__main__":
    main()
