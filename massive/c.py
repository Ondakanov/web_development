x = input()
x = input().split(" ")
res = 0
for i in x:
    if int(i) > 0:
        res += 1
print(res)