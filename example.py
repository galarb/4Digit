from machine import Pin, I2C
from tm1650 import TM1650
import time

i2c = I2C(0, scl=Pin(14), sda=Pin(27))
disp = TM1650(i2c, brightness=5)

disp.display("123")
time.sleep(1)
disp.display("-45 ")

