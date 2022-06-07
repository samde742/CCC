N= int(input())
A_life = 100
D_life = 100


for i in range(N):
    R = input().split(" ")
    R = list(map(int, R))
    if R[0] > R[1]:
        D_life -= R[0]
    elif R[0] < R[1]:
        A_life -= R[1]
    else: pass
print(A_life)
print(D_life)