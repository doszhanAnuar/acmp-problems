n = int(input())
l = list(map(int, input().split()))

even = []
odd = []
for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("".join(map(str, odd)))
print("".join(map(str, even)))
if len(even) >= len(odd):
    print("YES")
else:
    print("NO")
