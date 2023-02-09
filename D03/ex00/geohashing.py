#!/usr/bin/python3

import sys 
import antigravity

def check_args():
    if len(sys.argv) != 4:
        sys.exit("Error: Wrong number of arguments! The program needs 3 arguments:\
        [latitude] [longitude] [yyyy-mm-dd-Dow Jones opening price on date]")
    if sys.argv[3].replace('-', '').replace('.', '').isnumeric() is False:
        sys.exit("Error: Wrong element in date parameter")

def check_num(latitude, longitude):
    if latitude < -90.0 or latitude > 90.0:
        sys.exit("Error: The value of latitude must be betweet -90.0 and 90.0.")
    if longitude < -180.0 or longitude > 180.0:
        sys.exit("Error: The value of longitude must be betweet -180.0 and 180.0.")

def geohashing():
    try:
        check_args()
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        dow_opening = bytes(sys.argv[3], 'ascii')
        check_num(latitude, longitude)
        # Specific code for geohashing
        antigravity.geohash(latitude, longitude, dow_opening)

    except ValueError:
            sys.exit("Error: Could not convert string to float")

if __name__ == '__main__':
    geohashing()
