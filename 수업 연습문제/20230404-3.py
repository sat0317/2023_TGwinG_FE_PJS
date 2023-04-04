def newprint(x):
    data = x[:]
    lens = [len(i) for i in data]

    pos = 0
    while data:
        k = len(data)
        dels = 0
        for i in range(k):
            if lens[i-dels]<=pos:
                del lens[i-dels]
                del data[i-dels]
                dels+=1
                continue
            print(data[i-dels][pos], end="")
        pos+=1

inp = []
for i in range(5):
    inp.append(input())
newprint(inp)