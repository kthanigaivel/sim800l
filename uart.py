from machine import UART , Pin

TERMINATION_CHAR = '\x1a'

TXD_PIN = 'GP0'
RXD_PIN = 'GP1'

uart = UART(1, baudrate=9600, pins=(TXD_PIN, RXD_PIN))
 