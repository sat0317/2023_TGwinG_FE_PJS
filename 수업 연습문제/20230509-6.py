f = open("newfile.txt", 'a')

for i in range(11, 21):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)

f.close()