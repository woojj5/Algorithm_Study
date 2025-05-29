moi = lambda: map(int, input().split())
n,m = moi()
bags = [list(moi()) for _ in range(n)]
# x값은 크기값, y값은 가치값
bags.sort()
dp = [0] * (m+1)
for i in range(n):
    for j in range(m, 0, -1):
        if j >= bags[i][0]:
            dp[j] = max(dp[j], dp[j-bags[i][0]] + bags[i][1])
print(dp[-1])