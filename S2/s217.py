A = int(input())
M = input().split(" ")

M = list(map(int, M))
M.sort()
final = ""

if len(M) != 1:
    if A % 2 != 0:
        re = M[:A//2 + 1][::-1]
    else:
        re = M[:A//2][::-1]
    
    for i in re:
        ind = re.index(i)
        if i != M[ind + A//2]:
            add = f" {i} {M[ind + A//2]}"
        else:
            re.remove(i)
            del M[ind + A//2]
            add = ""
            
        final += add
    print(final.lstrip())

else:
    print(M[0])
