#!/usr/bin/env python

import csv
import requests

time = '0000-00-00 00:00:00'
msg = ''
message = ''
change_flag = False
pre_temp = 60
j=0
url = 'http://exe.kandaidea.com:9898/api/NMEA/SendNMEA'

with open("log.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")

    for i, line in enumerate(reader):
        # print 'line[{}] = {}'.format(i, line)
        if line:
            if "!A" in line[0] or "!B" in line[0]:
                text = line[0]

                if "!A" in text:

                    ls = text.split('!A')
                    time = ls[0]
                    time = time[0:-1]
                    msg = "!A" + ls[1]
                    # print(time,msg)

                else:

                    ls = text.split('!B')
                    time = ls[0]
                    time = time[0:-1]
                    msg = "!B" + ls[1]
                    # print(time,msg)
                
                time_list = time.split(':')
                temp = time_list[1]
                if temp != pre_temp:
                    j+=1
                    pre_temp = temp
                    change_flag = True
                    # print(j)

                if not change_flag:
                    message = message + time + "|||" + msg + "/n"
                else:
                    # print(message)
                    
                    # print
                    change_flag = False

                    test = {'some':'text'}
                    x = requests.post(url, data = message, headers={"content-type":"text/plain"})
                    print(x.text)

                    message = ''
        # print(time,msg)
    # print(message)
            