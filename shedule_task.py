import time
from datetime import datetime,timedelta

def task(target_time):
    while True:
        now = datetime.now()
        if now >= target_time:
            print("Task executed at:", now)
            break
        time.sleep(1)

target_time = datetime.now() + timedelta(seconds=10)
task(target_time)
     
