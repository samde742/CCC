N = int(input())
K = int(input())
N_og = N

for i in range(K):
    N *= 10
    N_og += N
print(N_og)