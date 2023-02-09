#!/bin/sh

python3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68
python3 geohashing.py 37.421542 -122.085589 2005-05-26-104538.68
echo ""

#errors
echo "Too few args"
python3 geohashing.py 37.421542 -122.085589
python3 geohashing.py

echo "Too many args"
python3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68 'hello world'

echo "Wrong parameters"
python3 geohashing.py 'hello world' -122.085589 2005-05-26-10458.68
python3 geohashing.py 37.421542 -122.085589 'hello world'
python3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.6ç
python3 geohashing.py 37421542 -122.085589 2005-05-26-10458.68
python3 geohashing.py 37.421542 -182.085589 2005-05-26-104538.68