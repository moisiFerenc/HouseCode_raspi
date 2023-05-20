from main import *
def checkbox_hanfeling(checkboxes_values):



    if '0' in checkboxes_values:
        #serial write 1
        ser.write("1".encode('utf-8'))
        if DEBUGGING:
            print("msg sent to serial monitor:  1")
    else:
        #serial write 0
        ser.write("2".encode('utf-8'))
        if DEBUGGING:
            print("msg sent to serial monitor:  2")

    if '1' in checkboxes_values:
        # serial write 1
        ser.write("5".encode('utf-8'))
        if DEBUGGING:
            print("msg sent to serial monitor:  5")
    else:
        # serial write 0
        ser.write("6".encode('utf-8'))
        if DEBUGGING:
            print("msg sent to serial monitor:  6")

    if '2' in checkboxes_values:
        # serial write 1
        ser.write("7".encode('utf-8'))
        if DEBUGGING:
            print("msg sent to serial monitor:  7")
    else:
        # serial write 0
        ser.write("8".encode('utf-8'))
        if DEBUGGING:
            print("msg sent to serial monitor:  8")

    if '3' in checkboxes_values:
        # serial write 1
        ser.write("c".encode('utf-8'))
        if DEBUGGING:
            print("msg sent to serial monitor:  c")
    else:
        # serial write 0
        ser.write("d".encode('utf-8'))
        if DEBUGGING:
            print("msg sent to serial monitor:  d")