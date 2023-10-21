import numpy as np
import pandas as pd

#part1=np.loadtxt("mars_base_main_parts-001.csv",delimiter=',',encoding="utf-8")
#print(part1)

with open("mars_base_main_parts-001.csv","r",encoding="utf-8") as f:
    content=f.readlines()
#print(content)
data=[]
for line in content:
    l=line.split('\n')
    sen=l[0].split(',')
    data.append(sen)


arr1=np.array(data)
#print(arr)

with open("mars_base_main_parts-002.csv","r",encoding="utf-8") as f:
    content=f.readlines()
#print(content)
data=[]
for line in content:
    l=line.split('\n')
    sen=l[0].split(',')
    data.append(sen)


arr2=np.array(data)

with open("mars_base_main_parts-003.csv","r",encoding="utf-8") as f:
    content=f.readlines()
#print(content)
data=[]
for line in content:
    l=line.split('\n')
    sen=l[0].split(',')
    data.append(sen)


arr3=np.array(data)

# arr12=np.concatenate(arr1,arr2,axis=0)
# arr=np.concatenate(arr12,arr3,axis=0)

arr1=np.delete(arr1,0,axis=0)
arr2=np.delete(arr2,0,axis=0)
arr3=np.delete(arr3,0,axis=0)

print(arr3[0])

arr=np.concatenate((arr1,arr2))
parts=np.concatenate((arr,arr3))
print(parts)

print(len(parts))

avg=[]

for i in range():
    