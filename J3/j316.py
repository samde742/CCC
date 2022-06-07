W = list(input())
length = 0
L = len(W) - 1
C = []


for i in W:
    Am = W.count(i)
    
    if Am <= 1:
        W.remove(i)
    print(W)

WR = W[::-1]

for i in W:
    index = W.index(i)
    if i == WR[index]:
        C.append(i)
    print(C)

#find all philandromes in a string -. 


# for i in W:
#     index = E.index(i)
#     C = E.count(i)
#     sub = abs(L - index)
    

#     if C <= 1:
#         del E[sub]
#         E.remove(i)
#         W = E
#     elif i != E[sub] or E.count(E[sub - 1]) <= 1:
#         del E[sub]
#         E.remove(i)
#         W = E
#     else:
#         length += 1
#     print(E)
# print(length)