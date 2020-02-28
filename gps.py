#!/usr/bin/env python3
import serial
ser = serial.Serial( '/dev/ttyUSB0', 4800, timeout=5)
while 1:
	line = ser.readline()
	splitline = line.split(',')
	if splitline[0] == '$GPGSV':
		Heading = line#line[20]+line[21]+line[22]
		print(Heading)

