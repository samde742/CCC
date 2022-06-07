alph = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
v = ["U","O","I","E","A"]
c = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]


P = list(input().upper())

for i in P:
    location = {}
    index = P.index(i)
    AI = alph.index(i)
    alph_index = alph.index(i)

    if i in c:
        CC = 0
        if i == "Z":
            const = "Z"
        for x in alph[alph_index+1:]:
            if x in c:
                const = x
                break
        for x in v:
            F = alph.index(x)
            L = abs(F-AI)
            location[L] = F
        vow_i = location[min(location.keys())]
        vow = alph[vow_i]

        P.remove(i)
        new = f"{i}{vow}{const}"
        P.insert(index, new)

print("".join(P).lower())