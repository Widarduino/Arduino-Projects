import csv
import sys
from operator import length_hint
from time import sleep

import serial
import time

#RUN THIS SCRIPT 2ND AND THEN OPEN SERIAL MONITOR IN ARDUINO CODE

serialCom = serial.Serial('/dev/ttyACM0', 9600)

entire = []
LASTSTORE = ['']
length =0
lastrow = []

while True:

    with open('output.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        reader.__next__()

        for row in reader:
            lastrow = row

    store = '\n'.join(lastrow)
    entire.append(store)



    if LASTSTORE[0] != entire[-1]:
        time.sleep(0.5)
        byteinfo = bytes(entire[-1] + "\n", encoding='utf-8')
        print(byteinfo)
        serialCom.write(byteinfo)
        time.sleep(0.05)
        LASTSTORE[0] = entire[-1]
    else:
        pass





serialCom.close()



#modify code so that entire file is read,
#newest line is read instead