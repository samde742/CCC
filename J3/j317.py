A = input().split()
B = input().split()
P = int(input())

A = list(map(int, A))
B = list(map(int, B))

xd = abs(A[0] - B[0])
yd = abs(A[1] - B[1])
sum = xd + yd

if (sum % 2 == 0 and P % 2 == 0 or sum % 2 != 0 and P % 2 != 0) and P >= sum:
    print("Y")

else: 
    print("N")