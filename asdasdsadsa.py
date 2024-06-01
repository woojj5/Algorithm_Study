import heapq

foot_time = [3,1,2]
k = 5
ans = -1
h = []
for i in range(len(foot_time)):
    heapq.heappush(h, (foot_time[i], i+1))
prev = 0
leng = len(foot_time)
while h:
    t = (h[0][0] - prev)*  leng
    if t  <= k:
        k -= t
        prev = h[0][0]
        heapq.heappop(h)
        leng -=1
    
    else:
        ind = k % leng
        h.sort(key = lambda x : x[1])
        ans = h[ind][1]
        break

print(ans)