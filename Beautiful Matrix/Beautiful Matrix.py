matrix = [list(map(int,input().split()))for _ in range (5)]

x=0
y =0
for i in range(5):
    for j in range(5):
        if matrix[j][i]==1:
            x=j
            y=i
            
moves = (abs(x-2)+abs(y-2))
print(moves)