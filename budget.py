from db import connect

def set_budget(user_id, category, amount, start_date, end_date):
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute("""
    INSERT INTO Budgets (user_id, category, amount, start_date, end_date)
    VALUES (%s, %s, %s, %s, %s);
    """, (user_id, category, amount, start_date, end_date))
    
    connection.commit()
    cursor.close()
    connection.close()

def view_budgets(user_id):
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute("""
    SELECT * FROM Budgets WHERE user_id = %s;
    """, (user_id,))
    
    budgets = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return budgets
