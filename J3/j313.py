Y = input()
year = int(Y)

while True:
    year += 1
    Y_list = str(year)
    Y_list = list(map(int,Y_list))

    wrong = 0
    for i in Y_list:
        SN = Y_list.count(i)
        if SN > 1:
            wrong += 1
    if wrong == 0:
        D = year
        break

print(D)