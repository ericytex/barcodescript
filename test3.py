import string
import random
import sqlite3

# Connect to the database
downloads_folder = 'D:\PROJECTS\IMMRSE SCRIPTS'
db_file = f'{downloads_folder}/strings.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create the table for each site
for site in range(1, 38):
    cursor.execute(f'''
        CREATE TABLE site_{site} (string text)
    ''')

# Generate 400 unique strings without the letter "E" for each site
for site in range(1, 38):
    generated_strings = set()
    while len(generated_strings) < 400:
        s = ''.join(random.choices(string.ascii_uppercase.replace('E', ''), k=4))
        generated_strings.add(s)

    # Insert the strings into the table for each site
    for s in generated_strings:
        cursor.execute(f'''
            INSERT INTO site_{site} (string) VALUES (?)
        ''', (s,))

# Save the changes and close the connection
conn.commit()
conn.close()
