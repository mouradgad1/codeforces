from itertools import permutations

def solution(t):
    for perm in permutations(t):
        (l1, b1), (l2, b2), (l3, b3) = perm

        if l1 == l2 == l3 and b1 + b2 + b3 == l1:
            return True
        if b1 == b2 == b3 and l1 + l2 + l3 == b1:
            return True
        if b1 == b2 and l1 + l2 == l3 and b1 + b3 == l3:
            return True
        if l2 == l3 and b2 + b3 == b1 and l1 + l2 == b1:
            return True

    return False

n = int(input())
for i in range(n):
    vals = list(map(int, input().split()))
    t = [(vals[0], vals[1]), (vals[2], vals[3]), (vals[4], vals[5])]
    print("Yes" if solution(t) else "no")
