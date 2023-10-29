try:
    with open("Mars_Base_Inventory_List.csv","r",encoding="utf-8") as f:
        reader=f.readlines()
except:
    print("exception")
f.close
content=[]
lines=[]

for line in reader:
    l=''.join(line)
    #print(l)
    content.append(l)

#print(content)
for i in range(len(content)):
    if i!=0:
        lines.append(content[i])
#print(lines)
result=''

for line in lines:
    l=line.split(',')
    #print(l)
    if float(l[4]) > 0.7:
        #print(line)
        print(l[4])
        result+=line
        #result+=str(l)
print(result)
try:

    with open("Mars_Base_Inventory_danger.csv","w",encoding="utf-8") as f:
        for line in result:
            f.write(line)
except:
    print("exception")
f.close
