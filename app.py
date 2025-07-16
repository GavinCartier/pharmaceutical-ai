from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='static')
app.secret_key = 'your-secret-key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_users'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/home")
def home():
    return render_template("index.html")

# Login handler
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        pwd = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT username, password FROM tbl_ubers WHERE username = %s", [username])
        user = cur.fetchone()
        cur.close()
        if user and pwd == user['password']:
            session['username'] = user['username']
            return redirect(url_for('home'))
        else:
            return render_template("register.html", error="Invalid username or password")
    return render_template("register.html")
# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
