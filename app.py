from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('waitlist.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS waitlist (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/waitlist', methods=['GET', 'POST'])
def waitlist():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        conn = sqlite3.connect('waitlist.db')
        c = conn.cursor()
        c.execute("INSERT INTO waitlist (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()

        return render_template('waitlist.html', success=True)

    return render_template('waitlist.html')

if __name__ == '__main__':
    app.run(debug=True)
