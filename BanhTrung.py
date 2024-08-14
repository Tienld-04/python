n = int(input())
a = list(map(int, input().split()))
a.sort()
max_abs = 0
for i in range(n):
    for j in range(i + 1, n):
        if abs(a[i] + a[j]) > max_abs:
            max_abs = abs(a[i] + a[j])
print(max_abs)