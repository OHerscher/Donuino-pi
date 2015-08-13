import MySQLdb
import serial
ser = serial.Serial('/dev/ttyACM0', baudrate=57600, timeout=10)
db = MySQLdb.connect('localhost', 'Dronuino', 'R6vf5FcdFwMj9JPF', 'GPS')
cur = db.cursor()
while 1:
	com = raw_input("Test ")
	ser.write(com)
	rcv = ser.read(9999).strip("\r\n")
	print rcv
	list = rcv.split(',')	
	print 'list[0]:', list[0]
 	print 'list[1]:', list[1]
 	print 'list[2]:', list[2]
 	print 'list[3]:', list[3]
	lat = float(list[0])
	lon = float(list[1])
	alt = float(list[2])
	vit = float(list[3])
	print type(lat)
	print type(lon)
	print type(alt)
	print type(vit)
	try:
		SQL = "INSERT INTO Data VALUES ('%f', '%f', '%f', '%f')" % (lat, lon, alt, vit)
		print SQL
		cur.execute(SQL)
		db.commit()
	except:
		db.rollback()
db.close()

