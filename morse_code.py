# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

class Morse_Code:

    morse_code_jp = {u"イ":"il",u"ロ":"ilil",u"ハ":"lii",u"ニ":"lili",u"ホ":"lii",u"ヘ":"i",u"ト":"iilii",
    u"チ":"iili",u"リ":"lli",u"ヌ":"iiii",u"ル":"lilli",u"ヲ":"illl",
    u"ワ":"lil",u"カ":"ilii",u"ヨ":"ll",u"タ":"li",u"レ":"lll",u"ソ":"llli",
    u"ツ":"illi",u"ネ":"llil",u"ナ":"ili",u"ラ":"iii",u"ム":"l",
    u"ウ":"iil",u"ヰ":"iliil",u"ノ":"iill",u"オ":"iliii",u"ク":"iiil",u"ヤ":"ill",u"マ":"liil",
    u"ケ":"lill",u"フ":"llii",u"コ":"llll",u"エ":"lilll",u"テ":"ilill",
    u"ア":"llill",u"サ":"lilil",u"キ":"lilii",u"ユ":"liill",u"メ":"liiil",u"ミ":"iilil",u"シ":"llili",
    u"ヱ":"illii",u"ヒ":"lliil",u"モ":"liili",u"セ":"illli",u"ス":"lllil",
    u"ン":"ilili",u"゛":"ii",u"゜":"iilli",
    u"一":"illll",u"二":"iilll",u"三":"iiill",u"四":"iiiil",u"五":"iiiii",u"六":"liiii",u"七":"lliii",u"八":"lllii",u"九":"lllli",
    u"〇":"lllll",u"ー":"illil"}

    def __init__(self,led,span):
        self.led = led
        self.span = span

    def led_setup(self):
        GPIO.setup(self.led, GPIO.OUT)

    def morse_test(self):
        a = self.morse_code_jp[u"ネ"]
        print a

    def tanten(self):
        GPIO.output(self.led, GPIO.HIGH)
        time.sleep(self.span)
        GPIO.output(self.led, GPIO.LOW)
        time.sleep(self.span)

    def tyouten(self):
        GPIO.output(self.led, GPIO.HIGH)
        time.sleep(self.span * 3)
        GPIO.output(self.led, GPIO.LOW)
        time.sleep(self.span)

    def morse_convert(self,kotoba):
        for w_f in kotoba:
            if w_f != u"　":
                mo = self.morse_code_jp[w_f]
                for w_s in mo:
                    if w_s == "i":
                        self.tanten()
                    elif w_s == "l":
                        self.tyouten()
                time.sleep(self.span * 2)
            elif w_f == u"　":
                time.sleep(self.span * 6)

if __name__ == '__main__':
    m = Morse_Code(37, 0.2)
    GPIO.setmode(GPIO.BOARD)
    m.led_setup()
    m.morse_convert(u"コ゛メンネ")
    GPIO.cleanup()
