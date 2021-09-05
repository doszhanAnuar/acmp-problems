a = input().split()
first = list(map(int, a))
if first[0] * first[1] == first[2]:
    print("YES")
else:
    print("NO")
