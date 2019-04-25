import os
import nmap
from datetime import datetime
from datetime import timedelta
from time import time
from tkinter import *



start_time=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")


master=Tk()
master.geometry("400x400")

nm = nmap.PortScanner()
iphone_time=0
iphone2_time=0
zacks_air_time=0
brookes_air_time=0






def feedback():

    global nm
    global iphone_time
    global iphone2_time
    global zacks_air_time
    global brookes_air_time
    labelfont='("arial",5)'
    
    Label(master,text='',).grid(row=0,column=0)
    Label(master,text=str(start_time),font=labelfont).grid(row=1,column=0,sticky='w')
    Label(master,text='Starting wifi scan',font=labelfont).grid(row=2,column=0,sticky='w')
    Label(master,text='Searching for signals...',font=labelfont).grid(row=3,column=0,sticky='w')
    Label(master,text='').grid(row=4,column=0)
    print('Starting wifi scan -',start_time)
    print('Searching for signals...')


    if iphone_time!=0:
      Label(master,text='Brooke iPhone - 192.168.1.205 -').grid(row=6,column=0,sticky='w')
      Label(master,text=str(iphone_time)).grid(row=7,column=0,sticky='w')
      Label(master,text='').grid(row=8,column=0)
      print('Brooke iPhone - 192.168.1.205 -',iphone_time)
      print()

    if iphone2_time!=0:
      Label(master,text='Zack iPhone - 192.168.1.14 -').grid(row=9,column=0,sticky='w')
      Label(master,text=str(iphone2_time)).grid(row=10,column=0,sticky='w')
      Label(master,text='').grid(row=11,column=0)
      print('Zack iPhone - 192.168.1.14 -',iphone2_time)
      print()
      
    if zacks_air_time!=0:
      Label(master,text='Zack Air - 192.168.1.17 -').grid(row=12,column=0,sticky='w')
      Label(master,text=str(zacks_air_time)).grid(row=13,column=0,sticky='w')
      Label(master,text='').grid(row=14,column=0)
      print('Zack Air - 192.168.1.17 -',zacks_air_time)
      print()


    if brookes_air_time!=0:
      Label(master,text='Brooke Air-2 - 192.168.1.133 -').grid(row=15,column=0,sticky='w')
      Label(master,text=str(iphone_time)).grid(row=16,column=0,sticky='w')
      Label(master,text='').grid(row=17,column=0)
      print('Brooke Air-2 - 192.168.1.133 -',brookes_air_time)
      print()

    master.update()
    search()

def search():

    global nm
    global iphone_time
    global iphone2_time
    global zacks_air_time
    global brookes_air_time
    
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
    print('finished search')
    print(x)

while True:
    feedback()

    
master.mainloop()       


        
