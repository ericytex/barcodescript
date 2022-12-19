import random
import string
import sqlite3

def generate_unique_string(conn, strings_table):
  # Generate a random 4-letter string using uppercase letters
  s = ''.join(random.choices(string.ascii_uppercase, k=4))
  # Check if the string has already been generated
  cursor = conn.cursor()
  cursor.execute(f"SELECT * FROM {strings_table} WHERE string=?", (s,))
  if cursor.fetchone() is not None:
    # If the string has already been generated, generate a new one
    return generate_unique_string(conn, strings_table)
  # If the string is unique, insert it into the database and return it
  cursor.execute(f"INSERT INTO {strings_table} (string) VALUES (?)", (s,))
  return s

# Connect to the database and create a table to store the strings
downloads_folder = 'D:\PROJECTS\IMMRSE SCRIPTS'
db_file = f'{downloads_folder}/strings.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE strings (id INTEGER PRIMARY KEY, string TEXT)''')

# Generate 400 unique 4-letter strings
strings_table = 'strings'
for i in range(400):
  s = generate_unique_string(conn, strings_table)

# Print the generated strings
cursor.execute(f"SELECT * FROM {strings_table}")
print(cursor.fetchall())
