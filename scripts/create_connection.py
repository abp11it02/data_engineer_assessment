import mysql.connector
from mysql.connector import Error
from create_tables import create_tables
from load_table import load_tables

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="db_user",
        password="6equj5_db_user",
        database="home_db"
    )
    
    if conn.is_connected():
        print("Successfully connected to MySQL database")
        cur = conn.cursor()
        create_tables(cur)
        load_tables(cur)
        conn.commit()

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cur.close()
        conn.close()
        print("MySQL connection closed")