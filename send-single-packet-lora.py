import time
import datetime
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import adafruit_ssd1306
import adafruit_rfm9x

def main(args):

    CS = DigitalInOut(board.CE1)
    RESET = DigitalInOut(board.D25)
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
    rfm9x.tx_power = 13
    prev_packet = None

    data = bytes(args.data,"utf-8")
    rfm9x.send(data)

    return 0

def parse_args():
    
    parser = argparse.ArgumentParser(description='Send Packet')

    parser.add_argument('--data', type=str, nargs='+', help='Data to send over LORA')

if __name__ == "__main__":

    print('Preparing to send packet')
    
    args = parse_args()

    main(args)
    
    sys.exit(0)