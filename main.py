# main.py
from bookstore.gui import BookstoreGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreGUI(root)
    root.mainloop()