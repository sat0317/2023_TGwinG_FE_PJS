f = open("newfile.txt", 'w')

for i in range(1, 6):
    data=""
    for j in range(i):
        data += "*"
    f.write(data+'\n')

f.close()

f = open("newfile2.txt", 'w')
i = 1
while i<6:
    j=0
    while j<i:
        f.write('*')
        j+=1
    f.write('\n')
    i+=1

f.close()

