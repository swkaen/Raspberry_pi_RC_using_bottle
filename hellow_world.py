# -*- coding: utf-8 -*-
from bottle import route, run, template, static_file
from motor_controle import Motor_Controle
from morse_code import Morse_Code
import RPi.GPIO as GPIO

mc = Motor_Controle(29,31,33,35)
morse = Morse_Code(37, 0.2)
mc.setup()
morse.led_setup()

@route('/hello')
def hello():
    return "Hello World!"

@route('/')
def root():
    return template("test")

@route("/static/<filepath:path>", name="static_file")
def static(filepath):   
    return static_file(filepath, root="./static")

@route('/<id:int>')
def detect(id):
    if id == 1:
        mc.forword()
    elif id == 2: 
	mc.backword()
    elif id == 3:
        mc.right_turning()
    elif id == 4:
	mc.left_turning()
    elif id == 5:
	mc.right_pivot()
    elif id == 6:
	mc.left_pivot()
    elif id == 0:
        mc.stop()
    elif id == 7:
        morse.morse_convert(u"メイカーフエア　サイコウ")
    elif id == 8:
        GPIO.cleanup()

    return template("test2")
run(host='192.168.1.26', post=8080, debug=True, reloader=True)
