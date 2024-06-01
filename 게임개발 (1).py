n,m = map(int, input().split())
x,y,d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
visit = [[0 for i in range(m)] for j in range(n)] 
dir = [(-1,0), (0,1), (1,0), (0, -1)]

visit[x][y] = 1
cnt = 1
turn = 0
while True:
    nx = x + dir[d][0]
    ny = y + dir[d][1]

    if 0<= nx < n and 0<= ny < m and arr[nx][ny] == 0 and visit[nx][ny] == 0:
        visit[nx][ny] = 1
        cnt+=1
        turn = 0
        x = nx
        y = ny
        continue
    else:
        turn+=1
    
    if turn == 4:
        nx = x - dir[d][0]
        ny = y - dir[d][1]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn  = 0
    
    d-=1
    
    if d == -1:
        d = 3
print(cnt)