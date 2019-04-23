from flask import Flask
import nmap
from datetime import datetime
from datetime import timedelta
from time import time
app= Flask(__name__)
nm = nmap.PortScanner()
zack=0
brooke=0
zack1=datetime.today()
brooke1=datetime.today()
status=''
print()
print()
#return('Starting system scan -',datetime.today())
print()
#return('Searching for signals from Zack and Brooke')
print()
@app.route('/')
def loop():
  global zack
  global zack1
  global brooke
  global brooke2
  status = 'Gone'
  bstatus = 'Gone'
  while True:
    
    if zack!=0:
      print('Zack is',status)
      print (zack)
      print()
      return (status)
    
    
    if brooke!=0:
      print('Brooke is',bstatus)
      print (brooke)
      print()
      return (status)
    
    nm.scan('192.168.1.*','62078-62079') 
    for host in nm.all_hosts():
      x=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")
      x1=datetime.today()-timedelta(hours=0,minutes=15)
      y=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")
      y1=datetime.today()-timedelta(hours=0,minutes=15)
      if ('iPhone' in nm[host].hostname() and '-iPhone' not in nm[host].hostname()): #or zack1 < x1:
        
        zack = x
        zack1 = datetime.today()
        status = 'Here'
      if ('brooke' in nm[host].hostname()):
        
        brooke = y
        brooke1 = datetime.today()
        bstatus = 'Here'
loop()
if __name__ == '__main__':
    app.run()
