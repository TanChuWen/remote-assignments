from flask import Flask, render_template, request, redirect, url_for
import pymysql
import ipdb

app = Flask(__name__)

mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "lisatanrocks308",
    database = "assignment",
)

my_cursor = mydb.cursor() 

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['password']
    # ipdb.set_trace() #in order to debug
    #check if email is not registered before
    my_cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
    mydb.commit()
    if my_cursor.fetchone() is None:
        my_cursor.execute("INSERT INTO user (email, password) VALUES (%s, %s)", (email, password))
        mydb.commit()
        return redirect(url_for('member', message='Welcome, {}!'.format(email)))
    else:
        return render_template('index.html', message='Email already registered')
    
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # check if the pair of email and password exists in the user table
    my_cursor.execute("SELECT * FROM user WHERE email=%s AND password=%s", (email, password))
    mydb.commit()
    if my_cursor.fetchone() is not None:
        return redirect(url_for('member', message='Welcome back, {}!'.format(email)))
    else:
        return render_template('index.html', message='Invalid email or password')


@app.route('/member') # If sign up/ log in successfully, show "Your access is permitted!"
def member():
    return render_template('member.html', message=request.args.get('message'))


if __name__ == "__main__":
    app.run(debug=True, port=3000)



