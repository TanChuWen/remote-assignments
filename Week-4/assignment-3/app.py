from flask import Flask, render_template, request, redirect, url_for
import pymysql

#initialize Flask application
app = Flask(__name__)

#connect to MySQL database connection
mydb = pymysql.connect(  
    host = "localhost",
    user = "root",
    passwd = "lisatanrocks308",
    database = "assignment",
)

my_cursor = mydb.cursor() 

#create user table if not exists
my_cursor.execute("CREATE TABLE IF NOT EXISTS user (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), password VARCHAR(255))")


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    # Get the value of the clicked button (login or signup)
    action = request.form.get('action')

    if action == 'login':
        # Handle login logic
        email = request.form.get('email')
        password = request.form.get('password')
        my_cursor.execute("SELECT * FROM user WHERE email=%s AND password=%s",(email,password))

        user = my_cursor.fetchone()
        if user:
            return render_template('member.html', result='Login successful!')
        else:
            return render_template('home.html', result='Invalid email or password. Please try again.')

       
    elif action == 'signup':
        # Handle signup logic
        email = request.form.get('email')
        password = request.form.get('password')
        #check if email already exists
        my_cursor.execute("SELECT * FROM user WHERE email=%s",(email,))

        existing_user = my_cursor.fetchone()
        if existing_user:
            return render_template('home.html', result='Email already exists. Please use a different email.')
        else:
            my_cursor.execute("INSERT INTO user(email, password) VALUE(%s,%s)", (email, password))
            mydb.commit()
            return render_template('member.html', result='Signup successful!')
    else:
        # Handle unexpected or no button click
        return "Invalid form submission"

if __name__ == '__main__':
    app.run(debug=True)