import serial
import time
import csv
from serial.tools import list_ports

#displays ports to terminal to find which arduino is connected to
ports = list_ports.comports()
for port in ports: print(port)

#creates a data file
f = open('data.csv', 'w',newline='')
f.truncate()

#sets com port
serialCom = serial.Serial('/dev/ttyACM0', 9600)

#resets arduino
serialCom.setDTR(False)
time.sleep(1)
serialCom.flushInput()
serialCom.setDTR(True)

kmax = 5 #number of data points
for k in range(kmax):
    try:
        #reads line
        s_bytes = serialCom.readline()
        #decodes binary
        decoded_bytes = s_bytes.decode("utf-8").strip('\r\n')


        if k == 0:
            values = [x for  x in decoded_bytes.split(',')]
        else:
            values = [float(x) for x in decoded_bytes.split(' ')]
        print (values)


        writer = csv.writer(f,delimiter=',') #delimiter is supposed to separate elements in a list by , but sensor is only giving one value at moment
        writer.writerow(values) # convert values to list because writerow function


    except:
        print("error")


f.close()

