from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy credentials (for demo)
USERNAME = "admin"
PASSWORD = "1234"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        return "<h2>Login Successful ?</h2>"
    else:
        return "<h2>Invalid Username or Password ?</h2>"

if __name__ == '__main__':
    app.run(debug=True)
