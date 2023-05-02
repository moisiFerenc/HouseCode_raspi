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
from my_project import app, db
from flask import Flask, render_template, request, redirect, url_for, flash,abort
from flask_login import UserMixin, LoginManager, login_manager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from my_project.models import User
from my_project.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
import time
import multiprocessing as mp
import serial
import flask_bcrypt as Bcrypt

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







@app.route("/")
def welcome(debug=True):
    return render_template("welcome.html")

@app.route("/login", methods=['GET', 'POST'])
def login(debug=True):
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Login Success!")
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('controlpanel')
            return redirect(next)
    return render_template("login.html", form=form)

@app.route("/managment")
def manage(debug=True):
    return render_template("manage.html")

@app.route("/register", methods=['GET', 'POST'])
def register(debug=True):
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registration!")
        return redirect(url_for('login'))

    return render_template("register.html", form=form)



@app.route("/controlpanel")
@login_required
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

@app.route("/logut")
@login_required
def logout():
    logout_user()
    flash("You logged out!")
    return redirect(url_for('welcome'))


if __name__ == "__main__":
    app.run(debug=True)

