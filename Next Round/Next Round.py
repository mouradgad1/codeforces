n,k = map(int,input().split())
players = list(map(int,input().split()))

kth = players[k-1]
c = 0
for i in players:
    if i >= kth and i>0:
        c+=1
print (c)