import telepot
import RPi.GPIO as GPIO
import time

sw=7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sw,GPIO.IN,pull_up_down=GPIO.PUD_UP)

token = '6454083743:AAEVlXvMBYl-rTFiA5Ccl6mjdNEbsyn1O-M' # telegram token
receiver_id=625984250  # https://api.telegram.org/bot<TOKEN>/getUpdates

bot = telepot.Bot(token)
while 1:
	val=GPIO.input(sw)
	time.sleep(0.2)
	if (val==0):
		bot.sendMessage(receiver_id, 'Help me I am in Danger') # send a activation message to telegram receiver id
		bot.sendMessage(receiver_id, 'https://goo.gl/maps/f3ktgHCBpzq7anPS7')
