import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rajansita@05",
        database="your_database"
    )

def create_tables():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Expenses (
        expense_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        amount DECIMAL(10, 2),
        category VARCHAR(255),
        date DATE,
        description TEXT,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Budgets (
        budget_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        category VARCHAR(255),
        amount DECIMAL(10, 2),
        start_date DATE,
        end_date DATE,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    """)
    
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_tables()