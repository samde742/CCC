#ask how many lines
#for i in range(N)
#loop through nums, and random numbers to find 2 primes

T = int(input())

nums = []

for i in range(T):
    num = int(input())
    nums.append(num)

solved = False

for v in nums:
    sum = v*2
    n2 = 0

    for i in range(2, v):
        prime = False
        wrong = False
        

        for x in range(2,i):
            
            if i % x == 0 and i != x:
                prime = False
                break
            else:
                n = i
                prime = True
                

        if prime == True:
            n2 = v*2 - n
            
        
        for x in range(2, n2):

            if n2 % x == 0 and n2 != x:
                solved = False
                break

            else:
                solved = True
        
        if solved == True and wrong == False:
            if (n + n2) == sum:
                print(f"{n} {n2}")
                break
