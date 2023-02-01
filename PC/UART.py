import serial
import socket 
from time import sleep

def xor(a, b):
 
   
    result = []
 
    
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
 
    return ''.join(result)
 
 

def mod2div(dividend, divisor):
 
   
    pick = len(divisor)
 
   
    tmp = dividend[0 : pick]
 
    while pick < len(dividend):
 
        if tmp[0] == '1':
 
            
            tmp = xor(divisor, tmp) + dividend[pick]
 
        else: 
 
          
            tmp = xor('0'*pick, tmp) + dividend[pick]
 
      
        pick += 1
 
   
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
 
    checkword = tmp
    return checkword
 

def encodeData(data, key):
 
    l_key = len(key)
 
   
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
 
    
    codeword = data + remainder
    return codeword   
     
  
 

port = 'COM1'       
ser = serial.Serial(port, 9600)

input_string = input("Enter data you want to send->")
data =(''.join(format(ord(x), 'b') for x in input_string))
print("Entered data in binary format :",data)
key = "1001"
 
ans = encodeData(data,key)
print("Encoded data to be sent to server in binary format :",ans)
ser.write(ans.encode())
 

print("Received feedback from server :",ser.read(1024))

ser.close()