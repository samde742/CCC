T = input()
L = len(T) // 2

places = {"Ottawa": [0,00], "Victoria": [-3,00], "Edmonton": [-2,00], "Winnipeg": [-1,00], 
"Toronto": [0,00], "Halifax": [1,00], "St. John's": [1,30]}

for k,v in places.items():
    if len(T) == 2 or len(T) == 1:
        TL = [0, int(T)]
    else:
        TL = [int(T[:L]), int(T[L:])]
    
    for i in v:
        index = v.index(i)
        TL[index] += i

    if TL[1] < 10:
        TL.insert(1, 0)

    if TL[1] >= 60:
        TL[1] -= 60
        TL[0] += 1


    if TL[0] >= 24:
        TL[0] -= 24
    
    if TL[0] < 0:
        TL[0] += 24

    if TL[0] == 0:
        del TL[0]
    final = []
    for i in TL:
        final.append(str(i))

    print(f"{''.join(final)} in {k}", TL)






# for k,v in places.items():
#     if len(T) == 2 or len(T) == 1:
#         TL = [0, int(T)]
#     else:
#         TL = [int(T[:L]), int(T[L:])]

#     for i in v:
#         index = v.index(i)
#         TL[index] += i

#         if TL[0] >= 24:
#             TL[0] -= 24
#         if TL[1] >= 60:
#             TL[1] -= 60
#             TL[0] += 1
#             if TL[1] < 10:
#                 TL.insert(1, 0)
#         if TL[0] < 0:
#             TL[0] += 12

#     final = []
#     for i in TL:
#         final.append(str(i))

#     if TL[0] == 0 and len(T) != 1:
#         print(f"{''.join(final[1])} in {k}")

#     elif len(T) == 1:
#         if final[0] == "0":
#             final.remove(final[0])
#         else:
#             final.insert(1, "0")
#         print(f"{''.join(final)} in {k}")
    
#     else:
#         print(f"{''.join(final)} in {k}")


