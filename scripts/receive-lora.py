#!/usr/bin/python3

import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_rfm9x
import json

print('Setting up LoRa Receiver...')

CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
rfm9x.tx_power = 13
prev_packet = None

print('Listening on 915MHz for packets...')

led = DigitalInOut(board.D26)
led.direction = Direction.OUTPUT

while True:
    packet = None
    try:
        packet = rfm9x.receive()
    except:
        print('Error receiving')
    if packet is not None:

        prev_packet = packet
        try:
            packet_text = json.loads(prev_packet)
            packet_dict = json.loads(list(packet_text.keys())[0])
            led.value = True
            print(packet_dict)
            time.sleep(.5)
            led.value = False
        except:
            pass
 
    time.sleep(1)

while True:
    packet = None
    try:
        packet = rfm9x.receive()
    except:
        print('Error receiving')
    if packet is not None:

        prev_packet = packet
        try:
            packet_text = str(prev_packet, "utf-8")
            print('RX: ' + packet_text)
        except:
            pass
 
    time.sleep(1)