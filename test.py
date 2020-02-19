from __future__ import print_function
import psutil
import time

def executeSomething():
    print(psutil.virtual_memory()[2])
    time.sleep(1)

while True:
    executeSomething()