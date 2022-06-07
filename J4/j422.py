#take inputs
#create final lists
#compare to x, make sure those 2 in the same group if not violations += 1
#same with y
#print vios

XL = []
YL = []


X = int(input())
for i in range(X):
    a = input().split(" ")
    XL.append(a)

Y = int(input())
for i in range(Y):
    a = input().split(" ")
    YL.append(a)

G = int(input())
vios = 0


for i in range(G):
    GL = input().split(" ")
    
    for x in XL:
        if x[0] in GL:
            if (x[0] in GL and x[1] not in GL) or (x[0] not in GL and x[1] in GL):
                vios += 1
    
    for x in YL:
        if x[0] in GL and x[1] in GL:
            vios += 1
print(vios)