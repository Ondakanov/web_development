prev = int(input())
ans = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        ans += 1
    prev = next
print(ans)