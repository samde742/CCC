L = int(input())

for i in range(L):
    N = input()
    N = N.split(" ")
    T = int(N[0])
    print(N[1] * T)
