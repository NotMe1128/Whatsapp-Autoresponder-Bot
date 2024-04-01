import mysql.connector
from mysql.connector import Error
import json
import atexit

USER_TABLES_FILE = 'user_tables.json'

# Function to load user tables from the JSON file
def load_user_tables():
    try:
        with open(USER_TABLES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save user tables to the JSON file
def save_user_tables(user_tables):
    with open(USER_TABLES_FILE, 'w') as file:
        json.dump(user_tables, file, indent=4)

# Establish a database connection at the top level of the script
try:
    connection = mysql.connector.connect(
        host='host url',
        port=3306,
        database='db',
        user='user',
        password='pass'
    )
    cursor = connection.cursor()
except Error as e:
    print(f"Error: {e}")

# Ensure that the connection is closed properly when the script ends
def close_connection():
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

atexit.register(close_connection)

# Load the initial user tables data
user_tables = load_user_tables()

# Function to execute a query
def execute_query(query, sender):
    try:
        result="Unknown Failure"
        #cursor.execute(query)
        if query.strip().split()[0].lower() == 'create':
            table_name = query.split()[2]
            if sender in user_tables:
                if len(user_tables[sender]) < 5:
                    cursor.execute(query)
                    result="Table Created."
                    user_tables[sender].append(table_name)
                else:
                    result="You have reached the limit of 5 tables."
            else:
                user_tables[sender] = [table_name]
        elif query.strip().split()[0].lower() == 'select':
            cursor.execute(query)
            result=cursor.fetchall()
        else:
            cursor.execute(query)
            result="Query Successful."
        connection.commit()
        save_user_tables(user_tables)
        return result
    except Error as e:
        return f"Error: {e}"

# Function to process a request
def process_request(message, sender):
    if message.startswith('!db query'):
        try:
  
            query = ' '.join(message.split(' ')[2:])
            command = query.split()[0].lower()
            print(command)
            if command not in ['create', 'delete', 'update', 'select', 'insert']:
                return "Missing permission."

            '''table_name = query.split()[2] if command == 'create' else query.split()[3]
            if command != 'create' and (sender not in user_tables or table_name not in user_tables[sender]):
                return "You do not have permission to perform this action on this table."'''
            return execute_query(query, sender)
        except Exception as e:
            return f"{e}"

