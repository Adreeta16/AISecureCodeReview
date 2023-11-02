import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name)

@app.route('/xss')
def xss():
    # Vulnerable to Cross-Site Scripting (XSS)
    user_input = request.args.get('input', '')
    return render_template_string('<p>User Input: {{ user_input }}</p>', user_input=user_input)

@app.route('/cors')
def cors():
    # Vulnerable to Cross-Origin Resource Sharing (CORS)
    response = app.make_response('')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/csrf')
def csrf():
    # Vulnerable to Cross-Site Request Forgery (CSRF)
    return render_template_string('<form action="https://evil.com/malicious-action" method="post"><input type="submit" value="Click me"></form>')

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

if __name__ == '__main__':
    insecure_code()
    app.run()
