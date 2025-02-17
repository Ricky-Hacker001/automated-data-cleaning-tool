import mysql.connector
from datetime import datetime

def log_cleaned_file(file_name):
    """Log the cleaned file name and timestamp in the database."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Replace with your MySQL password
        database="data_cleaning"
    )
    cursor = conn.cursor()

    # Create the table to store file logs if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS file_logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        file_name VARCHAR(255) NOT NULL,
        cleaned_at DATETIME NOT NULL
    )
    """
    cursor.execute(create_table_query)

    # Insert the file name and timestamp
    insert_query = "INSERT INTO file_logs (file_name, cleaned_at) VALUES (%s, %s)"
    cursor.execute(insert_query, (file_name, datetime.now()))

    conn.commit()
    conn.close()
