#!/usr/bin/python3

import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
 
CS = DigitalInOut(board.D16)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

respeak_cs = DigitalInOut(board.D5)
respeak_cs = True
 
for x in range(10):
    try:
        respeak_cs = True
        rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
        print('RFM9x: Detected')
    except RuntimeError:
        print('RFM9x: ERROR')
 
    time.sleep(0.5)