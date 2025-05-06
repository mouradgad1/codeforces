x = input()
a = int(input())
for i in range(a):
    
    N = input()
    
    mult = len(N)//len(x)
    if len(N)>10**5:
        
        print ("No")
    elif len(N)%len(x) == 0 and  x*mult == N :
        print("Yes")
    else :
        print("No")
        
