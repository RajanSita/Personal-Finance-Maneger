from db import connect
import hashlib
import mysql.connector

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    connection = connect()
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO Users (username, password)
        VALUES (%s, %s);
        """, (username, hash_password(password)))
        connection.commit()
        print("User registered successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def login(username, password):
    connection = connect()
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
        SELECT user_id, password FROM Users WHERE username = %s;
        """, (username,))
        
        user = cursor.fetchone()
        if user and user[1] == hash_password(password):
            print("Login successful.")
            return user[0]
        else:
            print("Invalid username or password.")
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        connection.close()
