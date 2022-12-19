#generate unique 4 letters 400 times in python and check if the strings dont repeat in uppercase and store the strings into a table called allcodes in columns code once and barcode twice with comma in sqlite db in downloads folder

import random
import string
import sqlite3

# Connect to the database

downloads_folder = 'D:\PROJECTS\IMMRSE SCRIPTS'
db_file = f'{downloads_folder}/test4.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create the table
cursor.execute("CREATE TABLE allcodes (code TEXT, barcode TEXT)")

# Set up a list of all possible characters for the strings
characters = string.ascii_uppercase

# Initialize an empty set to store the generated strings
generated_strings = set()

# Loop 400 times
for i in range(400):
    # Generate a random 4-letter string
    new_string = ''.join(random.choices(characters, k=4))
    
    # Check if the string has already been generated
    if new_string in generated_strings:
        # If it has, skip this iteration and generate a new string
        continue
    else:
        # If it hasn't, add it to the set of generated strings
        generated_strings.add(new_string)
        
        # Insert a row into the table
        cursor.execute("INSERT INTO allcodes (code, barcode) VALUES (?, ?)", (new_string, f"{new_string}, {new_string}"))

# Commit the changes and close the connection
conn.commit()
conn.close()
