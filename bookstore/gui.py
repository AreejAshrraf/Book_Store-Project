import tkinter as tk
from tkinter import messagebox, ttk

from bookstore.book import Book
from .bookstore import Bookstore

class AddBookDialog(tk.Toplevel):
    def __init__(self, master, bookstore):
        super().__init__(master)
        self.title("Add Book")
        self.configure(bg="#FFD700")  # Gold background

        self.bookstore = bookstore

        self.title_label = ttk.Label(self, text="Enter Book Details", font=("Arial", 16, "bold"), background="#FFD700", foreground="black")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.title_label = ttk.Label(self, text="Title:", font=("Arial", 12), background="#FFD700", foreground="#333")
        self.title_label.grid(row=1, column=0, pady=5, padx=5, sticky="E")
        self.title_entry = ttk.Entry(self, font=("Arial", 12))
        self.title_entry.grid(row=1, column=1, pady=5, padx=5, sticky="W")

        self.author_label = ttk.Label(self, text="Author:", font=("Arial", 12), background="#FFD700", foreground="#333")
        self.author_label.grid(row=2, column=0, pady=5, padx=5, sticky="E")
        self.author_entry = ttk.Entry(self, font=("Arial", 12))
        self.author_entry.grid(row=2, column=1, pady=5, padx=5, sticky="W")

        self.price_label = ttk.Label(self, text="Price:", font=("Arial", 12), background="#FFD700", foreground="#333")
        self.price_label.grid(row=3, column=0, pady=5, padx=5, sticky="E")
        self.price_entry = ttk.Entry(self, font=("Arial", 12))
        self.price_entry.grid(row=3, column=1, pady=5, padx=5, sticky="W")

        self.add_button = ttk.Button(self, text="Add Book", command=self.add_book, style="Accent.TButton")
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Style configuration for themed buttons
        self.style = ttk.Style()
        self.style.configure("Accent.TButton", foreground="black", background="#008080", font=("Arial", 12))

    '''def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        price = float(self.price_entry.get()) if self.price_entry.get() else 0.0

        if title and author:
            new_book = Book(title, author, price)
            self.bookstore.add_book(new_book)
            messagebox.showinfo("Success", "Book added successfully!")
            self.destroy()'''
    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        price = float(self.price_entry.get()) if self.price_entry.get() else 0.0

        if title and author:
            new_book = Book(title, author, price)
            self.bookstore.add_book(new_book)
            messagebox.showinfo("Success", "Book added successfully!")
            self.destroy()
'''class DisplayBooksDialog(tk.Toplevel):
    def __init__(self, master, bookstore):
        super().__init__(master)
        self.title("Book List")
        self.configure(bg="#FFD700")  # Gold background

        self.bookstore = bookstore

        if not self.bookstore.books:
            messagebox.showinfo("Info", "No books in the bookstore.")
            return

        for i, book in enumerate(self.bookstore.books):
            book_label = ttk.Label(self, text=str(book), font=("Arial", 12), background="#FFD700", foreground="#333")
            book_label.grid(row=i, column=0, pady=5) '''
class DisplayBooksDialog(tk.Toplevel):
    def __init__(self, master, bookstore):
        super().__init__(master)
        self.title("Book List")
        self.configure(bg="#FFD700")  # Gold background

        self.bookstore = bookstore

        books = self.bookstore.get_books()  # Retrieve books from the bookstore
        if not books:
            messagebox.showinfo("Info", "No books in the bookstore.")
            return

        for i, book in enumerate(books):
            book_label = ttk.Label(self, text=str(book), font=("Arial", 12), background="#FFD700", foreground="#333")
            book_label.grid(row=i, column=0, pady=5)



class BookstoreGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Bookstore")
        self.master.geometry("800x600")
        self.master.configure(bg="#6495ED")  # Cornflower blue background

        self.bookstore = Bookstore()

        self.title_label = ttk.Label(master, text="Welcome to the Bookstore", font=("Arial", 24, "bold"), background="#6495ED", foreground="red")
        self.title_label.pack(pady=20)

        self.add_button = ttk.Button(master, text="Add Book", command=self.open_add_book_dialog, style="Accent.TButton")
        self.add_button.pack(pady=10)

        self.display_button = ttk.Button(master, text="Display Books", command=self.open_display_books_dialog, style="Accent.TButton")
        self.display_button.pack(pady=10)

        # Style configuration for themed buttons
        self.style = ttk.Style()
        self.style.configure("Accent.TButton", foreground="black", background="#008080", font=("Arial", 14))

    def open_add_book_dialog(self):
        # Calculate the center position
        main_menu_x = self.master.winfo_x()
        main_menu_y = self.master.winfo_y()
        main_menu_width = self.master.winfo_width()
        main_menu_height = self.master.winfo_height()

        dialog_width = 300  # Adjust the width of the dialog as needed
        dialog_height = 200  # Adjust the height of the dialog as needed

        dialog_x = main_menu_x + (main_menu_width - dialog_width) // 2
        dialog_y = main_menu_y + (main_menu_height - dialog_height) // 2

        add_book_dialog = AddBookDialog(self.master, self.bookstore)
        add_book_dialog.geometry(f"{dialog_width}x{dialog_height}+{dialog_x}+{dialog_y}")
        self.master.wait_window(add_book_dialog)

    def open_display_books_dialog(self):
        # Calculate the center position
        main_menu_x = self.master.winfo_x()
        main_menu_y = self.master.winfo_y()
        main_menu_width = self.master.winfo_width()
        main_menu_height = self.master.winfo_height()

        dialog_width = 200  # Adjust the width of the dialog as needed
        dialog_height = 100  # Adjust the height of the dialog as needed

        dialog_x = main_menu_x + (main_menu_width - dialog_width) // 2
        dialog_y = main_menu_y + (main_menu_height - dialog_height) // 2

        display_books_dialog = DisplayBooksDialog(self.master, self.bookstore)
        display_books_dialog.geometry(f"{dialog_width}x{dialog_height}+{dialog_x}+{dialog_y}")
        self.master.wait_window(display_books_dialog)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreGUI(root)
    root.mainloop()
