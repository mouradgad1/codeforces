ans = 0
x = int(input())
for i in range (x):
    command = input().upper()
    
    if command == "X++" or command == "++X" :
        ans+=1
    else :
        ans -=1
        
print (ans)