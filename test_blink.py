import time
import blinkt

blinkt.set_clear_on_exit()
blinkt.set_brightness(.1)

blinkt.set_pixel(1,255,0,0)
time.sleep(5)
blinkt.show()
blinkt.set_pixel(1,0, 0, 0)
blinkt.show()

while True:
    blinkt.set_pixel(0,0, 100, 0)
    blinkt.show()
    time.sleep(5)
    blinkt.set_pixel(0,0, 0, 0)
    blinkt.show()
    time.sleep(5)
    blinkt.set_pixel(0,0, 100, 0)
    blinkt.show()
    time.sleep(5)
    blinkt.set_pixel(0,0, 0, 0)
    blinkt.show()

blinkt.show()
