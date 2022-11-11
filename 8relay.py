#!/usr/bin/python3
import RPi.GPIO as GPIO
import serial 
import time 
import struct

k=struct.pack('B', 0xff)

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate =9600,           
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Setting GPIO
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)


global tombol1_sts
global tombol2_sts
global tombol3_sts
global tombol4_sts
global tombol5_sts
global tombol6_sts
global tombol7_sts
global tombol8_sts



tombol1_sts=False
tombol2_sts=False
tombol3_sts=False
tombol4_sts=False
tombol5_sts=False
tombol6_sts=False
tombol7_sts=False
tombol8_sts=False

def red_button(obj_name):
	#print("Red Button")
	command = obj_name + '.bco=63488'
	ser.write(command.encode())
	ser.write(k)
	ser.write(k)
	ser.write(k)

def reset_button(obj_name):
	#print("Reset Button")
	command = obj_name + '.bco=48631'
	ser.write(command.encode())
	ser.write(k)
	ser.write(k)
	ser.write(k)


def text(str):
	command = 't0.txt="' + str + '"'
	ser.write(command.encode())
	ser.write(k)
	ser.write(k)
	ser.write(k)

#Reset button
reset_button('b0')
reset_button('b1')
reset_button('b2')
reset_button('b3')
reset_button('b5')
reset_button('b6')
reset_button('b7')
reset_button('b8')




time.sleep(0)

while True: 
	try:
		output = ser.readline()
		#Cek apakah ada trigger dari HMI
		if output:
			#print(output)
			#jika tombol1
			if output == b'e\x00\x01\x01\xff\xff\xff':
				print("Relay 1 was selected")
				if tombol1_sts==False:
					print("Relay 1 ON")
					#turn on relay1
					GPIO.output(23, 0)
					tombol1_sts = True
					#Change button to red
					red_button('b0')
					r1 = "1"
				else:
					#turn off relay1
					GPIO.output(23, 1)
					print("Relay 1 OFF")
					tombol1_sts = False
					#Reset button
					reset_button('b0')
					r1 = "0"
					
			if output ==b'e\x00\x02\x01\xff\xff\xff': 
				print("Relay 2 was selected")
				if tombol2_sts==False:
					print("Relay 2 ON")
					#turn on relay1
					GPIO.output(24, 0)
					tombol2_sts = True
					#Change button to red
					red_button('b1')
					r1 = "1"
				else:
					#turn off relay1
					GPIO.output(24, 1)
					print("Relay 2 OFF")
					tombol2_sts = False
					#Reset button
					reset_button('b1')
					r1 = "0"
					
			if output == b'e\x00\x03\x01\xff\xff\xff':
				print("Relay 3 was selected")
				if tombol3_sts==False:
					print("Relay 3 ON")
					#turn on relay3
					GPIO.output(27, 0)
					tombol3_sts = True
					#Change button to red
					red_button('b2')
					r3 = "1"
				else:
					#turn off relay3
					GPIO.output(27, 1)
					print("Relay 3 OFF")
					tombol3_sts = False
					#Reset button
					reset_button('b2')
					r3 = "0"
					
			if output ==b'e\x00\x04\x01\xff\xff\xff':
				print("Relay 4 was selected")
				if tombol4_sts==False:
					print("Relay 4 ON")
					#turn on relay4
					GPIO.output(22, 0)
					tombol4_sts = True
					#Change button to red
					red_button('b3')
					r4 = "1"
				else:
					#turn off relay4
					GPIO.output(22, 1)
					print("Relay 4 OFF")
					tombol4_sts = False
					#Reset button
					reset_button('b3')
					r4 = "0"
					
			
			if output == b'e\x00\x08\x01\xff\xff\xff':
				print("Relay 5 was selected")
				if tombol5_sts==False:
					print("Relay 5 ON")
					#turn on relay5
					GPIO.output(5, 0)
					tombol5_sts = True
					#Change button to red
					red_button('b5')
					r1 = "1"
				else:
					#turn off relay5
					GPIO.output(5, 1)
					print("Relay 5 OFF")
					tombol5_sts = False
					#Reset button
					reset_button('b5')
					r1 = "0"
			
			if output == b'e\x00\t\x01\xff\xff\xff':
				print("Relay 6 is selected")
				if tombol6_sts==False:
					print("Relay 6 ON")
					#turn on relay6
					GPIO.output(6, 0)
					tombol6_sts = True
					#Change button to red
					red_button('b6')
					r1 = "1"
				else:
					#turn off relay6
					GPIO.output(6, 1)
					print("Relay 1 OFF")
					tombol6_sts = False
					#Reset button
					reset_button('b6')
					r1 = "0"
			
			if output == b'e\x00\n':
				print("Relay 7 was selected")
				if tombol7_sts==False:
					print("Relay 7 ON")
					#turn on relay7
					GPIO.output(13, 0)
					tombol7_sts = True
					#Change button to red
					red_button('b7')
					r1 = "1"
				else:
					#turn off relay7
					GPIO.output(13, 1)
					print("Relay 7 OFF")
					tombol7_sts = False
					#Reset button
					reset_button('b7')
					r1 = "0"

			if output == b'e\x00\x0b\x01\xff\xff\xff':
				print("Relay 8 was selected")
				if tombol8_sts==False:
					print("Relay 8 ON")
					#turn on relay8
					GPIO.output(25, 0)
					tombol8_sts = True
					#Change button to red
					red_button('b8')
					r1 = "1"
				else:
					#turn off relay8
					GPIO.output(25, 1)
					print("Relay 8 OFF")
					tombol8_sts = False
					#Reset button
					reset_button('b8')
					r1 = "0"
			
			if output == b'e\x00\x05\x01\xff\xff\xff':
				print("All Relay are off")
				#Turn off All relays
				GPIO.output(23, 1)
				GPIO.output(24, 1)
				GPIO.output(27, 1)
				GPIO.output(22, 1)
				GPIO.output(5, 1)
				GPIO.output(6, 1)
				GPIO.output(13, 1)
				GPIO.output(25, 1)

				#Reset button
				reset_button('b0')
				reset_button('b1')
				reset_button('b2')
				reset_button('b3')
				reset_button('b5')
				reset_button('b6')
				reset_button('b7')
				reset_button('b8')

				tombol1_sts=False
				tombol2_sts=False
				tombol3_sts=False
				tombol4_sts=False
				tombol5_sts=False
				tombol6_sts=False
				tombol7_sts=False
				tombol8_sts=False
				
				
			


	except Exception:
		pass		



	except Exception:
		pass
GPIO.cleanup() 
e