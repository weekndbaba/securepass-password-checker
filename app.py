from flask import Flask, render_template, request, redirect, url_for
import re
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Create DB on first run
def init_db():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            length INTEGER,
            strength TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def check_strength(password):
    length = len(password) >= 8
    digit = re.search(r"\d", password)
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([bool(length), bool(digit), bool(upper), bool(lower), bool(symbol)])

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        strength = check_strength(password)
        length = len(password)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to DB
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute('INSERT INTO history (length, strength, timestamp) VALUES (?, ?, ?)',
                  (length, strength, timestamp))
        conn.commit()
        conn.close()

        return render_template('index.html', strength=strength)

    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('SELECT * FROM history ORDER BY timestamp DESC')
    data = c.fetchall()
    conn.close()
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
