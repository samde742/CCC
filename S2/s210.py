#Huffman Encoding
K = int(input())

key = {}

for i in range(K):
    #take keys and add to dict
    assign = input().split(" ")
    key[assign[1]] = assign[0]

message = input()
analyse = ""
final = ""

for i in message:
    analyse += "".join(i)
    for k,v in key.items():
        if analyse == k:
            final += "".join(v)
            analyse = ""
    
print(final)
