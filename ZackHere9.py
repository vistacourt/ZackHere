import nmap
from datetime import datetime
from datetime import timedelta
from time import time
import os
from flask import Flask, render_template, request

nm = nmap.PortScanner()
iphone_time=0
iphone2_time=0
zacks_air_time=0
brookes_air_time=0

app = Flask(__name__)
@app.route('/')

def loop():
    
  global iphone_time
  global iphone2_time
  global brookes_air_time
  global zacks_air_time
  start_time=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")
  x='data'
  return render_template('index.html',x=x)
  while True:
    os.system('cls||clear')

    print()
    print()
    print('Starting system scan -',start_time)
    #return('Starting system scan -',start_time)
    print()
    print('Searching for signals from Zack and Brooke')
    #return('Searching for signals from Zack and Brooke')
    print()
    print()
     
    if iphone_time!=0:
      print('Brooke iPhone - 192.168.1.205 -',iphone_time)
      print()
    
    if iphone2_time!=0:
      print('Zack iPhone - 192.168.1.14 -',iphone2_time)
      print()
    if zacks_air_time!=0:
      za=('Zack Air - 192.168.1.17 -',zacks_air_time)
      #return (za)
      return render_template('index.html',za=za)
      print('Zack Air - 192.168.1.17 -',zacks_air_time)
      #return('Zack Air - 192.168.1.17 -',zacks_air_time)
      print()
      #return
    
    if brookes_air_time!=0:
      print('Brooke Air-2 - 192.168.1.133 -',brookes_air_time)
      print()
      
    nm.scan('192.168.1.*','62078-62079')
    
    for host in nm.all_hosts():
      x=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")

      try:
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
  #return render_template('index.html',loop(za))    
loop()
 
if __name__ == '__main__':
    app.run()