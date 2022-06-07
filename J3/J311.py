T1 = int(input())
T2 = int(input())
st = 2

while True:
    TM = T1 - T2
    st += 1
    if TM > T2:
        break
    T1 = T2
    T2 = TM

print(st)