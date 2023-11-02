import json
import sys
import os
import platform
import psutil
import json

class MissionComputer:
    def get_mission_computer_info():
        OS=platform.system()
        OSver=platform.version()
        CPUtype=platform.machine()
        CPUcore=os.cpu_count()
        memory=str(round(psutil.virtual_memory().total/(1024.0**3)))+"(GB)"
        data={}
        data["OS"]=OS
        data["OS ver"]=OSver
        data["CPU type"]=CPUtype
        data["CPU core"]=CPUcore
        data["MEM size"]=memory
        file_path="./sample1.json"
        with open(file_path,"w") as f1:
            json.dump(data,f1)
        f1.close
        result=open("./1-8/mars_mission_computer.py","a")
        with open(file_path,"r") as f1:
            json_data=json.load(f1)
            print(json_data)
            result.write(str(json_data))
        f1.close
        result.close

    def get_mission_computer_load():
        CPUuse=psutil.cpu_percent()
        P=psutil.Process()
        MEMuse=str(round(P.memory_info().rss/2**20))+"(MB)"
        data={}
        data["CPU use"]=CPUuse
        data["MEM use"]=MEMuse
        file_path="./sample2.json"
        with open(file_path,"w") as f2:
            json.dump(data,f2)
        f2.close
        result=open("./1-8/mars_mission_computer.py","a")
        with open(file_path,"r") as f2:
            json_data=json.load(f2)
            print(json_data)
            result.write(str(json_data))
        f2.close
        result.close

runComputer=MissionComputer
runComputer.get_mission_computer_info()
runComputer.get_mission_computer_load()
