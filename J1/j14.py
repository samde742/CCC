A1 = int(input())
A2 = int(input())
A3 = int(input())
sum = A1 + A2 + A3

if sum == 180:
    if A1 == A2 and A2 == A3:
        print("Equilateral")

    if A1 == A2 and A2 != A3 or A2 == A3 and A1 != A3 or A1 == A3 and A1 != A2:
        print("Isosceles")

    if A1 != A2 and A2 != A3 and A1 != A3:
        print("Scalene")

else: print("Error")
