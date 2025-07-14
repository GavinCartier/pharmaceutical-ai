# app.py
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/signin')
def signin():
    return render_template('components/signin.html')

@app.route('/register')
def register():
    return render_template('/components/register.html')

@app.route('/newproduct')
def newproduct(): 
    return render_template('components/newproduct.html')

@app.route('/controltable')
def controltable():
    return render_template('ctindex.html')

if __name__ == "__main__":
    app.run(debug=True)
