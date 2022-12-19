import random
import string
import sqlite3

# Create an empty list to store the strings
strings_list = []

# Generate 400 unique 4-letter strings in uppercase that don't contain the letter "E"
while len(strings_list) < 400:
    # Generate a random 4-letter string in uppercase
    s = ''.join(random.choices(string.ascii_uppercase.replace("E", ""), k=4))

    # Check if the string doesn't already exist in the list
    if s not in strings_list:
        # If it doesn't, add it to the list
        strings_list.append(s)

# Create a list of integers from 1 to 76
sites = list(range(1, 77))

# Connect to the database in the downloads folder
downloads_folder = 'D:\PROJECTS\IMMRSE SCRIPTS'
db_file = f'{downloads_folder}/test5.db'
conn = sqlite3.connect(db_file)

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Iterate over the list of sites
for site in sites:
    # Generate the table name based on the site value
    table_name = "IM" +"_" +"22"+ "_0" + str(site)

    # Create the table for the site if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS {} (code TEXT, barcode TEXT)".format(table_name))

    # Iterate over the list of strings
    for s in strings_list:
        # Insert two records for each string into the table, with the code and barcode columns
        cursor.execute("INSERT INTO {} (code, barcode) VALUES (?, ?)".format(table_name), (s, s))
        cursor.execute("INSERT INTO {} (code, barcode) VALUES (?, ?)".format(table_name), (s, s))

# Commit the changes to the database
conn.commit()


# Get a list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Iterate over the list of tables
for table in tables:
    # Get the name of the table
    table_name = table[0]

    # Update the code column to NULL for every second row in the table
    cursor.execute("UPDATE {} SET code = NULL WHERE (rowid % 2) = 1".format(table_name))

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
