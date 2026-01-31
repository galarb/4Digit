from machine import I2C

TM1650_CTRL = 0x24
TM1650_DIGITS = [0x34, 0x35, 0x36, 0x37]

SEGMENTS = {
    '0': 0x3F, '1': 0x06, '2': 0x5B, '3': 0x4F,
    '4': 0x66, '5': 0x6D, '6': 0x7D, '7': 0x07,
    '8': 0x7F, '9': 0x6F,
    ' ': 0x00, '-': 0x40
}

class TM1650:
    def __init__(self, i2c, brightness=3):
        self.i2c = i2c
        self.brightness(brightness)
        self.clear()

    def brightness(self, level):
        level = max(0, min(7, level))
        self.i2c.writeto(TM1650_CTRL, bytes([0x01 | (level << 4)]))

    def clear(self):
        for addr in TM1650_DIGITS:
            self.i2c.writeto(addr, b'\x00')

    def display(self, value):
        text = "{:>4}".format(value)
        for i, ch in enumerate(text):
            self.i2c.writeto(
                TM1650_DIGITS[i],
                bytes([SEGMENTS.get(ch, 0x00)])
            )



