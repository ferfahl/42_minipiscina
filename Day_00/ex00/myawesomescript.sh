#!/bin/sh
curl -s $1 | grep '"' | cut -d '"' -f 2
