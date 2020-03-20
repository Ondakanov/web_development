
num = int(input())
num = input().split(" ")

for i in num:
    if int(i) % 2 == 0:
        print(i, end=" ")