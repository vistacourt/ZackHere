#! /usr/bin/env python
import nmap
from datetime import datetime
from datetime import timedelta
from time import time
import time
import os
import blinkt

nm = nmap.PortScanner()
tom_iphone_time=0
tessie_iphone_time=0
brooke_iphone_time=0
zack_iphone_time=0

blinkt.set_clear_on_exit()
blinkt.set_brightness(.1)
input('Press ENTER to start scanning')

def loop():
    global tom_iphone_time
    global tessie_iphone_time
    global brooke_iphone_time
    global zack_iphone_time
    start_time=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")
  
    while True:
        os.system('clear')
        print('----------------------------------------------------')
        print('Starting wifi scan -',start_time)
        print('Searching for signals...')
        print()
        print('----------------------------------------------------')
        print()

        if zack_iphone_time!=0:
            print('Zack iPhone -',zack_iphone_time)
            print()
            blinkt.set_pixel(1,0, 100, 0)
            blinkt.set_pixel(0,0, 100, 0)
            if datetime.now()>=zack_last+timedelta(minutes=5):
                blinkt.set_pixel(0,0, 0, 0)
                if datetime.now()>=zack_last+timedelta(minutes=15):
                    for i in range(5):
                        blinkt.set_pixel(1,0, 0, 0)            
                        blinkt.show()
                        time.sleep(.5)
                        blinkt.set_pixel(1,0, 100, 0)
                        time.sleep(.5)
                        blinkt.show()
                if datetime.now()>=zack_last+timedelta(minutes=30):
                    blinkt.set_pixel(1,0, 0, 0)

        if brooke_iphone_time!=0:
            print('Brooke iPhone -',brooke_iphone_time)
            print()
            blinkt.set_pixel(3,255, 140, 0)
            blinkt.set_pixel(2,255, 140, 0)
            if datetime.now()>=brooke_last+timedelta(minutes=5):
                blinkt.set_pixel(2,0, 0, 0)
                if datetime.now()>=brooke_last+timedelta(minutes=15):
                    for i in range(5):
                        blinkt.set_pixel(3,0, 0, 0)            
                        blinkt.show()
                        time.sleep(.5)
                        blinkt.set_pixel(3,255, 140, 0)
                        time.sleep(.5)
                        blinkt.show()
                if datetime.now()>=brooke_last+timedelta(minutes=30):
                    blinkt.set_pixel(3,0, 0, 0)
  
        if tom_iphone_time!=0:
            print('Tom iPhone -',tom_iphone_time)
            blinkt.set_pixel(5,0, 0, 255)
            blinkt.set_pixel(4,0, 0, 255)
            if datetime.now()>=tom_last+timedelta(minutes=5):
                blinkt.set_pixel(4,0, 0, 0)
                if datetime.now()>=tom_last+timedelta(minutes=15): 
                    for i in range(5):
                        blinkt.set_pixel(5,0, 0, 0)
                        blinkt.show()
                        time.sleep(.5)
                        blinkt.set_pixel(5,0, 0, 255)
                        time.sleep(.5)
                        blinkt.show()
                if datetime.now()>=tom_last+timedelta(minutes=30):
                    blinkt.set_pixel(5,0, 0, 0)
   
        if tessie_iphone_time!=0:
            print('Tessie iPhone -',tessie_iphone_time)
            print()
            blinkt.set_pixel(7,255, 20, 147)
            blinkt.set_pixel(6,255, 20, 147)
            if datetime.now()>=tessie_last+timedelta(minutes=5):
                blinkt.set_pixel(6,0, 0, 0)
                if datetime.now()>=tessie_last+timedelta(minutes=15):
                    for i in range(5):
                        blinkt.set_pixel(7,0, 0, 0)            
                        blinkt.show()
                        time.sleep(.5)
                        blinkt.set_pixel(7,255, 20, 147)
                        time.sleep(.5)
                        blinkt.show()
                if datetime.now()>=tessie_last+timedelta(minutes=30):
                    blinkt.set_pixel(7,0, 0, 0)

        blinkt.show()
        nm.scan('192.168.1.*','62078-62079')
    
        for host in nm.all_hosts():
            x=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")
            y=datetime.now()
            try:
                if 'B4:8B:19:88:47:07' in nm[host]['addresses']['mac']:
                    tom_iphone_time = x
                    tom_last = y
                if '54:33:CB:4E:33:6A' in nm[host]['addresses']['mac']:
                    tessie_iphone_time = x
                    tessie_last = y
                if '18:81:0E:7E:60:71' in nm[host]['addresses']['mac']:
                    brooke_iphone_time = x
                    brooke_last = y
                if '64:A5:C3:97:93:B5' in nm[host]['addresses']['mac']:
                    zack_iphone_time = x
                    zack_last = y
                if 'FC:E9:98:B7:5C:45' in nm[host]['addresses']['mac']:
                    zack_iphone_time = x
                    zack_last = y
            except(KeyError):
                continue
loop()
