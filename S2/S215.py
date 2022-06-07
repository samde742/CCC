J = int(input())
A = int(input())
available = {}
reqs = {}
satisfied = 0

for i in range(J):
    size = input()
    available[i] = size

for i in range(A):
    req = input().split(" ")
    reqs[i] = req[0]


for k,v in available.items():
    for n,s in reqs.items():
        if k == n:
            if s == "S":
                satisfied += 1
            elif s == "L" and v == "L":
                satisfied += 1
                

            elif s == "M" and (v == "M" or v == "L"):
                satisfied += 1


print(satisfied)