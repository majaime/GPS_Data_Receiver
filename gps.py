#!/usr/bin/env python3
import serial
ser = serial.Serial( '/dev/ttyUSB0', 4800, timeout=1)
while 1:
	line = ser.readline()
	splitline = line.split(',')
	if splitline[0] == '$GPGSV':
		Heading = line[20]
		print(Heading)
