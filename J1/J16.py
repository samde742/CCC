g1 = input()
g2 = input()
g3 = input()
g4 = input()
g5 = input()
g6 = input()

player_stats = [g1, g2, g3, g4, g5, g6]
wins = 0

for i in player_stats:
    if i == "W":
        wins += 1

if wins >= 5:
    print(1)

elif wins >= 3 and wins <= 4:
    print(2)

elif wins >= 1 and wins <= 2:
    print(3)

else: print(-1)