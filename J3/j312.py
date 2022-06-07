K = int(input())
l1 = ['*','x','*']
l2 = [' ', 'x', 'x']
l3 = ['*', ' ', '*']

final = []

for i in range(3):
    l1[i] *= K
    l2[i] *= K
    l3[i] *= K
    line1 = "".join(l1)
    line2 = "".join(l2)
    line3 = "".join(l3)

final.extend([line1]*K)
final.extend([line2]*K)
final.extend([line3]*K)

for i in final:
    print(i)


#get k
#3 lists grid
#each item * 3
#all three string * 3
#n for each 3