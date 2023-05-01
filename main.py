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

from flask import Flask, render_template, request
from flask_login import UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy
import time
import multiprocessing as mp
import serial
import flask_bcrypt as Bcrypt

# read the string from the arduino
RAWmessage = " "
massage = [0] * 12

#bcrypt = Bcrypt(app) # create an instance of the class
bcrypt = Bcrypt.Bcrypt()

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


@app.route("/")
def login(debug=True):
    return render_template("login.html")

@app.route("/managment")
def manage(debug=True):
    return render_template("manage.html")

@app.route("/register")
def register(debug=True):
    return render_template("register.html")

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

