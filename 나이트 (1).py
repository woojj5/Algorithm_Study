arr = input()
y = ord(arr[0]) - ord('a')
x = int(arr[1]) - 1
cnt = 0
dir = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2),(1, -2), (1, 2)]
for i in range(8):
    nx = x + dir[i][0]
    ny = y + dir[i][1]
    if 0<=nx<8 and 0<=ny<8:
        cnt+=1
print(cnt)