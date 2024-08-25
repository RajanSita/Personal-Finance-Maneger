import tkinter as tk
from gui import FinanceManagerApp
from db import create_tables

if __name__ == "__main__":
    create_tables()
    root = tk.Tk()
    app = FinanceManagerApp(root)
    root.mainloop()
