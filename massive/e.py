num= int(input())
x = input().split(" ")

for j in range(1, num):
    if int(x[j])*int(x[j-1]) > 0:
        print("YES")
        break
else:
    print("NO")