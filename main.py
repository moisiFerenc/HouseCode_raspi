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

from flask import Flask, render_template
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import time
import multiprocessing as mp
import serial

# read the string from the arduino
RAWmessage = " "
massage = [0] * 12
#the message container is 11 bytes long

def readArduino():
    while True:
        if __name__ == '__main__':
            for i in range(12):
                massage[i] = 2
                time.sleep(1)
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
                    time.sleep(1)



app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret'


db.init_app(app)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(80))

@app.route("/login")
def index(debug=True):
    return render_template("login.html")

@app.route("/register")
def register(debug=True):
    return render_template("register.html")

@app.route("/controlpanel")
def controlpanel(debug=True):


    ultrasonic_sensor_val = massage[0]
    photo_resistor_val    = massage[1]
    temperature_val       = massage[2]
    humidity_sensor       = massage[3]
    temperature_F_val     = massage[4]
    lamp_1_state          = massage[5]
    lamp_2_state          = massage[6]
    lamp_3_state          = massage[7]
    air_conditioner_state = massage[8]
    garage_door_state     = massage[9]
    door_state            = massage[10]
    solar_panel_state     = massage[11]
    return render_template("controlpanel.html", ultrasonic_sensor_var = ultrasonic_sensor_val, humidity_sensor = humidity_sensor,  photo_resistor_var = photo_resistor_val, temperature_F_var = temperature_F_val, temperature_var = temperature_val, lamp_1_state_var = lamp_1_state, lamp_2_state_var = lamp_2_state,  lamp_3_state_var = lamp_3_state, air_conditioner_state_var = air_conditioner_state, garage_door_state_var = garage_door_state, door_state_var = door_state, solar_panel_state_var = solar_panel_state)



if __name__ == "__main__":
    # Osztott memória létrehozása
    massage = mp.Array('i', [0,0,0,0,0,0,0,0,0,0,0,0])

    # Szenzor olvasó folyamat elindítása
    p = mp.Process(target=readArduino, args=(massage,))
    p.start()

    # Flask alkalmazás futtatása
    app.run(debug=True)

