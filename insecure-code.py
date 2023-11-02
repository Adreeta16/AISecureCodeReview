import sqlite3

def insecure_code():
    # Insecure: Hardcoded password
    password = "my_password"
    print(f"Password is: {password}")

    # Insecure: Hardcoded secret key
    secret_key = "super_secret_key"
    print(f"Secret key is: {secret_key}")

    # Insecure: Using unsanitized user input in an SQL query
    user_input = input("Enter a name: ")
    conn = sqlite3.connect("mydb.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")
    results = cursor.fetchall()
    print("Results:", results)

insecure_code()
