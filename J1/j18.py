n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

if (n1 == 8 and n4 == 8 or n4 == 9 and n1 == 9 or n1 == 8 and n4 == 9 or n1 ==9 and n4 == 8) and n2 == n3:
    print("ignore")

else: print("answer")