import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# connect to data in web
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    webtoons = conn.execute('SELECT * FROM webtoons').fetchall()
    conn.close()
    return render_template('index.html', webtoons=webtoons)

@app.route('/add', methods=['POST'])
def add_webtoon():
#input info from form 
   name = request.form['name']
   rating = request.form['rating']
   comment = request.form['comment']

   conn = get_db_connection()

#save info in database
   conn.execute('INSERT INTO webtoons (name, rating, comment) VALUES (?, ?, ?)', (name, rating, comment))
   conn.commit()
   conn.close()

   return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
