import time
import datetime
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_ssd1306
import adafruit_rfm9x

CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 13
prev_packet = None
 
while True:
    packet = None
    data = bytes("LORA-1: " + str(datetime.datetime.now()),"utf-8")
    rfm9x.send(data)
    time.sleep(1)