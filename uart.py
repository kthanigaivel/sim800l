from machine import UART,Pin
import time
uart=UART(0,baudrate=9600,tx=Pin(0),rx=Pin(1))

def writedata(command):
    TERMINATION_CHAR = '\n\r'
    rxData=bytes()
    uart.write(b''+command+ b'' + TERMINATION_CHAR)
    time.sleep(0.1)
    while uart.any()>0:
        rxData += uart.readline()
    print(rxData.decode('utf-8'))
#CONNECTION SUCCESS IF RETURN OK
writedata('AT')


writedata('ATA')
 
