def isthere228(year):
    if not year%400:
        return "윤년"
    elif not year%100:
        return "평년"
    elif not year%4:
        return "윤년"
    else:
        return "평년"

print(2020, isthere228(2020))
print(2000, isthere228(2000))
print(1000, isthere228(1000))

def codegolf(y):
    return ("윤년","평년","평년")[bool(y%4)+(y%400 and not y%100)]
print(2020, codegolf(2020))
print(2000, codegolf(2000))
print(1000, codegolf(1000))
print(2021, codegolf(2021))
