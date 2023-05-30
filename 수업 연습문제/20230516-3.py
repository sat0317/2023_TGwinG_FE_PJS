src = [5, 4, 3, 7, 8, 9, 1, 6]

def bubble_sort(a):
    l = len(a)
    for i in range(l):
        for j in range(l-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

bubble_sort(src)
print(src)