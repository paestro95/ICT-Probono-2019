from bluetooth import *
import RPi.GPIO as GPIO
import time
vi=18
rsw=23
red=24
green=25
print("G1")
GPIO.setwarnings (False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(vi,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #vib
GPIO.setup(rsw,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #but
GPIO.setup(red,GPIO.OUT) #LED_R
GPIO.setup(green,GPIO.OUT) #LED_G
print("G2")
i=0
brecv='p'
client_socket=BluetoothSocket(RFCOMM)
client_socket.connect(("98:D3:31:FD:63:A7",1))        
print("G3")
while True:
    recv = client_socket.recv(65535).decode('utf-8')
    result = GPIO.input(vi)
    sw = GPIO.input(rsw)
    if result > 0:
        client_socket.send('1')
        i=0
        GPIO.output(red,GPIO.HIGH)
        GPIO.output(green,GPIO.LOW)
        print("vi test")
    if sw > 0 :
        client_socket.send('1')
        GPIO.output(red,GPIO.HIGH)
        GPIO.output(green,GPIO.LOW)
        print("switch test")
    if recv == 'y' :
        print('wait')
    if recv == 'o' :
        GPIO.output(red,GPIO.LOW)
        GPIO.output(green,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(red,GPIO.LOW)
        GPIO.output(green,GPIO.LOW)
client_socket.close() 
