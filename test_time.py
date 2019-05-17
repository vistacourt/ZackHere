from datetime import datetime
from datetime import timedelta
from time import time
import time

now=datetime.now()
now10=timedelta(minutes=10)

print (now+now10)
time.sleep(1)
print ('test')
