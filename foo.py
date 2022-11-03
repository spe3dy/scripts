Names = []
for line in open('quellen.txt','r').readlines():
    Names.append(line.strip())
    print(Names)