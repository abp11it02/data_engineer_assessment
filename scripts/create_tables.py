import mysql.connector

conn = mysql.connector.connect(host = "127.0.0.1", port = 3306, user = "db_user" , password = "6equj5_db_user")
cur  = conn.cursor()

cur.execute("show databases;")
filepath = "../data/fake_property_data_new.json"
with open(filepath, 'r') as file:
    sql_script = file.read()
statements = [stmt.strip() for stmt in sql_script.split(';')]
print(statements)
print(cur.fetchall())

cur.close()
conn.close()