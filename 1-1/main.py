print("Hello Mars")

try:
    with open ("mission_computer_main.log","r",encoding="utf-8") as f:
        content=f.readlines()
except:
    print("예외 발생")
f.close()
    
for line in content:
    print(line)

for i in range(len(content)):
    if "unstable" in content[i]:
        problem=''
        for j in range(i,len(content)):
            problem+=content[j]

#print(problem)
try:

    with open("log_analysis.md","w",encoding="utf-8") as f:
        f.write(problem)
except:
    print("exception")
