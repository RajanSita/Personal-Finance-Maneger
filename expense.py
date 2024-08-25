from db import connect

def add_expense(user_id, amount, category, date, description):
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute("""
    INSERT INTO Expenses (user_id, amount, category, date, description)
    VALUES (%s, %s, %s, %s, %s);
    """, (user_id, amount, category, date, description))
    
    connection.commit()
    cursor.close()
    connection.close()

def view_expenses(user_id):
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute("""
    SELECT * FROM Expenses WHERE user_id = %s;
    """, (user_id,))
    
    expenses = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return expenses
