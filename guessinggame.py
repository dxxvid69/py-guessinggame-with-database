import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('guessing_game.db')
cursor = conn.cursor()

# Create a table to store guesses
cursor.execute('''CREATE TABLE IF NOT EXISTS guesses
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                guess INTEGER,
                correct INTEGER)''')
conn.commit()

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

# Game loop
while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    
    if user_guess == target_number:
        print("Congratulations! You guessed the correct number.")
        cursor.execute("INSERT INTO guesses (guess, correct) VALUES (?, 1)", (user_guess,))
        conn.commit()
        break
    else:
        print("Incorrect guess. Try again.")
        cursor.execute("INSERT INTO guesses (guess, correct) VALUES (?, 0)", (user_guess,))
        conn.commit()

# Display previous guesses
print("Previous guesses:")
cursor.execute("SELECT guess, correct FROM guesses")
previous_guesses = cursor.fetchall()
for guess, correct in previous_guesses:
    print(f"Guess: {guess}, Correct: {'Yes' if correct else 'No'}")

# Close the database connection
conn.close()


# MAKE SURE TO TYPE THIS IN SHELL 
# pip install sqlite3
