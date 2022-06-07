N = int(input())
X = []
Y = []

for i in range(N):
    c = input().split(",")
    X.append(int(c[0]))
    Y.append(int(c[1]))

BOT_X = min(X) - 1
BOT_Y = min(Y) - 1

TOP_X = max(X) + 1
TOP_Y = max(Y) + 1

print(f"{BOT_X},{BOT_Y}")
print(f"{TOP_X},{TOP_Y}")