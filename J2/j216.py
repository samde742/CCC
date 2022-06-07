A = input().split(" ")
B = input().split(" ")
C = input().split(" ")
D = input().split(" ")

AI = list(map(int, A))
Xs = sum(AI)


for i in range(4):
    Y_sum = int(A[i]) + int(B[i]) + int(C[i]) + int(D[i])

    if Y_sum != Xs:
        print("not magic")
        break

if Y_sum == Xs:
    print("magic")
