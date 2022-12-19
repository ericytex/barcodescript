import random
import sqlite3

# Connect to the database
downloads_folder = 'D:\PROJECTS\IMMRSE SCRIPTS'
db_file = f'{downloads_folder}/test6.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

array1 = []
array2 = []
array3 = []
array4 = []
array5 = []

# Generate the strings and add them to the arrays
for i in range(400):
    # Generate a random string
    string = ''.join(random.choices([chr(x) for x in range(65, 91) if chr(x) != 'E'], k=4))
    # Convert the string to uppercase
    string = string.upper()
    #add string to first array, if range is < 400 else restart the loop and add to second array and so on
    if len(array1) < 400:
        array1.append(string)
        break

    print (array1)



# Commit the changes and close the connection
conn.commit()
conn.close()
