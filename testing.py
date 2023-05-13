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
import data_processing

massage = [0] * 13
#serial communication initialization
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(3)
ser.reset_input_buffer()
print("serial communication initialized")
while True:
   if ser.inWaiting() > 0:
      line = ser.readline()
      line = str(line)
      line = line[2:-5]
      line = line.split("--")
      for i in range(13):
         massage[i] = line[i]
         print(massage)

