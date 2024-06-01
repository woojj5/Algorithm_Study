n, m = map(int, input().split())
list_a  = list(map(int, input().split()))

lista = []
for i in range(n-1):
    for j in range(i+1, n):
        if i != j and list_a[i] != list_a[j]:
            lista.append((i,j))
print(len(lista))
