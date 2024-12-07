file=open('Codingal.txt','r')
counter=0
content=file.read()
Colist=content.split("\n")

for i in Colist:
    counter+=1

print("number of lines i  file is ",counter)
