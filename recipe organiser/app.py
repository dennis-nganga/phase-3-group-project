import sqlite3

# Connect to a new SQLite database (will create if it doesn't exist)
conn = sqlite3.connect('recipes.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute SQL command to create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
