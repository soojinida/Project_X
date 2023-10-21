from collections import defaultdict

try:
    with open ("mission_computer_main.log","r",encoding="utf-8") as f:
        content=f.readlines()
except:
    print("exception")
f.close()

date_res=[]
log_res=[]

for line in content:
    l=line.split('\n')
    sen=l[0].split(',')
    date=sen[0]
    log=sen[1]+' '+sen[2]
    #print(date)
    #print(log)
    date_res.append(date)
    log_res.append(log)

#print(date_res)
#print(log_res)

# date_res.sort(reverse=True)
# date=date_res
# print(date)

# log=log_res
# for i in range(len(log_res)):
#     log[len(log_res)-1-i]=log_res[i]
# print(log)


result=defaultdict(lambda:'default')

for i in range(len(content),-1):
    result[date_res[i]]+=log_res[i]

for i in range(len(content)):
    result[date_res[i]]=log_res[i]

r=sorted(result.items(),reverse=True)
try:

    with open("mission_computer_main.json","w",encoding="utf-8") as f:
        for date,log in enumerate(r):
            f.write(f"{date},{log}")
except:
    print("exception")
f.close
