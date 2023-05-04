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
from flask_login import UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy
import time
import multiprocessing as mp
import serial
import flask_bcrypt as Bcrypt
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
# read the string from the arduino
RAWmessage = " "
massage = [0] * 12





def readArduino():
    if __name__ == '__main__':
        for i in range(12):
            massage[i] = 2
    else:
        ser = serial.Serial('COM10', 9600)
        #while True:
        if ser.inWaiting() > 0:
            line = ser.readline()
            line = str(line)
            line = line[2:-5]
            line = line.split("--")
            for i in range(12):
                massage[i] = line[i]




app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your password'
app.config['MYSQL_DB'] = 'geeklogin'

mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('controlpanel.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
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

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route("/controlpanel")
def controlpanel(debug=True):
    readArduino()

    ultrasonic_sensor_val = massage[0]
    photo_resistor_val = massage[1]
    temperature_val = massage[2]
    humidity_sensor = massage[3]
    temperature_F_val = massage[4]
    lamp_1_state = massage[5]
    lamp_2_state = massage[6]
    lamp_3_state = massage[7]
    air_conditioner_state = massage[8]
    garage_door_state = massage[9]
    door_state = massage[10]
    solar_panel_state = massage[11]
    return render_template("controlpanel.html", ultrasonic_sensor_var = ultrasonic_sensor_val, humidity_sensor = humidity_sensor,  photo_resistor_var = photo_resistor_val, temperature_F_var = temperature_F_val, temperature_var = temperature_val, lamp_1_state_var = lamp_1_state, lamp_2_state_var = lamp_2_state,  lamp_3_state_var = lamp_3_state, air_conditioner_state_var = air_conditioner_state, garage_door_state_var = garage_door_state, door_state_var = door_state, solar_panel_state_var = solar_panel_state)

@app.route("/checkboxes", methods=['POST'])
def handle_checkboxes():
    checkboxes_values = request.form.getlist('my_checkbox')
    for value in checkboxes_values:
        print(value)
    return ''

if __name__ == "__main__":
    app.run(debug=True)

