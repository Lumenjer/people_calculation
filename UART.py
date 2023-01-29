import serial
from time import sleep

ser = serial.Serial #( port name )    
while True:
    received_data = ser.read()             
    sleep(0.03)
    data_left = ser.inWaiting()             
    received_data += ser.read(data_left)
    print (received_data)                   
    ser.write(received_data)                