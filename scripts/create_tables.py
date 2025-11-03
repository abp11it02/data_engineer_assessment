from mysql.connector import Error
import os


def create_tables(cur):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    filepath = os.path.join(parent_dir, "sql", "create_table.sql")
    try:
        with open(filepath, 'r') as file:
            # Read SQL file content
            sql_script = file.read()
            
            # Split into individual statements and filter out empty ones
            statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip()]
            
            # Execute each statement
            for statement in statements:
                if statement and not statement.isspace():
                    print(f"Executing: {statement[:100]}...") # Print first 100 chars of statement
                    cur.execute(statement)
                    print("Statement executed successfully")
                else:
                    print("Skipping empty statement")
                
    except FileNotFoundError:
        print(f"SQL file not found at: {filepath}")
    except Error as err:
        print(f"MySQL Error: {err}")
