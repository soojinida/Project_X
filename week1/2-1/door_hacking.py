import datetime
import time
import itertools
import zipfile 
import os

current=datetime.datetime.now()
zFile=zipfile.ZipFile('./emergency_storage_key.zip')
def unlock_zip():
    start=current.time()
    print("start time: {}",start)
    start_time=time.time()
    cnt=0
    passwd_string = "0123456789abcdefghijklmnopqrstuvwxyz"
    for len in range(1, 6):
        to_attempt = itertools.product(passwd_string, repeat = len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            cnt+=1
            try:
                pwd="xxxxxx"
                if pwd==passwd:
                    print (f"password: {passwd}")
                    break
            except:
                pass
    end_time=time.time()
    all_time=end_time-start_time
    print("count: {}",cnt)
    print("all time: ",all_time)
    with open("password.txt","w") as f:
        f.write(pwd)
    f.close

unlock_zip()
