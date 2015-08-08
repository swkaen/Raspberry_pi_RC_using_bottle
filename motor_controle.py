# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
class Motor_Controle:
    def __init__(self, left1, left2, right1, right2):
        self.left1 = left1
        self.left2 = left2
        self.right1 = right1
        self.right2 = right2

    def setup(self):
    	GPIO.setmode(GPIO.BOARD)
    	GPIO.setup(self.left1, GPIO.OUT)
    	GPIO.setup(self.left2, GPIO.OUT)
    	GPIO.setup(self.right1, GPIO.OUT)
    	GPIO.setup(self.right2, GPIO.OUT)
        
    def forword(self):
    	GPIO.output(self.left1, GPIO.HIGH)
    	GPIO.output(self.left2, GPIO.LOW)
    	GPIO.output(self.right1, GPIO.HIGH)
    	GPIO.output(self.right2, GPIO.LOW)
        
    def backword(self):
    	GPIO.output(self.left1, GPIO.LOW)
    	GPIO.output(self.left2, GPIO.HIGH)
    	GPIO.output(self.right1, GPIO.LOW)
    	GPIO.output(self.right2, GPIO.HIGH)

    def right_turning(self):
    	GPIO.output(self.left1, GPIO.HIGH)
    	GPIO.output(self.left2, GPIO.LOW)
    	GPIO.output(self.right1, GPIO.LOW)
    	GPIO.output(self.right2, GPIO.LOW)

    def left_turning(self):
    	GPIO.output(self.left1, GPIO.LOW)
    	GPIO.output(self.left2, GPIO.LOW)
    	GPIO.output(self.right1, GPIO.HIGH)
    	GPIO.output(self.right2, GPIO.LOW)

    def right_pivot(self):
    	GPIO.output(self.left1, GPIO.HIGH)
    	GPIO.output(self.left2, GPIO.LOW)
    	GPIO.output(self.right1, GPIO.LOW)
    	GPIO.output(self.right2, GPIO.HIGH)

    def left_pivot(self):
    	GPIO.output(self.left1, GPIO.LOW)
    	GPIO.output(self.left2, GPIO.HIGH)
    	GPIO.output(self.right1, GPIO.HIGH)
    	GPIO.output(self.right2, GPIO.LOW)
    def stop(self):
	GPIO.output(self.left1, GPIO.LOW)
	GPIO.output(self.left2, GPIO.LOW)
	GPIO.output(self.right1, GPIO.LOW)
	GPIO.output(self.right2, GPIO.LOW)

if __name__ == '__main__':
    m = Motor_Controle(29,31,33,35)
    m.setup()
    m.forword()
    time.sleep(3)
    m.right_pivot()
    time.sleep(3)
    m.left_pivot()
    time.sleep(3)
    GPIO.cleanup()
