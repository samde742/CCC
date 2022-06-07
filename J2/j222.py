N = int(input())
star = 0

for i in range(N):
    S = int(input())
    F = int(input())
    SS = S * 5
    FS = F * 3
    rating = SS - FS

    if rating > 40:
        star += 1
    else: pass

if star == N:
    print(f"{star}+")
else: print(star)