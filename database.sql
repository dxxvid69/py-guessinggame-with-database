cursor = conn.cursor()

# Create a table to store guesses
cursor.execute('''CREATE TABLE IF NOT EXISTS guesses
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                guess INTEGER,
                correct INTEGER)''')
conn.commit()
