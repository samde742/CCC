B = int(input())

P = 5 * B - 400

if P > 100:
    level = -1
elif P < 100:
    level = 1
else: level = 0

print(P)
print(level)