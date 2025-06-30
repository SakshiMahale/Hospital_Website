from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# ✅ DB Initialization
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userid TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# ✅ Homepage with HTML form
@app.route('/')
def home():
    return render_template('SignUp.html')

# ✅ Save form data
@app.route('/register', methods=['POST'])
def register():
    userid = request.form['userid']
    email = request.form['email']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (userid, email) VALUES (?, ?)", (userid, email))
    conn.commit()
    conn.close()

    return f"<h3>Thank you, {userid}! Your data is saved.</h3><a href='/'>Back</a>"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)