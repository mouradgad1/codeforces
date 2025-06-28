t = int(input())

for q in range(t):
    n, c= map(int, input().split())
    arr = list(map(int, input().split()))
    lo = min(arr)
    hi = max(arr)
    steps = min(abs(c - lo), abs(c - hi)) + (hi - lo)
    print(steps)
