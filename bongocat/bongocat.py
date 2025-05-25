from machine import Pin, I2C
import sh1106
import time
from framebuf import FrameBuffer, MONO_HLSB

OLED_WIDTH = 128
OLED_HEIGHT = 64

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled = sh1106.SH1106_I2C(OLED_WIDTH, OLED_HEIGHT, i2c, Pin(10), 0x3c)
oled.sleep(False)

def load_pbm(path):
    with open(path, "rb") as f:
        for _ in range(3):
            f.readline()
        data = bytearray(f.read())
    return FrameBuffer(data, OLED_WIDTH, OLED_HEIGHT, MONO_HLSB)

btn_left = Pin(15, Pin.IN, Pin.PULL_UP)
btn_right = Pin(16, Pin.IN, Pin.PULL_UP)
#while True:
#    if not btn_left.value():
#        print("btn left")
#    elif not btn_right.value():
#        print("btn right")
#    time.sleep(0.1)

frames = [load_pbm(f"bongocat{i}.pbm") for i in range(4)]
current = -1

while True:
    state = (btn_left.value(), btn_right.value())
    idx = {(1,1):0, (0,1):1, (1,0):2, (0,0):3}.get(state, 0)
    if idx != current:
        oled.fill(0)
        oled.blit(frames[idx], 0, 0)
        oled.show()
        current = idx
    time.sleep(0.01)
    
