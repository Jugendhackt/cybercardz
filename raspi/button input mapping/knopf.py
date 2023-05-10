import RPi.GPIO as GPIO

import keyboard

btn_up=31
btn_down=29
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(btn_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
btn_up_pressed=False
btn_down_pressed=False
while True:
	if GPIO.input(btn_up)==GPIO.LOW and btn_up_pressed==False:
		keyboard.send("up")
		btn_up_pressed=True
		print("knopf_up wurde gedrückt")
	elif  GPIO.input(btn_up)==GPIO.HIGH:
		btn_up_pressed=False
	
		

	if GPIO.input(btn_down)==GPIO.LOW and  btn_down_pressed==False:
		keyboard.send("down")
		btn_down_pressed=True
		print("knopf_down wurde gedrückt")
	elif   GPIO.input(btn_down)==GPIO.HIGH:
		btn_down_pressed=False
	
