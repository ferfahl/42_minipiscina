#!/usr/bin/python3

import sys 
import antigravity

def check_args():
    if len(sys.argv) != 4:
        sys.exit("Wrong number of arguments!\n\
        The program needs 3 arguments:\n\
        [latitude] [longitude] [yyyy-mm-dd-Dow Jones opening price on date]")

def check_num(latitude, longitude):
    if latitude < -90.0 or latitude > 90.0:
        sys.exit("Error: latitude must be betweet -90.0 and 90.0.")
    if longitude < -180.0 or longitude > 180.0:
        sys.exit("Error: longitude must be betweet -180.0 and 180.0.")

def geohashing():
    try:
        check_args()
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        dow_opening = bytes(sys.argv[3], 'ascii')
        check_num(latitude, longitude)

        antigravity.geohash(latitude, longitude, dow_opening)

    except ValueError:
            sys.exit("Error: could not convert string to float")
    # -37.88365 144.73438 2021-12-19-35365.44


if __name__ == '__main__':
    geohashing()
