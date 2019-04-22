import winsound
import nmap
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
nm = nmap.PortScanner()
while True:
    nm.scan('192.168.1.*', '62078-62079')
    for h in nm.all_hosts():
        try:
            
            if '84:38:35:48:6D:4C' in nm[h]['addresses']['mac']:
                print (nm[h]['addresses'])
                winsound.Beep(2000, duration)
                print('Zack')
                print()
            if 'FC:E9:98:B7:5C:45' in nm[h]['addresses']['mac']:
                print (nm[h]['addresses'])
                winsound.Beep(2500, duration)
                print('Brooke')
                print()
        except(KeyError):
            continue



