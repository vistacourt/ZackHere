import nmap
from datetime import datetime
from datetime import timedelta
from time import time
import os

nm = nmap.PortScanner()
iphone_time=0
iphone2_time=0
zacks_air_time=0
brookes_air_time=0

def loop():

    
  global iphone_time
  global iphone2_time
  global brookes_air_time
  global zack_air_time
  
  while True:
    os.system('cls||clear') 

    print()
    print()
    print('Starting system scan -',datetime.now().strftime("%A, %B %d - %I:%M:%S %p"))
    print()
    print('Searching for signals from Zack and Brooke')
    print()
    print()
      
    if iphone_time!=0:
      print('iPhone - 192.168.1.205',iphone_time)
      print()
    
    if iphone2_time!=0:
      print('iPhone - 192.168.1.14',iphone2_time)
      print()
    if zacks_air_time!=0:
      print('Zacks-Air - 192.168.1.17',zacks_air_time)
      print()
    
    if brookes_air_time!=0:
      print('Brookes-Air-2 - 192.168.1.133',brookes_air_time)
      print()

      
    nm.scan('192.168.1.*','62078-62079')
    
    for host in nm.all_hosts():
      x=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")

      if '18:81:0E:7E:60:71' in nm[host]['addresses']['mac']:
##        print (nm[host]['addresses'])
##        print('iPhone - 192.168.1.205',iphone_time)
##        print()
          iphone_time = x
      if 'FC:E9:98:B7:5C:45' in nm[host]['addresses']['mac']:
##        print (nm[host]['addresses'])
##        print('iPhone - 192.168.1.14',iphone2_time)
##        print()
          iphone_time = x
      if '84:38:35:48:6D:4C' in nm[host]['addresses']['mac']:
##        print (nm[host]['addresses'])
##        print('Zacks-Air - 192.168.1.17',zacks_air_time)
##        print()
          iphone_time = x          
      if '84:38:35:67:42:22' in nm[host]['addresses']['mac']:
##        print (nm[host]['addresses'])
##        print('Brookes-Air-2 - 192.168.1.133',brookes_air_time)
##        print()
          iphone_time = x          
##      
##      if ('iPhone' in nm[host].hostname() and '-iPhone' not in nm[host].hostname()): 
##        iphone_time = x
##      
##      if ('Brookes-Air-2' in nm[host].hostname()):
##        brookes_air_2_time = x
##
##    
loop()
