D = input().split(" ")
D = list(map(int, D))
c = [0]

for i in range(len(D)):
    c.append(c[i] + D[i])

for i in range(5):
    final = []
    for x in range(len(c)):

        dis = abs(c[x] - c[i])
        final.append(dis)
    f = f"{final[0]} {final[1]} {final[2]} {final[3]} {final[4]}"
    print(f)

    