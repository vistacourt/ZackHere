import nmap
from datetime import datetime
from datetime import timedelta
from time import time
import os
import tkinter as tk
import sys


root = tk.Tk()
nm = nmap.PortScanner()
iphone_time=0
iphone2_time=0
zacks_air_time=0
brookes_air_time=0











##global iphone_time
##global iphone2_time
##global brookes_air_time
##global zacks_air_time



  



while True:
    root.update_idletasks()
    root.update()

    text_box = tk.Text(root, state=tk.DISABLED)
    text_box.grid(row=0, column=0, columnspan=4)

    def write(string):
        text_box.config(state=tk.NORMAL)
        text_box.insert("end",string +"\n")
        text_box.see("end")
        text_box.config(state=tk.DISABLED) 



 
    
    start_time=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")
    write('----------------------------------------------------')
    write('Starting wifi scan -')
    write(start_time)

    write('Searching for signals...')
    write('')
    write('----------------------------------------------------')
    write('')
    root.update_idletasks()
    root.update()


  
    if iphone_time!=0:
      write('Brooke iPhone - 192.168.1.205 -')
      write(iphone_time)
      write('')

    if iphone2_time!=0:
      write('Zack iPhone - 192.168.1.14 -')
      write(iphone2_time)
      write('')
      
    if zacks_air_time!=0:
      write('Zack Air - 192.168.1.17 -')
      write(zacks_air_time)
      write('')
      root.update_idletasks()
      root.update()


    if brookes_air_time!=0:
      write('Brooke Air-2 - 192.168.1.133 -')
      write(brookes_air_time)
      write('')

    
      
    nm.scan('192.168.1.*','62078-62079')

    for host in nm.all_hosts():
      x=datetime.now().strftime("%A, %B %d - %I:%M:%S %p")
      print('test')
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
    
    root.mainloop()
      



    

