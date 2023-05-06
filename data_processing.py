from main import *
def checkbox_hanfeling(checkboxes_values):

    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

    if 0 in checkboxes_values:
        #serial write 1
        ser.write(b'1')
        if DEBUGGING:
            print("data_processing value sent on serial: 1")
    else:
        #serial write 0
        ser.write(b'2')
        if DEBUGGING:
            print("data_processing value sent on serial: 0")

    if 1 in checkboxes_values:
        #serial write 2
        ser.write(b'3')
        if DEBUGGING:
            print("data_processing value sent on serial: 3")
    else:
        #serial write 0
        ser.write(b'4')
        if DEBUGGING:
            print("data_processing value sent on serial: 4")
    if 2 in checkboxes_values:
        #serial write 3
        ser.write(b'5')
        if DEBUGGING:
            print("data_processing value sent on serial: 5")
    else:
        #serial write 0
        ser.write(b'6')
        if DEBUGGING:
            print("data_processing value sent on serial: 6")
    if 3 in checkboxes_values:
        #serial write 4
        ser.write(b'7')
        if DEBUGGING:
            print("data_processing value sent on serial: 7")
    else:
        #serial write 0
        ser.write(b'8')
        if DEBUGGING:
            print("data_processing value sent on serial: 8")
    if 4 in checkboxes_values:
        #serial write 5
        ser.write(b'9')
        if DEBUGGING:
            print("data_processing value sent on serial: 9")
    else:
        #serial write 0
        ser.write(b'0')
        if DEBUGGING:
            print("data_processing value sent on serial: 0")
    if 5 in checkboxes_values:
        #serial write 6
        ser.write(b'5')
        ser.write(b'7')
        ser.write(b'9')
        if DEBUGGING:
            print("data_processing value sent on serial: 5")
            print("data_processing value sent on serial: 7")
            print("data_processing value sent on serial: 9")
    else:
        ser.write(b'6')
        ser.write(b'8')
        ser.write(b'0')
        if DEBUGGING:
            print("data_processing value sent on serial: 6")
            print("data_processing value sent on serial: 8")
            print("data_processing value sent on serial: 0")
    #if 6 in checkboxes_values:
     #   #serial write 7
      #  ser.write(b'7')
       # if DEBUGGING:
        #    print("data_processing value sent on serial: 7")
    if 7 in checkboxes_values:
        #serial write 8
        ser.write(b'c')
        if DEBUGGING:
            print("data_processing value sent on serial: c")
    else:
        #serial write 0
        ser.write(b'd')
        if DEBUGGING:
            print("data_processing value sent on serial: d")