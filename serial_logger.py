#!/usr/bin/env python

import serial
from datetime import datetime 

baudrate = 38400
port = '/dev/ttyUSB0'

ser = serial.Serial()
ser.baudrate = baudrate
ser.port = port

# ser.flushInput()
# ser.flushOutput()

ser.close()
ser.open()


while True:
    if ser.inWaiting():
        
        data_raw = ser.readline()
        # print(data_raw)

        with open('log.csv', 'a') as log_file :
            date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write('%s,%s\n'%(date,data_raw))

