import serial
from time import sleep

port = 'COM1'
ser = serial.Serial(port, 9600, timeout=1)
UART_BUFF_SIZE = 64

def calcCRC8(byte_arr):
    result = 0
    for byte in byte_arr:
        result ^= byte
    return result

def transmit(byte_arr):
    data = [byte for byte in byte_arr]
    crc8 = calcCRC8(byte_arr)
    data.append(crc8)
    ser.write(data)
    print(data)

def receive():
    data = [byte for byte in ser.read(UART_BUFF_SIZE)]
    crc8 = calcCRC8(data[:-1])
    if data[-1] != crc8:
        print('RECEIVE ERROR: Wrong CRC')
        return 0
    return data


input_string = input("Enter data you want to send->")
data = [int(x) for x in input_string]
print("Entered data in binary format :", data)

transmit(data)

print("Received feedback from server :", receive())

ser.close()