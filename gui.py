import tkinter as tk
from tkinter import messagebox
from db import create_tables
import user
import expense
import budget
import report

class FinanceManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Manager")
        self.user_id = None
        
        self.login_screen()
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1)
        
        tk.Label(self.root, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)
        
        tk.Button(self.root, text="Login", command=self.login).grid(row=2, column=0)
        tk.Button(self.root, text="Register", command=self.register_screen).grid(row=2, column=1)
    
    def register_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Username:").grid(row=0, column=0)
        self.reg_username_entry = tk.Entry(self.root)
        self.reg_username_entry.grid(row=0, column=1)
        
        tk.Label(self.root, text="Password:").grid(row=1, column=0)
        self.reg_password_entry = tk.Entry(self.root, show="*")
        self.reg_password_entry.grid(row=1, column=1)
        
        tk.Button(self.root, text="Register", command=self.register).grid(row=2, column=0)
        tk.Button(self.root, text="Back", command=self.login_screen).grid(row=2, column=1)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_id = user.login(username, password)
        if user_id:
            self.user_id = user_id
            self.user_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        user.register(username, password)
        messagebox.showinfo("Success", "User registered successfully")
        self.login_screen()
    
    def user_menu(self):
        self.clear_screen()
        
        tk.Button(self.root, text="Add Expense", command=self.add_expense_screen).grid(row=0, column=0)
        tk.Button(self.root, text="View Expenses", command=self.view_expenses).grid(row=1, column=0)
        tk.Button(self.root, text="Set Budget", command=self.set_budget_screen).grid(row=2, column=0)
        tk.Button(self.root, text="View Budgets", command=self.view_budgets).grid(row=3, column=0)
        tk.Button(self.root, text="Generate Report", command=self.generate_report).grid(row=4, column=0)
        tk.Button(self.root, text="Logout", command=self.login_screen).grid(row=5, column=0)
    
    def add_expense_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Amount:").grid(row=0, column=0)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=0, column=1)
        
        tk.Label(self.root, text="Category:").grid(row=1, column=0)
        self.category_entry = tk.Entry(self.root)
        self.category_entry.grid(row=1, column=1)
        
        tk.Label(self.root, text="Date (YYYY-MM-DD):").grid(row=2, column=0)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=2, column=1)
        
        tk.Label(self.root, text="Description:").grid(row=3, column=0)
        self.description_entry = tk.Entry(self.root)
        self.description_entry.grid(row=3, column=1)
        
        tk.Button(self.root, text="Add Expense", command=self.add_expense).grid(row=4, column=0)
        tk.Button(self.root, text="Back", command=self.user_menu).grid(row=4, column=1)
    
    def add_expense(self):
        amount = float(self.amount_entry.get())
        category = self.category_entry.get()
        date = self.date_entry.get()
        description = self.description_entry.get()
        expense.add_expense(self.user_id, amount, category, date, description)
        messagebox.showinfo("Success", "Expense added successfully")
        self.user_menu()
    
    def view_expenses(self):
        self.clear_screen()
        
        expenses = expense.view_expenses(self.user_id)
        for idx, exp in enumerate(expenses):
            tk.Label(self.root, text=str(exp)).grid(row=idx, column=0)
        
        tk.Button(self.root, text="Back", command=self.user_menu).grid(row=len(expenses), column=0)
    
    def set_budget_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Category:").grid(row=0, column=0)
        self.budget_category_entry = tk.Entry(self.root)
        self.budget_category_entry.grid(row=0, column=1)
        
        tk.Label(self.root, text="Amount:").grid(row=1, column=0)
        self.budget_amount_entry = tk.Entry(self.root)
        self.budget_amount_entry.grid(row=1, column=1)
        
        tk.Label(self.root, text="Start Date (YYYY-MM-DD):").grid(row=2, column=0)
        self.start_date_entry = tk.Entry(self.root)
        self.start_date_entry.grid(row=2, column=1)
        
        tk.Label(self.root, text="End Date (YYYY-MM-DD):").grid(row=3, column=0)
        self.end_date_entry = tk.Entry(self.root)
        self.end_date_entry.grid(row=3, column=1)
        
        tk.Button(self.root, text="Set Budget", command=self.set_budget).grid(row=4, column=0)
        tk.Button(self.root, text="Back", command=self.user_menu).grid(row=4, column=1)
    
    def set_budget(self):
        category = self.budget_category_entry.get()
        amount = float(self.budget_amount_entry.get())
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        budget.set_budget(self.user_id, category, amount, start_date, end_date)
        messagebox.showinfo("Success", "Budget set successfully")
        self.user_menu()
    
    def view_budgets(self):
        self.clear_screen()
        
        budgets = budget.view_budgets(self.user_id)
        for idx, bud in enumerate(budgets):
            tk.Label(self.root, text=str(bud)).grid(row=idx, column=0)
        
        tk.Button(self.root, text="Back", command=self.user_menu).grid(row=len(budgets), column=0)
    
    def generate_report(self):
        self.clear_screen()
        
        report_data = report.generate_report(self.user_id)
        for idx, row in enumerate(report_data):
            tk.Label(self.root, text=str(row)).grid(row=idx, column=0)
        
        tk.Button(self.root, text="Back", command=self.user_menu).grid(row=len(report_data), column=0)

if __name__ == "__main__":
    create_tables()
    root = tk.Tk()
    app = FinanceManagerApp(root)
    root.mainloop()
