runs = 0
if runs <= 0:
    ABD = {}


while True:
    runs += 1
    IN = input().split()
    if IN[0] == "1":
        ABD[IN[1]] = int(IN[2])

    if IN[0] == "2":
        print(ABD[IN[1]])

    if IN[0] == "3":
        ABD[IN[1]] = ABD[IN[1]] + ABD[IN[2]]

    if IN[0] == "4":
        ABD[IN[1]] = ABD[IN[1]] * ABD[IN[2]]

    if IN[0] == "5":
        ABD[IN[1]] = ABD[IN[1]] - ABD[IN[2]]

    if IN[0] == "6":
        ABD[IN[1]] = ABD[IN[1]] // ABD[IN[2]] 

    if IN[0] == "7":
        break