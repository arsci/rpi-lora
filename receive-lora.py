import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_ssd1306
import adafruit_rfm9x
 
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 23
prev_packet = None
 
while True:
    packet = None
    try:
        packet = rfm9x.receive()
    except:
        print('Error receiving')
    if packet is None:
        print('Waiting for packet')
    else:
        prev_packet = packet
        packet_text = str(prev_packet, "utf-8")
        print('RX: ' + packet_text)
        time.sleep(1)
 
    time.sleep(0.1)