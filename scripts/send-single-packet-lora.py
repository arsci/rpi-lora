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
    CS = DigitalInOut(board.D16)
    RESET = DigitalInOut(board.D25)
    led = DigitalInOut(board.D26)
    led.direction = Direction.OUTPUT


    board_connect = False
    ctr = 0
    while (board_connect is False) and (ctr is not 30):
        try:
            print('Attempting RFM9X connection...')
            spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
            rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
            rfm9x.tx_power = 13
            prev_packet = None
            board_connect = True
            ctr = 0
        except:
            print('Board connection failed. Retry...')
            ctr = ctr + 1
            if(ctr is 30):
                print('Failed to connect to board. Skipping Data Send.')
            time.sleep(.5)
            
    connect = False

    while (connect is False) and (ctr is not 30):
        try:
            print("TX: " + data_send)
            data = bytes(data_send,"utf-8")
            print('Attempting RFM9X send...')
            rfm9x.send(data)
            connect = True
            led.value = True
            time.sleep(.5)
            led.value = False
            print("Packet Sent")
        except:
            print('Failed. Retry')
            ctr = ctr + 1
            time.sleep(.5)

    sys.exit(0)

if __name__ == '__main__':

    main(sys.argv[1])

    sys.exit(0)