A = input().upper()
UL = list(A)
A = list(A)
A.sort()

swaps = 0
runs = 0
def sort_books(swaps):
    """find amount of swaps to put books back into normal order"""
    while A != UL:
        for i in UL:

            #find index of item in UL(wrong place) and item in A(right place)
            ULI = UL.index(i)
            AI = A.index(i)
            
            #if pos of the letter in wanted order is not the letter 
            if UL[AI] != i:
                
                #swaps letters
                replace = UL[AI]
                UL[ULI] = replace
                UL[AI] = i
                    
                swaps +=1
                
    return swaps
print(sort_books(swaps))







#get order
#sort, keep old
#L

