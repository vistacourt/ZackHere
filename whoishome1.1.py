import nmap
from datetime import datetime
from datetime import timedelta
from time import time
import os
#import blinkt

nm = nmap.PortScanner()
tom_iphone_time=0
iphone_time=0
iphone2_time=0
zacks_air_time=0
brookes_air_time=0


#blinkt.set_clear_on_exit()

input('Press ENTER to start scanning')

def loop():
    global tom_iphone_time
    global iphone_time
    global iphone2_time
    global brookes_air_time
    global zacks_air_time
    start_time=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")
  
    while True:
        os.system('cls||clear') 

        print('----------------------------------------------------')
        print('Starting wifi scan -',start_time)
        print('Searching for signals...')
        print()
        print('----------------------------------------------------')
        print()

        
        if tom_iphone_time!=0:
            #blinkt.set_all(128, 0, 0)
            print('Tom iPhone -',tom_iphone_time)
            print()
            
        if iphone_time!=0:
            print('Brooke iPhone -',iphone_time)
            print()
    
        if iphone2_time!=0:
            print('Zack iPhone -',iphone2_time)
            print()
      
        if zacks_air_time!=0:
            print('Zack Air -',zacks_air_time)
            print()
    
        if brookes_air_time!=0:
            print('Brooke Air-2 -',brookes_air_time)
            print()

        #blinkt.show()
      
        nm.scan('192.168.1.*','62078-62079')
    
        for host in nm.all_hosts():
            x=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")

            try:
                if 'B4:8B:19:88:47:07' in nm[host]['addresses']['mac']:
                    tom_iphone_time = x
                if '18:81:0E:7E:60:71' in nm[host]['addresses']['mac']:
                    iphone_time = x
                if 'FC:E9:98:B7:5C:45' in nm[host]['addresses']['mac']:
                    iphone2_time = x
                if '84:38:35:48:6D:4C' in nm[host]['addresses']['mac']:
                    zacks_air_time = x
                if '84:38:35:67:42:22' in nm[host]['addresses']['mac']:
                    brookes_air_time = x
            except(KeyError):
                continue

loop()
