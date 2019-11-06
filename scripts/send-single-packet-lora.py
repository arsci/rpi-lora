import time
import datetime
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
import argparse
import sys

def main(data_send):
    print('Starting')
    CS = DigitalInOut(board.CE1)
    RESET = DigitalInOut(board.D25)
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
    rfm9x.tx_power = 23
    prev_packet = None

    print("TX: " + data_send)

    data = bytes(data_send,"utf-8")
    rfm9x.send(data)

    print("Packet Sent")

    sys.exit(0)

if __name__ == '__main__':

    main(sys.argv[1])

    sys.exit(0)