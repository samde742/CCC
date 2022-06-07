P = int(input())
N = int(input())
R = int(input())
days = 0
people = N
yesterday = N

while people <= P:
    people *= R
    people += yesterday
    days += 1

print(days)

