n = int(input())
arr = list(map(int, input().split()))
visit = [0] * (sum(arr)+1)

for i in arr:
    visit[i] = 1

for i in range(n-1):
    res = arr[i]
    for j in range(i+1, n):
        if i!= j:
            res= res+arr[j]
            if visit[res] == 0:
                visit[res] = 1

for i in range(min(arr), max(arr) +1):
    if visit[i] == 0:
        print(i)
        break