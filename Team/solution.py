number = 0
a = int(input())
for _ in range(a):
    x = input()
    counter = x.count('1')
    if counter > 1:
        number += 1
print(number)
