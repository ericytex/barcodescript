
#generate unique 4 letters 400 times in python and check if the strings dont repeat in uppercase and store the strings into a table in sqlite db in downloads folder
import string
import random
import sqlite3

# Connect to the database
downloads_folder = 'D:\PROJECTS\IMMRSE SCRIPTS'
db_file = f'{downloads_folder}/strings.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE strings (string text)
''')

# Generate 400 unique strings
generated_strings = set()
while len(generated_strings) < 400:
    s = ''.join(random.choices(string.ascii_uppercase.replace('E', ''), k=4))
    generated_strings.add(s)

# Insert the strings into the table
for s in generated_strings:
    cursor.execute('''
        INSERT INTO strings (string) VALUES (?)
    ''', (s,))

# Save the changes and close the connection
conn.commit()
conn.close()
