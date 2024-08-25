from db import connect

def generate_report(user_id):
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute("""
    SELECT category, SUM(amount) as total
    FROM Expenses
    WHERE user_id = %s
    GROUP BY category;
    """, (user_id,))
    
    report = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return report
