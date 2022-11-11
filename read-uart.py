import serial 
import time 

ser = serial.Serial(
    port='/dev/ttyS0', # Make sure that you have your pi connected in uart mode or will not read 
    baudrate =9600,           
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

time.sleep(1) 
while True: 
	try:
		output = ser.readline()
		if output:
			print(output)
		time.sleep(0.5)

	except Exception:
		pass

#for better understanding found this  useful video on youtube channel https://www.youtube.com/watch?v=oevxqPk78sM