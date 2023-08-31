import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from datetime import datetime
from ubidots import ApiClient
import time


def times_now():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S -  %d/%m/%Y")
	return current_time



rfid = SimpleMFRC522()
api=ApiClient(token="BBFF-OHSRRigalIWGRTrTLtYTYxjNCP8v32")
var=api.get_variable('64f022b15e1153000e37f63b')
while 1:
	print("place your card")
	id, text = rfid.read()
	print(id)
	#print(text)
	if(id==910177607415):
		name="mayur"
		usn="4mc20cs123"
		place="hassan"
		mobno="9844742000"
		response = var.save_value({"value":1,"context":{"name":name,"usn":usn,"place":place,"mobno":mobno,"time":times_now()}})
	elif(id==348548580654):
		name="ranjan"
		usn="4mc20cs567"
		place="mysore"
		mobno="9900743643"
		response = var.save_value({"value":1,"context":{"name":name,"usn":usn,"place":place,"mobno":mobno,"time":times_now()}})
	elif(id==906304495163):
		name="dhanush"
		usn="4mc20cs890"
		place="goa"
		mobno="9844732205"
		response = var.save_value({"value":1,"context":{"name":name,"usn":usn,"place":place,"mobno":mobno,"time":times_now()}})
	elif(id==978765164252):
		name="arjun"
		usn="4mc20cs534"
		place="ooty"
		mobno="9844032205"
		response = var.save_value({"value":1,"context":{"name":name,"usn":usn,"place":place,"mobno":mobno,"time":times_now()}})
	elif(id==900618454637):
		name="jeevan"
		usn="4mc20cs699"
		place="hubli"
		mobno="9741423034"
		response = var.save_value({"value":1,"context":{"name":name,"usn":usn,"place":place,"mobno":mobno,"time":times_now()}})
