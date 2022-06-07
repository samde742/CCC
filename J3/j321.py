i = []
directions = []

while '99999' not in i:
    DI = input()
    instruction = list(DI)
    i.append(instruction)

    x = int(instruction[0]) + int(instruction[1])
    y = instruction[2] + instruction[3] + instruction[4]

    if (x != 0):
        if DI == '99999':
            break

        elif x % 2 == 0:
            d = 'right'
            directions.append(d)

        elif x % 2 != 0:
            d = 'left'
            directions.append(d)
    print(d, y)