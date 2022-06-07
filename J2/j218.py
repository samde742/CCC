N = int(input())
Y = list(input())
T = list(input())
occ = 0

for i in range(N):
    if Y[i] == "C" and T[i] == "C":
        occ += 1
print(occ)
        



