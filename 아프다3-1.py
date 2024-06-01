n,m = map(int, input().split())
count = 0
count = count + (n // m) + (n%m)
n = n//m
print(count)
