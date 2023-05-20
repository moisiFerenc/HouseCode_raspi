#####################################################################
#  author: Ferenc Moisi
# 
#  date   : 2023. 04. 20.
# 
#  version: 0.1
# 
#  description:
#   This is a simple web application that allows users to log in and
#    register. The application is based on Flask.
#    The application uses SQLite database. 
#    
# 
#
#####################################################################

from flask import Flask, render_template, request , redirect , url_for , session
import time
import serial
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import data_processing
from pyngrok import ngrok

#DEBUG MODE
DEBUGGING = True
DEBUGGING_1 = True
WORD_WIDE_FLAG = False

# read the string from the arduino
RAWmessage = " "
massage = [0] * 5

#serial communication initialization
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(3)
print("serial communication initialized")


app = Flask(__name__)

app.secret_key = 'password'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'housecode'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'houselogin'

mysql = MySQL(app)


def readArduino():
    if DEBUGGING_1:
        for i in range(5):
            massage[i] = 2
    else:
        if ser.inWaiting() > 0:
            line = ser.readline()
            line = str(line)
            line = line[2:-5]
            line = line.split("--")
            for i in range(5):
                massage[i] = line[i]





@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        if DEBUGGING:
            print("DEBUGGING: request.method == POST and username in request.form and password in request.form")
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            if DEBUGGING:
                print("DEBUGGING: account")
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'

            return redirect(url_for('controlpanel'))
        else:
            if DEBUGGING:
                print("DEBUGGING: else")
            msg = 'Incorrect username / password !'
    if DEBUGGING:
        print(request.method)
    return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route("/managment")
def manage(debug=True):
    return render_template("manage.html")

@app.route('/register', methods =['POST', 'GET'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        if DEBUGGING:
            print("DEBUGGING: register.method == POST and username in request.form and password in request.form and email in request.form")
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            if DEBUGGING:
                print("DEBUGGING: account")
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            if DEBUGGING:
                print("DEBUGGING: email")
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            if DEBUGGING:
                print("DEBUGGING: username")
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            if DEBUGGING:
                print("DEBUGGING: not username or not password or not email")
            msg = 'Please fill out the form !'
        else:
            if DEBUGGING:
                print("DEBUGGING: else")
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        if DEBUGGING:
            print("DEBUGGING: request.method == POST")
        msg = 'Please fill out the form !'

    if DEBUGGING:
        print("DEBUGGING: return render_template('register.html', msg = msg)")
        print(request.method)
    return render_template('register.html', msg = msg)

@app.route("/controlpanel")
def controlpanel(debug=True):

    if session['username'] == None:
        return '<h1>Acces denied</h1>'

    readArduino()

    photo_resistor_val = massage[0]
    temperature_val = massage[1]
    humidity_sensor = massage[2]
    air_conditioner_state = massage[3]
    solar_panel_state = massage[4]

    return render_template('controlpanel.html',user=session['username'],temperature_var=temperature_val ,humidity_sensor=humidity_sensor,photo_resistor_val=photo_resistor_val,solar_panel_state_var=solar_panel_state)

@app.route("/checkboxes", methods=['POST'])
def handle_checkboxes():
    if DEBUGGING:
        print(request.form.getlist('my_checkbox'))
    my_checkbox = request.form.getlist('my_checkbox')
    data_processing.checkbox_hanfeling(my_checkbox)

    return ''

if __name__ == "__main__":
    if WORD_WIDE_FLAG:
        url = ngrok.connect(5001, "http", bind_tls=True)  # Connect ngrok to port 5001 with HTTPS
        print(f"ngrok URL: {url}")
    app.run(host='0.0.0.0', port=5001)

