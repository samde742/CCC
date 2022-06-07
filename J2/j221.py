N = int(input())

bids = {}

for i in range(N):
    name = input()
    b = int(input())

    bids[name] = b

win = max(bids.values())

for k,v in bids.items():
    if v == win:
        print(k)
        break