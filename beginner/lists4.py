x1 = int(input())
x2 = int(input())

l = list(range(x1, x2+1, 2))

x = int(input())

if x > len(l):
    print("not possible")
else:
    print(l[:x])