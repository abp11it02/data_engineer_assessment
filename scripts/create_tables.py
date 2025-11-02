import mysql.connector
import os

# conn = mysql.connector.connect(host = "127.0.0.1", port = 3306, user = "db_user" , password = "6equj5_db_user")
# cur  = conn.cursor()

# cur.execute("show databases;")
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
filepath = os.path.join(parent_dir, "sql", "create_table.sql")
with open(filepath, 'r') as file:
    sql_script = file.read()
statements = [stmt.strip() for stmt in sql_script.split(';')]
print(statements)
# print(cur.fetchall())

# cur.close()
# conn.close()
