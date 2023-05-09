sum = 0

with open("test2.txt", 'r') as f:
    data = f.readline().strip()
    for i in data:
        sum += int(i)

with open("test2.txt", 'a') as f:
    f.write("\n")
    f.write(str(sum/len(data)))
